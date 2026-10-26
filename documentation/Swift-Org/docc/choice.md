---
url: "https://docs.swift.org/latest/documentation/docc/choice"
framework: "Swift-Org/docc"
---

# Choice

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

Defines a single choice for a multiple-choice question in the assessments section of a tutorial page.

**Availability**:
- Swift-DocC 5.5+

## Declaration

```swift
@Choice(isCorrect: Bool) {
    ...

    @Justification(reaction: String?) { ... }
}
```

#### Overview

Use the `Choice` directive to define a single possible answer for a multiple-choice assessment question in a tutorial. Use the `isCorrect` parameter to denote whether the choice is a correct or incorrect answer. Then, use the [`Justification`](./justification.md) directive to explain why. Optionally, you can display an image for a choice.

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

            ...
           
        }
    }
}
```

##### Contained Elements

A choice can contain the following items:

- **[`Justification`](./justification.md)**: Text that explains why the choice is either correct or incorrect. **(required)**
- **[`Image`](./image.md)**: An image that accompanies the choice. **(optional)**

##### Containing Elements

The following items must include a choice:

- [`MultipleChoice`](./multiplechoice.md)

## Parameters

- `isCorrect`: A Boolean `true` or `false` value that denotes whether this choice is a correct or incorrect answer. **(required)**

## Topics

### Responding to the Choice
- [@Justification(reaction: String)](./justification.md)
  Displays text that explains why a chosen multiple-choice answer is either correct or incorrect.
### Displaying an Image
- [@Image(source: ResourceReference, alt: String)](./image.md)
  Displays an image in a tutorial.

## See Also

### Related Documentation
- [@Assessments](./assessments.md)
  Tests the reader’s knowledge at the end of a tutorial page.
- [@Tutorial(time: Int, projectFiles: ResourceReference)](./tutorial.md)
  Displays a tutorial page that teaches your Swift framework or package APIs through interactive coding exercises.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/choice)*