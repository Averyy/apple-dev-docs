# init(judge:dimensions:scoringMode:prompt:)

**Framework**: Evaluations  
**Kind**: init

Creates a multi-metric evaluator with a custom judge prompt.

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
init(judge: any LanguageModel, dimensions: [ScoreDimension], scoringMode: ScoringMode = .discrete, prompt: ModelJudgePrompt<Input>)
```

## Parameters

- `judge`: The language model to use as judge.
- `dimensions`: The dimensions to score. Each produces a separate DataFrame column.
- `scoringMode`: A value that indicates whether scores are discrete (default) or allow any floating-point value.
- `prompt`: Configuration for the judge prompt, including instructions, response presentation, and reference.

## See Also

- [init(judge: any LanguageModel, dimensions: [ScoreDimension], scoringMode: ScoringMode)](modeljudgeevaluator/init(judge:dimensions:scoringmode:).md)
  Creates a multi-metric evaluator with default prompt configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modeljudgeevaluator/init(judge:dimensions:scoringmode:prompt:))*