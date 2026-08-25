# EvaluationRunErrors

**Framework**: Evaluations  
**Kind**: struct

A summary of the failures encountered during an evaluation run.

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
struct EvaluationRunErrors
```

#### Overview

Retrieved via [`errors`](evaluationresult/errors.md).

## Topics

### Instance Properties
- [var anyInferenceProduced: Bool](evaluationrunerrors/anyinferenceproduced.md)
  Whether any sample produced a subject.
- [var evaluatorFailureCount: Int](evaluationrunerrors/evaluatorfailurecount.md)
  The total number of evaluator invocations that threw.
- [var failingEvaluatorTypes: Set<String>](evaluationrunerrors/failingevaluatortypes.md)
  The set of evaluator type names that threw at least once.
- [var hasFailures: Bool](evaluationrunerrors/hasfailures.md)
  Whether this represents any failure worth persisting.
- [var inferenceFailureCount: Int](evaluationrunerrors/inferencefailurecount.md)
  The number of samples whose subject failed to be produced.
- [var metricsNotFound: [String]](evaluationrunerrors/metricsnotfound.md)
  Metric names referenced by `MetricsAggregator` that no evaluator produced.
### Type Properties
- [static let clean: EvaluationRunErrors](evaluationrunerrors/clean.md)
  Used as the default when loading a file that carries no `runErrors`.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluationrunerrors)*