# judgePrompt(for:output:)

**Framework**: Evaluations  
**Kind**: method

Builds and returns the full judge prompt for inspection, debugging, or logging.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
(nonsending) func judgePrompt(for sample: Input, output: Input.ExpectedValue) async throws -> Prompt
```

#### Return Value

The fully assembled `Prompt` that would be sent to the judge.

#### Discussion

Use this to see exactly what the judge model will receive for a given input/response pair.

## Parameters

- `sample`: The evaluation sample.
- `output`: The model’s response content.

## See Also

- [static var defaultInstructions: String](modeljudgeevaluator/defaultinstructions.md)
  The default system instructions the model uses when no custom instructions are provided.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modeljudgeevaluator/judgeprompt(for:output:))*