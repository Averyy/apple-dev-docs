# init(instructions:evaluationTarget:reference:)

**Framework**: Evaluations  
**Kind**: init

Creates a model-as-judge prompt configuration.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(instructions: String = ModelJudgePrompt.defaultInstructions, evaluationTarget: (@Sendable (Input.ExpectedValue) -> String)? = nil, reference: (nonisolated(nonsending) @Sendable (Input, Input.ExpectedValue) async throws -> [String : String])? = nil)
```

#### Discussion

```swift
let prompt = ModelJudgePrompt<ModelSample<String>>(
    instructions: "You are a domain expert."
)
```

## Parameters

- `instructions`: System instructions for the model-as-judge. Defaults to a general-purpose evaluator prompt.
- `evaluationTarget`: Optional closure to convert the response to a string. When `nil`, the response is JSON-serialized.
- `reference`: Optional closure returning labeled reference data to include in the judge prompt.

## See Also

- [static var defaultInstructions: String](modeljudgeprompt/defaultinstructions.md)
  The default system instructions used when no custom instructions are provided.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modeljudgeprompt/init(instructions:evaluationtarget:reference:))*