# init(judge:dimensions:scoringMode:)

**Framework**: Evaluations  
**Kind**: init  
**Role**: Initializer

Creates a multi-metric evaluator with default prompt configuration.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+
- Xcode 27.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, macOS, visionOS*

```swift
init(judge: any LanguageModel = SystemLanguageModel(), dimensions: [ScoreDimension], scoringMode: ScoringMode = .discrete)
```

*watchOS*

```swift
init(judge: any LanguageModel, dimensions: [ScoreDimension], scoringMode: ScoringMode = .discrete)
```

## Parameters

- `judge`: The language model to use as judge. Defaults to `SystemLanguageModel.default`.
- `dimensions`: The dimensions to score. Each produces a separate DataFrame column.
- `scoringMode`: A value that indicates whether scores are discrete (default) or allow any floating-point value.

## See Also

### Creating a multi-dimension evaluator
- [init(judge: any LanguageModel, dimensions: [ScoreDimension], scoringMode: ScoringMode, prompt: ModelJudgePrompt<Input>)](./init%28judge,dimensions,scoringmode,prompt%29.md)
  Creates a multi-metric evaluator with a custom judge prompt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modeljudgeevaluator/init(judge:dimensions:scoringmode:))*