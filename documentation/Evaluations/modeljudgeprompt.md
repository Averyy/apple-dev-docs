# ModelJudgePrompt

**Framework**: Evaluations  
**Kind**: struct

A configuration for how a model-as-judge evaluator constructs its prompt.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct ModelJudgePrompt<Input> where Input : ModelSampleProtocol
```

## Mentions

- [Scoring with model-as-judge evaluators](scoring-with-model-as-judge-evaluators.md)

#### Overview

```swift
let prompt = ModelJudgePrompt<ModelSample<String>>(
    instructions: "You are a domain expert evaluating product reviews."
)
```

`ModelJudgePrompt` bundles the instructions, response presentation, and reference-data injection into a single composable value. Use it with [`ModelJudgeEvaluator`](modeljudgeevaluator.md) to customize how the model as judge sees the evaluation.

## Topics

### Creating a prompt configuration
- [init(instructions: String, evaluationTarget: ((Input.ExpectedValue) -> String)?, reference: ((Input, Input.ExpectedValue) async throws -> [String : String])?)](modeljudgeprompt/init(instructions:evaluationtarget:reference:).md)
  Creates a model-as-judge prompt configuration.
- [static var defaultInstructions: String](modeljudgeprompt/defaultinstructions.md)
  The default system instructions used when no custom instructions are provided.
### Customizing judge input
- [let instructions: String](modeljudgeprompt/instructions.md)
  The system instructions for the judge model.
- [let evaluationTarget: ((Input.ExpectedValue) -> String)?](modeljudgeprompt/evaluationtarget.md)
  An optional closure that converts the model’s response to a string for the judge prompt.
- [let reference: ((Input, Input.ExpectedValue) async throws -> [String : String])?](modeljudgeprompt/reference.md)
  An optional closure that provides labeled reference data to include in the model-as-judge prompt.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [Designing effective model-as-judge evaluators](designing-effective-model-judges.md)
  Configure model-as-judge evaluators that produce scores you correlate with human review.
- [Scoring with model-as-judge evaluators](scoring-with-model-as-judge-evaluators.md)
  Score subjective qualities like tone, accuracy, and relevance that programmatic checks cannot measure.
- [struct ModelJudgeEvaluator](modeljudgeevaluator.md)
  An evaluator that uses a language model as a judge to score responses.
- [struct ScoreDimension](scoredimension.md)
  A named scoring dimension for a model judge evaluator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modeljudgeprompt)*