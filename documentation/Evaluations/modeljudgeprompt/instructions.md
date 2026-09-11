# instructions

**Framework**: Evaluations  
**Kind**: property

The system instructions for the model judge.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+
- Xcode 27.0+

## Declaration

```swift
let instructions: String
```

## Mentions

- [Designing effective model-judge evaluators](designing-effective-model-judges.md)

## See Also

- [let evaluationTarget: ((Input.ExpectedValue) -> String)?](modeljudgeprompt/evaluationtarget.md)
  An optional closure that converts the model’s response to a string for the model prompt.
- [let reference: ((Input, Input.ExpectedValue) async throws -> [String : String])?](modeljudgeprompt/reference.md)
  An optional closure that provides labeled reference data to include in the model prompt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modeljudgeprompt/instructions)*