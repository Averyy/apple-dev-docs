# init(_:scale:judge:scoringMode:prompt:)

**Framework**: Evaluations  
**Kind**: init  
**Role**: Initializer

Creates a single-metric evaluator with a custom model prompt.

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
init(_ name: String, scale: ScoringScale, judge: any LanguageModel, scoringMode: ScoringMode = .discrete, prompt: ModelJudgePrompt<Input>)
```

## Discussion

```swift
let prompt = ModelJudgePrompt<ModelSample<String>>(
    instructions: "Score the relevance of the response."
)
let evaluator = ModelJudgeEvaluator<ModelSample<String>>(
    "Relevance",
    scale: .passFail(passDescription: "Relevant", failDescription: "Not relevant"),
    judge: SystemLanguageModel.default,
    prompt: prompt
)
```

## Parameters

- `name`: The metric name, used as the DataFrame column name.
- `scale`: The scoring scale for this metric.
- `judge`: The language model to use as judge.
- `scoringMode`: Whether scores are discrete (default) or allow any floating-point value.
- `prompt`: Configuration for the model prompt, including instructions, response presentation, and reference.

## See Also

### Creating a single-dimension evaluator
- [init(String, scale: ScoringScale, judge: any LanguageModel, scoringMode: ScoringMode)](./init%28_,scale,judge,scoringmode%29.md)
  Creates a single-metric evaluator with default prompt configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modeljudgeevaluator/init(_:scale:judge:scoringmode:prompt:))*