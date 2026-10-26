---
url: "https://docs.swift.org/latest/documentation/docc/multiplechoice"
framework: "Swift-Org/docc"
---

# MultipleChoice

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

Defines a single question and multiple possible answers to include in the Assessments section of a tutorial page.

**Availability**:
- Swift-DocC 5.5+

## Declaration

```swift
@MultipleChoice {
    ...
}
```

#### Overview

Use the `MultipleChoice` directive to define a descriptive question that assesses the reader’s knowledge after they complete the steps in a tutorial. Multiple choice questions appear in the assessments section of a tutorial  page. Provide a question and several choices.

```markdown
@Tutorial(time: 30) {
    
    ...

    @Assessments {
        @MultipleChoice {
            What element did you use to add space around and between your views?

            @Choice(isCorrect: false) {
                A state variable.

                @Justification(reaction: "Try again!") {
                    Remember, it's something you used to arrange views vertically.
                }
            }

            @Choice(isCorrect: true) {
                A `VStack` with trailing padding.

                @Justification(reaction: "That's right!") {
                    A `VStack` arranges views in a vertical line.
                }
            }

            @Choice(isCorrect: false) {
              
              ...
              
            }
        }  
    }
}
```

##### Contained Elements

A multiple choice question contains the following items:

- **[`Choice`](./choice.md)**: A possible correct or incorrect answer to the question. It’s a good idea to include 2-4 choices. **(optional)**

##### Containing Elements

The following items include multiple choice questions:

- [`Assessments`](./assessments.md)

## Topics

### Offering Choices
- [@Choice(isCorrect: Bool)](./choice.md)
  Defines a single choice for a multiple-choice question in the assessments section of a tutorial page.

## See Also

### Related Documentation
- [@Tutorial(time: Int, projectFiles: ResourceReference)](./tutorial.md)
  Displays a tutorial page that teaches your Swift framework or package APIs through interactive coding exercises.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/multiplechoice)*