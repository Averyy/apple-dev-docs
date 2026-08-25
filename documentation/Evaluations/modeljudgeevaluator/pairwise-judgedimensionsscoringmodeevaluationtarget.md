# pairwise(judge:dimensions:scoringMode:evaluationTarget:)

**Framework**: Evaluations  
**Kind**: method

Creates a multi-metric pairwise comparison evaluator.

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
static func pairwise(judge: any LanguageModel, dimensions: [ScoreDimension], scoringMode: ScoringMode = .discrete, evaluationTarget: (@Sendable (Input.ExpectedValue) -> String)? = nil) -> ModelJudgeEvaluator<Input>
```

## Parameters

- `judge`: The language model to use as judge.
- `dimensions`: The dimensions to score for the comparison.
- `scoringMode`: A value that indicates whether scores are discrete (default) or allow any floating-point value.
- `evaluationTarget`: An optional closure that converts the value to a string. Both responses use this target.

## See Also

- [static func pairwise(String, scale: ScoringScale, judge: any LanguageModel, scoringMode: ScoringMode, evaluationTarget: ((Input.ExpectedValue) -> String)?) -> ModelJudgeEvaluator<Input>](modeljudgeevaluator/pairwise(_:scale:judge:scoringmode:evaluationtarget:).md)
  Creates a pairwise comparison evaluator that compares the model’s response against the sample’s expected value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modeljudgeevaluator/pairwise(judge:dimensions:scoringmode:evaluationtarget:))*