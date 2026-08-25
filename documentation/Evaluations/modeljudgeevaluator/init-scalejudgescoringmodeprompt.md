# init(_:scale:judge:scoringMode:prompt:)

**Framework**: Evaluations  
**Kind**: init

Creates a single-metric evaluator with a custom judge prompt.

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
init(_ name: String, scale: ScoringScale, judge: any LanguageModel, scoringMode: ScoringMode = .discrete, prompt: ModelJudgePrompt<Input>)
```

## Parameters

- `name`: The metric name that corresponds to the DataFrame column.
- `scale`: The scoring scale for this metric.
- `judge`: The language model to use as judge.
- `scoringMode`: A value that indicates whether scores are discrete (default) or allow any floating-point value.
- `prompt`: Configuration for the judge prompt, including instructions, response presentation, and reference.

## See Also

- [init(String, scale: ScoringScale, judge: any LanguageModel, scoringMode: ScoringMode)](modeljudgeevaluator/init(_:scale:judge:scoringmode:).md)
  Creates a single-metric evaluator with default prompt configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modeljudgeevaluator/init(_:scale:judge:scoringmode:prompt:))*