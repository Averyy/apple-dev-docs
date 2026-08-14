# ToolCallEvaluator

**Framework**: Evaluations  
**Kind**: struct

An evaluator that verifies agentic tool calls against an expected trajectory.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct ToolCallEvaluator<Input> where Input : ModelSampleProtocol, Input.Expectation == TrajectoryExpectation
```

## Mentions

- [Evaluating tool-calling behavior](evaluating-tool-calling-behavior.md)
- [Evaluating language model responses](evaluating-language-model-responses.md)

#### Overview

Produces both a strict and partial result from a single evaluation pass.

Supports ordered sequences, unordered expectations, disallowed tool checks, and group steps.

Use the [`toolsAllPass`](metric/toolsallpass.md) and [`toolsPercentagePass`](metric/toolspercentagepass.md) conveniences for the standard metrics:

```swift
let evaluator = ToolCallEvaluator<ModelSample<String>>(
    allPass: .toolsAllPass, percentagePass: .toolsPercentagePass
)
```

## Topics

### Initializers
- [init(allPass: Metric, percentagePass: Metric)](toolcallevaluator/init(allpass:percentagepass:).md)
  Creates a new tool call expectations evaluator.
- [init(allPass: Metric, percentagePass: Metric, argumentMatchModel: any LanguageModel)](toolcallevaluator/init(allpass:percentagepass:argumentmatchmodel:).md)
  Creates a new tool call expectations evaluator with a custom language model for semantic matching of `.naturalLanguage` argument matchers.
### Instance Properties
- [let allPass: Metric](toolcallevaluator/allpass.md)
  The metric for the strict pass or fail result.
- [let percentagePass: Metric](toolcallevaluator/percentagepass.md)
  The metric for the partial score result.

## Relationships

### Conforms To
- [EvaluatorProtocol](evaluatorprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [Evaluating tool-calling behavior](evaluating-tool-calling-behavior.md)
  Analyze your model’s tool calls against expected trajectories, argument values, and call ordering.
- [struct TrajectoryExpectation](trajectoryexpectation.md)
  The expected pattern of tool calls for an evaluation.
- [enum ArgumentMatcher](argumentmatcher.md)
  The values that define how to validate a tool-call argument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/toolcallevaluator)*