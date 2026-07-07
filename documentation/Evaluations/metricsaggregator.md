# MetricsAggregator

**Framework**: Evaluations  
**Kind**: struct

A utility for computing aggregate statistics from evaluation metrics.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct MetricsAggregator
```

## Mentions

- [Designing effective evaluations](designing-effective-evaluations.md)
- [Scoring with model-as-judge evaluators](scoring-with-model-as-judge-evaluators.md)

#### Overview

```swift
let accuracy = Metric("Accuracy")

func aggregateMetrics(using aggregator: inout MetricsAggregator) {
    aggregator.computeMean(of: accuracy)
    aggregator.computeMaximum(of: accuracy)
    aggregator.computeStandardDeviation(of: accuracy)
}
```

Use this structure to calculate summary statistics like mean, median, and standard deviation from your evaluation results. The aggregator processes metric data from a DataFrame and produces aggregated results.

## Topics

### Computing standard aggregations
- [func computeMean(of: Metric)](metricsaggregator/computemean(of:).md)
  Computes the mean of a metric and adds it to the aggregated results.
- [func computeMedian(of: Metric)](metricsaggregator/computemedian(of:).md)
  Computes the median of a metric and adds it to the aggregated results.
- [func computeMode(of: Metric)](metricsaggregator/computemode(of:).md)
  Computes the mode of a metric and adds it to the aggregated results.
- [func computeMinimum(of: Metric)](metricsaggregator/computeminimum(of:).md)
  Computes the minimum value of a metric and adds it to the aggregated results.
- [func computeMaximum(of: Metric)](metricsaggregator/computemaximum(of:).md)
  Computes the maximum value of a metric and adds it to the aggregated results.
### Computing variability
- [func computeStandardDeviation(of: Metric)](metricsaggregator/computestandarddeviation(of:).md)
  Computes the standard deviation of a metric and adds it to the aggregated results.
- [func computeVariance(of: Metric)](metricsaggregator/computevariance(of:).md)
  Computes the variance of a metric and adds it to the aggregated results.
### Computing custom aggregations
- [func custom(of: Metric, label: String, ([Double]) -> Double)](metricsaggregator/custom(of:label:_:).md)
  Computes a custom aggregation from a single metric’s results.
### Grouping metrics
- [func group(String, (inout MetricsAggregator.Group) -> Void)](metricsaggregator/group(_:_:).md)
  Creates a group of related metrics.
- [MetricsAggregator.Group](metricsaggregator/group.md)
  A grouped collection of related metrics.
### Inspecting aggregate results
- [struct AggregateMetric](aggregatemetric.md)
  An aggregate statistic computed from a metric’s results across the evaluation dataset.
- [enum AggregationOperation](aggregationoperation.md)
  The type of aggregation operation used to compute a summary statistic.

## See Also

- [Designing specific, measurable criteria in an evaluation suite](designing-evaluation-criteria.md)
  Define quality for your feature by choosing measurable criteria, scoring approaches, and ground-truth strategies.
- [struct Metric](metric.md)
  A named metric that carries a result value.
- [struct Evaluator](evaluator.md)
  A closure-based evaluator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/metricsaggregator)*