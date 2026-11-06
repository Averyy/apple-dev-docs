# pairwise(_:scale:judge:scoringMode:evaluationTarget:)

**Framework**: Evaluations  
**Kind**: method  
**Role**: Type Method

Creates a pairwise comparison evaluator that compares the model’s response against the sample’s expected value.

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
static func pairwise(_ name: String, scale: ScoringScale, judge: any LanguageModel, scoringMode: ScoringMode = .discrete, evaluationTarget: (@Sendable (Input.ExpectedValue) -> String)? = nil) -> ModelJudgeEvaluator<Input>
```

## Mentions

- [Scoring with model-judge evaluators](../scoring-with-model-as-judge-evaluators.md)

## Discussion

The model judge sees the model’s output under “Response” and the expected value from `input.expected` under “Baseline Response” in the Context section.

```swift
let evaluator = ModelJudgeEvaluator<ModelSample<String>>.pairwise(
    "Similarity",
    scale: .passFail(passDescription: "Similar", failDescription: "Dissimilar"),
    judge: SystemLanguageModel.default
)
```

## Parameters

- `name`: The metric name, used as the DataFrame column name.
- `scale`: Scoring scale for the comparison.
- `judge`: The language model to use as judge.
- `scoringMode`: Whether scores are discrete (default) or allow any floating-point value.
- `evaluationTarget`: Optional closure to convert the value to a string. Used for both responses.

## See Also

### Creating a pairwise evaluator
- [static func pairwise(judge: any LanguageModel, dimensions: [ScoreDimension], scoringMode: ScoringMode, evaluationTarget: ((Input.ExpectedValue) -> String)?) -> ModelJudgeEvaluator<Input>](./pairwise%28judge,dimensions,scoringmode,evaluationtarget%29.md)
  Creates a multi-metric pairwise comparison evaluator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modeljudgeevaluator/pairwise(_:scale:judge:scoringmode:evaluationtarget:))*