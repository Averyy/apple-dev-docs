# Metric

**Framework**: Evaluations  
**Kind**: struct

A named metric that carries a result value.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct Metric
```

## Mentions

- [Scoring with model-as-judge evaluators](scoring-with-model-as-judge-evaluators.md)
- [Evaluating language model responses](evaluating-language-model-responses.md)
- [Evaluating tool-calling behavior](evaluating-tool-calling-behavior.md)

#### Overview

Use `Metric` to define a named measurement. The factory methods (`passing`, `failing`, `scoring`, `ignore`) return a new `Metric` with the result stored inside.

Here’s how you create a custom metric:

```swift
let metric = Metric("Accuracy")
let result = metric.passing(rationale: "Exact match")
```

## Topics

### Creating a metric
- [init(String)](metric/init(_:).md)
  Creates a metric with just a name.
### Producing results
- [func passing(rationale: String?) -> Metric](metric/passing(rationale:).md)
  Returns a metric with a passing result.
- [func failing(rationale: String?) -> Metric](metric/failing(rationale:).md)
  Returns a metric with a failing result.
- [func scoring(Double, rationale: String?) -> Metric](metric/scoring(_:rationale:).md)
  Returns a metric with a numeric result.
- [func ignore(rationale: String?) -> Metric](metric/ignore(rationale:).md)
  Returns a metric with an ignored result, excluded from aggregation.
### Inspecting a result
- [let name: String](metric/name.md)
  The name of the metric, used as the DataFrame column name.
- [let value: Metric.Value](metric/value-swift.property.md)
  The result value of this metric.
- [var doubleValue: Double?](metric/doublevalue.md)
  The numeric value of this metric, or `nil` for ignored metrics.
- [let rationale: String?](metric/rationale.md)
  An optional rationale describing the result.
- [Metric.Value](metric/value-swift.enum.md)
  A metric result value.
### Type Properties
- [static let toolsAllPass: Metric](metric/toolsallpass.md)
  A convenience metric for the strict pass or fail result of a [`ToolCallEvaluator`](toolcallevaluator.md).
- [static let toolsPercentagePass: Metric](metric/toolspercentagepass.md)
  A convenience metric for the partial score result of a [`ToolCallEvaluator`](toolcallevaluator.md).

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Designing specific, measurable criteria in an evaluation suite](designing-evaluation-criteria.md)
  Define quality for your feature by choosing measurable criteria, scoring approaches, and ground-truth strategies.
- [struct Evaluator](evaluator.md)
  A closure-based evaluator.
- [struct MetricsAggregator](metricsaggregator.md)
  A utility for computing aggregate statistics from evaluation metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/metric)*