# Metric

**Framework**: Evaluations  
**Kind**: struct  
**Role**: Structure

A named metric that carries a result value.

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
struct Metric
```

## Mentions

- [Scoring with model-judge evaluators](./scoring-with-model-as-judge-evaluators.md)
- [Evaluating language model responses](./evaluating-language-model-responses.md)
- [Evaluating tool-calling behavior](./evaluating-tool-calling-behavior.md)

## Overview

Use `Metric` to define a named measurement. The factory methods (`passing`, `failing`, `scoring`, `ignore`) return a new `Metric` with the result stored inside.

Here’s how you create a custom metric:

```swift
let metric = Metric("Accuracy")
let result = metric.passing(rationale: "Exact match")
```

## Topics

### Creating a metric
- [init(String, description: String?)](./metric/init%28_,description%29.md)
  Creates a metric with a name and an optional description.
### Producing results
- [func passing(rationale: String?) -> Metric](./metric/passing%28rationale%29.md)
  Returns a metric with a passing result.
- [func failing(rationale: String?) -> Metric](./metric/failing%28rationale%29.md)
  Returns a metric with a failing result.
- [func scoring(Double, rationale: String?) -> Metric](./metric/scoring%28_,rationale%29.md)
  Returns a metric with a numeric result.
- [func ignore(rationale: String?) -> Metric](./metric/ignore%28rationale%29.md)
  Returns a metric with an ignored result, excluded from aggregation.
### Using built-in metrics
- [static let toolsAllPass: Metric](./metric/toolsallpass.md)
  A convenience metric for the strict pass or fail result of a [`ToolCallEvaluator`](./toolcallevaluator.md).
- [static let toolsPercentagePass: Metric](./metric/toolspercentagepass.md)
  A convenience metric for the partial score result of a [`ToolCallEvaluator`](./toolcallevaluator.md).
- [static let intentsPass: Metric](./metric/intentspass.md)
  The name [`intentsAllPass`](./metric/intentsallpass.md) shipped with.
- [static let foundEntitiesPass: Metric](./metric/foundentitiespass.md)
  The name [`foundEntitiesAllPass`](./metric/foundentitiesallpass.md) shipped with.
- [static let onScreenEntitiesPass: Metric](./metric/onscreenentitiespass.md)
  The name [`onScreenEntitiesAllPass`](./metric/onscreenentitiesallpass.md) shipped with.
- [static let siriResponsePass: Metric](./metric/siriresponsepass.md)
  The name [`siriResponseAllPass`](./metric/siriresponseallpass.md) shipped with.
- [static let skillsLoadedPass: Metric](./metric/skillsloadedpass.md)
  The name [`skillsLoadedAllPass`](./metric/skillsloadedallpass.md) shipped with.
### Inspecting a result
- [let name: String](./metric/name.md)
  The name of the metric, used as the DataFrame column name.
- [let value: Metric.Value](./metric/value-swift.property.md)
  The result value of this metric.
- [var doubleValue: Double?](./metric/doublevalue.md)
  The numeric value of this metric.
- [let rationale: String?](./metric/rationale.md)
  An optional rationale describing the result.
- [let metricDescription: String?](./metric/metricdescription.md)
  An optional description of the associated metric.
- [Metric.Value](./metric/value-swift.enum.md)
  A metric result value.
- [var description: String](./metric/description.md)
  A human-readable string representation of the metric, including its name, value, and optional rationale.
### Type Properties
- [static let foundEntitiesAllPass: Metric](./metric/foundentitiesallpass.md)
  A metric that passes when every finds expectation in the scenario holds.
- [static let foundEntitiesPercentagePass: Metric](./metric/foundentitiespercentagepass.md)
  The fraction of finds expectations that held, for one scenario.
- [static let intentsAllPass: Metric](./metric/intentsallpass.md)
  A metric that passes when every intent expectation in the scenario holds.
- [static let intentsPercentagePass: Metric](./metric/intentspercentagepass.md)
  The fraction of intent expectations that held, for one scenario.
- [static let onScreenEntitiesAllPass: Metric](./metric/onscreenentitiesallpass.md)
  A metric that passes when every onscreen expectation in the scenario holds.
- [static let onScreenEntitiesPercentagePass: Metric](./metric/onscreenentitiespercentagepass.md)
  The fraction of onscreen expectations that held, for one scenario.
- [static let siriResponseAllPass: Metric](./metric/siriresponseallpass.md)
  A metric that passes when every Siri response check in the scenario holds.
- [static let siriResponsePercentagePass: Metric](./metric/siriresponsepercentagepass.md)
  The fraction of reply checks that held, for one scenario.
- [static let skillsLoadedAllPass: Metric](./metric/skillsloadedallpass.md)
  A metric that passes when Siri loaded every required skill.
### Default Implementations
- [CustomStringConvertible Implementations](./metric/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Metrics and evaluators
- [Designing specific, measurable criteria in an evaluation suite](./designing-evaluation-criteria.md)
  Define quality for your feature by choosing measurable criteria, scoring approaches, and ground-truth strategies.
- [struct Evaluator](./evaluator.md)
  A closure-based evaluator.
- [struct MetricsAggregator](./metricsaggregator.md)
  A utility for computing aggregate statistics from evaluation metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/metric)*