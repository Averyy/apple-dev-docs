# init(judge:dimensions:scoringMode:prompt:)

**Framework**: Evaluations  
**Kind**: init  
**Role**: Initializer

Creates a multi-metric evaluator with a custom model prompt.

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
init(judge: any LanguageModel, dimensions: [ScoreDimension], scoringMode: ScoringMode = .discrete, prompt: ModelJudgePrompt<Input>)
```

## Discussion

```swift
let prompt = ModelJudgePrompt<ModelSample<String>>(
    instructions: "Score the response on multiple dimensions."
)
let evaluator = ModelJudgeEvaluator<ModelSample<String>>(
    judge: SystemLanguageModel.default,
    dimensions: [
        ScoreDimension("Quality", scale: .passFail(passDescription: "Good", failDescription: "Poor"))
    ],
    prompt: prompt
)
```

## Parameters

- `judge`: The language model to use as judge.
- `dimensions`: The dimensions to score. Each produces a separate DataFrame column.
- `scoringMode`: Whether scores are discrete (default) or allow any floating-point value.
- `prompt`: Configuration for the model prompt, including instructions, response presentation, and reference.

## See Also

### Creating a multi-dimension evaluator
- [init(judge: any LanguageModel, dimensions: [ScoreDimension], scoringMode: ScoringMode)](./init%28judge,dimensions,scoringmode%29.md)
  Creates a multi-metric evaluator with default prompt configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modeljudgeevaluator/init(judge:dimensions:scoringmode:prompt:))*