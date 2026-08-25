# pairwise(_:scale:judge:scoringMode:evaluationTarget:)

**Framework**: Evaluations  
**Kind**: method

Creates a pairwise comparison evaluator that compares the model’s response against the sample’s expected value.

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
static func pairwise(_ name: String, scale: ScoringScale, judge: any LanguageModel, scoringMode: ScoringMode = .discrete, evaluationTarget: (@Sendable (Input.ExpectedValue) -> String)? = nil) -> ModelJudgeEvaluator<Input>
```

## Mentions

- [Scoring with model-judge evaluators](scoring-with-model-as-judge-evaluators.md)

#### Discussion

The judge sees the model’s output under “Response” and the expected value from `input.expected` under “Baseline Response” in the Context section.

## Parameters

- `name`: The metric name that corresponds to the DataFrame column.
- `scale`: Scoring scale for the comparison.
- `judge`: The language model to use as judge.
- `scoringMode`: A value that indicates whether scores are discrete (default) or allow any floating-point value.
- `evaluationTarget`: An optional closure that converts the value to a string. Both responses use this target.

## See Also

- [static func pairwise(judge: any LanguageModel, dimensions: [ScoreDimension], scoringMode: ScoringMode, evaluationTarget: ((Input.ExpectedValue) -> String)?) -> ModelJudgeEvaluator<Input>](modeljudgeevaluator/pairwise(judge:dimensions:scoringmode:evaluationtarget:).md)
  Creates a multi-metric pairwise comparison evaluator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modeljudgeevaluator/pairwise(_:scale:judge:scoringmode:evaluationtarget:))*