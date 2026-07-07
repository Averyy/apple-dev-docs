# reference

**Framework**: Evaluations  
**Kind**: property

An optional closure that provides labeled reference data to include in the model-as-judge prompt.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
let reference: (nonisolated(nonsending) @Sendable (Input, Input.ExpectedValue) async throws -> [String : String])?
```

#### Discussion

The closure receives both the input sample and the model’s response, allowing reference data derived from either, for example, running a grammar checker on the response, or passing the sample’s expected value for comparison.

## See Also

- [let instructions: String](modeljudgeprompt/instructions.md)
  The system instructions for the judge model.
- [let evaluationTarget: ((Input.ExpectedValue) -> String)?](modeljudgeprompt/evaluationtarget.md)
  An optional closure that converts the model’s response to a string for the judge prompt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modeljudgeprompt/reference)*