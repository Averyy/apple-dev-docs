# EvaluationRunErrors

**Framework**: Evaluations  
**Kind**: struct  
**Role**: Structure

A summary of the failures encountered during an evaluation run.

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
struct EvaluationRunErrors
```

## Overview

Retrieved via [`errors`](./evaluationresult/errors.md).

## Topics

### Checking for failures
- [var hasFailures: Bool](./evaluationrunerrors/hasfailures.md)
  Whether this represents any failure worth persisting.
- [static let clean: EvaluationRunErrors](./evaluationrunerrors/clean.md)
  Used as the default when loading a file that carries no `runErrors`.
### Counting failures
- [var inferenceFailureCount: Int](./evaluationrunerrors/inferencefailurecount.md)
  The number of samples whose subject failed to be produced.
- [var evaluatorFailureCount: Int](./evaluationrunerrors/evaluatorfailurecount.md)
  The total number of evaluator invocations that threw.
- [var failingEvaluatorTypes: Set<String>](./evaluationrunerrors/failingevaluatortypes.md)
  The set of evaluator type names that threw at least once.
### Diagnosing a run
- [var anyInferenceProduced: Bool](./evaluationrunerrors/anyinferenceproduced.md)
  Whether any sample produced a subject.
- [var metricsNotFound: [String]](./evaluationrunerrors/metricsnotfound.md)
  Metric names referenced by `MetricsAggregator` that no evaluator produced.
### Default Implementations
- [Decodable Implementations](./evaluationrunerrors/decodable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Results
- [struct EvaluationResult](./evaluationresult.md)
  The results of running a model evaluation.
- [struct ResultColumn](./resultcolumn.md)
  A typed descriptor for a column in an evaluation result DataFrame.
- [var inputColumn: ResultColumn<Self.Sample>](./evaluation/inputcolumn.md)
  A typed column descriptor for the input samples in the detailed DataFrame.
- [var responseColumn: ResultColumn<Self.Subject>](./evaluation/responsecolumn.md)
  A typed column descriptor for the model responses in the detailed DataFrame.
- [var expectedColumn: ResultColumn<Self.Sample.ExpectedValue>](./evaluation/expectedcolumn.md)
  A typed column descriptor for the expected values in the detailed DataFrame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluationrunerrors)*