# init(judge:dimensions:scoringMode:)

**Framework**: Evaluations  
**Kind**: init

Creates a multi-metric evaluator with default prompt configuration.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
init(judge: any LanguageModel, dimensions: [ScoreDimension], scoringMode: ScoringMode = .discrete)
```

## Parameters

- `judge`: The language model to use as judge. Defaults to `SystemLanguageModel.default`.
- `dimensions`: The dimensions to score. Each produces a separate DataFrame column.
- `scoringMode`: A value that indicates whether scores are discrete (default) or allow any floating-point value.

## See Also

- [init(judge: any LanguageModel, dimensions: [ScoreDimension], scoringMode: ScoringMode, prompt: ModelJudgePrompt<Input>)](modeljudgeevaluator/init(judge:dimensions:scoringmode:prompt:).md)
  Creates a multi-metric evaluator with a custom judge prompt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modeljudgeevaluator/init(judge:dimensions:scoringmode:))*