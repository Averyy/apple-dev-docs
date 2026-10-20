# init(_:scale:judge:scoringMode:)

**Framework**: Evaluations  
**Kind**: init  
**Role**: Initializer

Creates a single-metric evaluator with default prompt configuration.

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
init(_ name: String, scale: ScoringScale, judge: any LanguageModel = SystemLanguageModel(), scoringMode: ScoringMode = .discrete)
```

*watchOS*

```swift
init(_ name: String, scale: ScoringScale, judge: any LanguageModel, scoringMode: ScoringMode = .discrete)
```

## Parameters

- `name`: The metric name that corresponds to the DataFrame column.
- `scale`: The scoring scale for this metric.
- `judge`: The language model to use as judge. Defaults to `SystemLanguageModel.default`.
- `scoringMode`: A value that indicates whether scores are discrete (default) or allow any floating-point value.

## See Also

### Creating a single-dimension evaluator
- [init(String, scale: ScoringScale, judge: any LanguageModel, scoringMode: ScoringMode, prompt: ModelJudgePrompt<Input>)](./init%28_,scale,judge,scoringmode,prompt%29.md)
  Creates a single-metric evaluator with a custom judge prompt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modeljudgeevaluator/init(_:scale:judge:scoringmode:))*