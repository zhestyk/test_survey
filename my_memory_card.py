from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel)
from random import shuffle
from random import randint
 
app = QApplication([])

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3



questions_list = []
questions_list.append(Question('Самый просматриваемый стример на зарубежном твич', 'xQcOW', 'SodaPoppin', 'Forsen', 'shroud'))
questions_list.append(Question('Какая столица США?', 'Vashington', 'los-angeles', 'New-York', 'Chicago'))
questions_list.append(Question('Как зовут создателя фильмов Marvel?', 'Стэнли Мартин Либер', 'Квентин Тарантино', 'Уэс Андерсон', 'Дени Вильнёв' ))
questions_list.append(Question('Какой самый большой океан в мире?', 'Тихий океан', 'Атлантический океан', 'Индийский океан', 'Северно-Ледовитый океан'))
questions_list.append(Question('Какая команда выйграла The International 10?', 'Team Spirit', 'OG', 'PSG.lgd', 'Team Secret'))
questions_list.append(Question('На какой призовой фонд был The International 10?', '40 000 000$', '2 000 000$', '10 000 000$', '5 000 000$'))
questions_list.append(Question('Какой самый популярный бренд одежды в мире?', 'Gucci', 'Nike', 'Puma', 'Adidas'))
questions_list.append(Question('Какой самый большой остров в мире?', 'Гренландия', 'Новая Гвинея', 'Калимантан(Борнео)', 'Мадагаскар'))
questions_list.append(Question('В каком году началась Первая Мировая война?', '1914', '1917', '1915', '1913'))
questions_list.append(Question('В каком году произошло восстание декабристов?', '1825', '1824', '1820', '1828'))
questions_list.append(Question('В каком году был принят указ об обязательных крестьянах?', '1842', '1845', '1822', '1839'))
questions_list.append(Question('Какая игра получила звание игры года?', 'Resident Evil Village', 'Dark Souls', 'Battlefield 2042', 'Elden Ring'))

btn_OK = QPushButton('Ответить') 
lb_Question = QLabel('Самый сложный вопрос в мире!')
 
RadioGroupBox = QGroupBox("Варианты ответов") 
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')
 
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) 
 
RadioGroupBox.setLayout(layout_ans1) 
 
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')
lb_Rating = QLabel("результат")

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
layout_res.addWidget(lb_Rating, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
 
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide() 
 
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) 
layout_line3.addStretch(1)
 
layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
 
def show_result():
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
 
def show_question():
    ''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) 
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) 
 
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
 
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer) 
    show_question() 

def check_rating(rat):
    print("Статистика")
    print("-Всего вопросов:", window.total)
    print("-Правильных ответов:", window.score)
    window.result = window.score / window.total * 100
    print("Рейтинг:", window.result)


def show_correct(res):
    ''' показать результат - установим переданный текст в надпись "результат" и покажем нужную панель '''
    lb_Result.setText(res)
    show_result()
 
def check_answer():
    ''' если выбран какой-то вариант ответа, то надо проверить и показать панель ответов'''
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score = window.score + 1
        print("Статистика")
        print("-Всего вопросов:", window.total)
        print("-Правильных ответов:", window.score)
        window.result = window.score / window.total * 100
        print("Рейтинг:", window.result)
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
        window.result = window.score / window.total * 100
        print("Рейтинг:", window.result)

def next_question():
    window.total = window.total + 1
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    print("Статистика")
    print("-Всего вопросов:", window.total)
    print("-Правильных ответов:", window.score)
    ask(q)

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()



window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')

cur_question = -1

btn_OK.clicked.connect(click_OK)
window.score = 0
window.total = 0 
window.result = 0 
next_question()
window.resize(500, 400)
window.show()
app.exec()