---
url: "https://docs.swift.org/latest/documentation/docc/assessments"
framework: "Swift-Org/docc"
---

# Assessments

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

Tests the reader’s knowledge at the end of a tutorial page.

**Availability**:
- Swift-DocC 5.5+

## Declaration

```swift
@Assessments {
    @MultipleChoice { ... }
}
```

## Mentions

- [Building an Interactive Tutorial](./building-an-interactive-tutorial.md)

#### Overview

Use the `Assessment` directive to display an assessments section that helps the reader check their knowledge of your Swift framework or package APIs at the end of a tutorial page. An assessment includes a set of multiple-choice questions that you create using the [`MultipleChoice`](./multiplechoice.md) directive. If the reader gets a question wrong, you can provide a hint that points them toward the correct answer so they can try again.

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

An assessment contains the following items:

- **[`MultipleChoice`](./multiplechoice.md)**: A question with multiple possible answers that tests the reader’s knowledge about content within the tutorial. It’s a good practice to include 3-4 multiple choice questions. **(optional)**

##### Containing Elements

The following items include assessments:

- [`Tutorial`](./tutorial.md)

## Topics

### Defining Questions
- [@MultipleChoice](./multiplechoice.md)
  Defines a single question and multiple possible answers to include in the Assessments section of a tutorial page.

## See Also

### Related Documentation
- [@Tutorial(time: Int, projectFiles: ResourceReference)](./tutorial.md)
  Displays a tutorial page that teaches your Swift framework or package APIs through interactive coding exercises.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/assessments)*