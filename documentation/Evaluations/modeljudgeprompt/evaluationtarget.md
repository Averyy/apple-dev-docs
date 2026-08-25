# evaluationTarget

**Framework**: Evaluations  
**Kind**: property

An optional closure that converts the model’s response to a string for the model prompt.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)
- Xcode 27.0+ (Beta)

## Declaration

```swift
let evaluationTarget: (@Sendable (Input.ExpectedValue) -> String)?
```

#### Discussion

When `nil`, the evaluator JSON-serializes the response automatically.

## See Also

- [let instructions: String](modeljudgeprompt/instructions.md)
  The system instructions for the model judge.
- [let reference: ((Input, Input.ExpectedValue) async throws -> [String : String])?](modeljudgeprompt/reference.md)
  An optional closure that provides labeled reference data to include in the model prompt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modeljudgeprompt/evaluationtarget)*