# pairwise(judge:dimensions:scoringMode:evaluationTarget:)

**Framework**: Evaluations  
**Kind**: method  
**Role**: Type Method

Creates a multi-metric pairwise comparison evaluator.

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
static func pairwise(judge: any LanguageModel, dimensions: [ScoreDimension], scoringMode: ScoringMode = .discrete, evaluationTarget: (@Sendable (Input.ExpectedValue) -> String)? = nil) -> ModelJudgeEvaluator<Input>
```

## Discussion

```swift
let evaluator = ModelJudgeEvaluator<ModelSample<String>>.pairwise(
    judge: SystemLanguageModel.default,
    dimensions: [
        ScoreDimension("Quality", scale: .passFail(passDescription: "Good", failDescription: "Poor")),
        ScoreDimension("Relevance", scale: .passFail(passDescription: "Relevant", failDescription: "Not relevant"))
    ]
)
```

## Parameters

- `judge`: The language model to use as judge.
- `dimensions`: The dimensions to score for the comparison.
- `scoringMode`: Whether scores are discrete (default) or allow any floating-point value.
- `evaluationTarget`: Optional closure to convert the value to a string. Used for both responses.

## See Also

### Creating a pairwise evaluator
- [static func pairwise(String, scale: ScoringScale, judge: any LanguageModel, scoringMode: ScoringMode, evaluationTarget: ((Input.ExpectedValue) -> String)?) -> ModelJudgeEvaluator<Input>](./pairwise%28_,scale,judge,scoringmode,evaluationtarget%29.md)
  Creates a pairwise comparison evaluator that compares the model’s response against the sample’s expected value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modeljudgeevaluator/pairwise(judge:dimensions:scoringmode:evaluationtarget:))*