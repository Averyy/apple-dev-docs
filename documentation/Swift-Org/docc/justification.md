---
url: "https://docs.swift.org/latest/documentation/docc/justification"
framework: "Swift-Org/docc"
---

# Justification

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

Displays text that explains why a chosen multiple-choice answer is either correct or incorrect.

**Availability**:
- Swift-DocC 5.5+

## Declaration

```swift
@Justification(reaction: String?) {
    ...
}
```

#### Overview

Use the `Justification` directive to display a response when the reader chooses an answer in a multiple-choice assessment question in a tutorial. Use the `reaction` parameter to briefly indicate whether the choice is correct or incorrect. Then, provide some more descriptive text that explains why. In the case of an incorrect answer, consider also providing a hint so the reader can try again.

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

##### Containing Elements

The following items must include a justification:

- [`Choice`](./choice.md)

## Parameters

- `reaction`: Text that clearly and succinctly indicates whether the answer is correct or incorrect, for example “Correct!” or “Sorry, try again.” **(required)**

## See Also

### Related Documentation
- [@Assessments](./assessments.md)
  Tests the reader’s knowledge at the end of a tutorial page.
- [@Tutorial(time: Int, projectFiles: ResourceReference)](./tutorial.md)
  Displays a tutorial page that teaches your Swift framework or package APIs through interactive coding exercises.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/justification)*