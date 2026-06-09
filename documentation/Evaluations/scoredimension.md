# ScoreDimension

**Framework**: Evaluations  
**Kind**: struct

A named scoring dimension for a model judge evaluator.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct ScoreDimension
```

## Mentions

- [Scoring with model-as-judge evaluators](scoring-with-model-as-judge-evaluators.md)
- [Designing effective model-as-judge evaluators](designing-effective-model-judges.md)

#### Overview

Each dimension defines a name (used as the DataFrame column), an optional description, and a [`ScoringScale`](scoringscale.md) that defines what each score means.

```swift
ScoreDimension("Grammar", scale: .numeric([
    5: "Flawless grammar throughout",
    3: "Some errors but generally readable",
    1: "Pervasive errors making text difficult to understand"
]))
```

```swift
ScoreDimension("Safe", scale: .passFail(
    passDescription: "The response is safe and appropriate",
    failDescription: "The response contains harmful content"
))
```

```swift
enum SafetyLevel: ScoreLevel {
    case safe, unsafe
    var guideDescription: String { self == .safe ? "Safe" : "Unsafe" }
    var value: Double { self == .safe ? 1 : 0 }
}
let _ = ScoreDimension("Safety", scale: .custom(SafetyLevel.self))
```

## Topics

### Defining scales
- [struct ScoringScale](scoringscale.md)
  A scoring scale that defines the set of options a judge can assign.
- [protocol ScoreLevel](scorelevel.md)
  A type that defines individual levels within a scoring scale.
### Initializers
- [init(String, description: String?, scale: ScoringScale)](scoredimension/init(_:description:scale:).md)
  Creates a scoring dimension.
### Instance Properties
- [let description: String?](scoredimension/description.md)
  An optional description providing additional context for the judge about what this dimension measures.
- [var metric: Metric](scoredimension/metric.md)
  A metric identifier derived from this dimension’s name.
- [let name: String](scoredimension/name.md)
  The name of the dimension, used as the DataFrame column name.
- [let scale: ScoringScale](scoredimension/scale.md)
  The scoring scale for this dimension.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Designing effective model-as-judge evaluators](designing-effective-model-judges.md)
  Configure model-as-judge evaluators that produce scores you correlate with human review.
- [Scoring with model-as-judge evaluators](scoring-with-model-as-judge-evaluators.md)
  Score subjective qualities like tone, accuracy, and relevance that programmatic checks cannot measure.
- [struct ModelJudgeEvaluator](modeljudgeevaluator.md)
  An evaluator that uses a language model as a judge to score responses.
- [struct ModelJudgePrompt](modeljudgeprompt.md)
  A configuration for how a model-as-judge evaluator constructs its prompt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/scoredimension)*