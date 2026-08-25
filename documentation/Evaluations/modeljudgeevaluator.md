# ModelJudgeEvaluator

**Framework**: Evaluations  
**Kind**: struct

An evaluator that uses a language model as a judge to score responses.

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
struct ModelJudgeEvaluator<Input> where Input : ModelSampleProtocol
```

## Mentions

- [Scoring with model-judge evaluators](scoring-with-model-as-judge-evaluators.md)
- [Designing effective model-judge evaluators](designing-effective-model-judges.md)
- [Designing specific, measurable criteria in an evaluation suite](designing-evaluation-criteria.md)
- [Evaluating language model responses](evaluating-language-model-responses.md)

#### Overview

`ModelJudgeEvaluator` sends the query, response, and optional reference data to a model judge, which returns scores for one or more dimensions. The response is automatically serialized as JSON, because `OutputType` is `Codable`, or is customizable via [`ModelJudgePrompt`](modeljudgeprompt.md).

## Topics

### Creating a single-dimension evaluator
- [init(String, scale: ScoringScale, judge: any LanguageModel, scoringMode: ScoringMode)](modeljudgeevaluator/init(_:scale:judge:scoringmode:).md)
  Creates a single-metric evaluator with default prompt configuration.
- [init(String, scale: ScoringScale, judge: any LanguageModel, scoringMode: ScoringMode, prompt: ModelJudgePrompt<Input>)](modeljudgeevaluator/init(_:scale:judge:scoringmode:prompt:).md)
  Creates a single-metric evaluator with a custom judge prompt.
### Creating a multi-dimension evaluator
- [init(judge: any LanguageModel, dimensions: [ScoreDimension], scoringMode: ScoringMode)](modeljudgeevaluator/init(judge:dimensions:scoringmode:).md)
  Creates a multi-metric evaluator with default prompt configuration.
- [init(judge: any LanguageModel, dimensions: [ScoreDimension], scoringMode: ScoringMode, prompt: ModelJudgePrompt<Input>)](modeljudgeevaluator/init(judge:dimensions:scoringmode:prompt:).md)
  Creates a multi-metric evaluator with a custom judge prompt.
### Creating a pairwise evaluator
- [static func pairwise(String, scale: ScoringScale, judge: any LanguageModel, scoringMode: ScoringMode, evaluationTarget: ((Input.ExpectedValue) -> String)?) -> ModelJudgeEvaluator<Input>](modeljudgeevaluator/pairwise(_:scale:judge:scoringmode:evaluationtarget:).md)
  Creates a pairwise comparison evaluator that compares the model’s response against the sample’s expected value.
- [static func pairwise(judge: any LanguageModel, dimensions: [ScoreDimension], scoringMode: ScoringMode, evaluationTarget: ((Input.ExpectedValue) -> String)?) -> ModelJudgeEvaluator<Input>](modeljudgeevaluator/pairwise(judge:dimensions:scoringmode:evaluationtarget:).md)
  Creates a multi-metric pairwise comparison evaluator.
### Configuring the judge prompt
- [static var defaultInstructions: String](modeljudgeevaluator/defaultinstructions.md)
  The default system instructions the model uses when no custom instructions are provided.
- [func judgePrompt(for: Input, output: Input.ExpectedValue) async throws -> Prompt](modeljudgeevaluator/judgeprompt(for:output:).md)
  Builds and returns the full judge prompt for inspection, debugging, or logging.
### Inspecting the evaluator
- [let dimensions: [ScoreDimension]](modeljudgeevaluator/dimensions.md)
  The dimensions this evaluator scores.
- [let scoringMode: ScoringMode](modeljudgeevaluator/scoringmode.md)
  The scoring constraint mode. See [`ScoringMode`](scoringmode.md).
- [enum ScoringMode](scoringmode.md)
  The scoring constraint mode for a model evaluator.
### Errors
- [enum ModelJudgeError](modeljudgeerror.md)

## Relationships

### Conforms To
- [EvaluatorProtocol](evaluatorprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [Designing effective model-judge evaluators](designing-effective-model-judges.md)
  Configure model-judge evaluators that produce scores you correlate with human review.
- [Scoring with model-judge evaluators](scoring-with-model-as-judge-evaluators.md)
  Score subjective qualities like tone, accuracy, and relevance that programmatic checks cannot measure.
- [struct ModelJudgePrompt](modeljudgeprompt.md)
  A configuration for how a model evaluator constructs its prompt.
- [struct ScoreDimension](scoredimension.md)
  A named scoring dimension for a model evaluator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modeljudgeevaluator)*