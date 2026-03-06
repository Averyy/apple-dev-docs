# xcodeMetrics.ProductData.MetricCategories.Metrics.Datasets.Points

**Framework**: App Store Connect API  
**Kind**: dictionary

A metric value of a goal for a specific app version, with a breakdown by metric subtypes.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```swift
object xcodeMetrics.ProductData.MetricCategories.Metrics.Datasets.Points
```

## Topics

### Objects
- [object xcodeMetrics.ProductData.MetricCategories.Metrics.Datasets.Points.PercentageBreakdown](xcodemetrics/productdata-data.dictionary/metriccategories-data.dictionary/metrics-data.dictionary/datasets-data.dictionary/points-data.dictionary/percentagebreakdown-data.dictionary.md)
  A metric subtype and the percentage of the metric value it contributes.

## Properties

- `errorMargin` (number): The margin of error estimated based on the sample size and metric type, for metrics with an insufficient data volume. Note: For the system to provide a metric, the number of samples must meet a minimum threshold size. The `errorMargin` is present if a metric meets the minimum, but is inaccurate within a margin. If the metric surpasses a high enough threshold, the `errorMargin` isn’t present.
- `goal` (string): The metric value’s classification in terms of a goal key, such as `"good",` `"fair"`, or `"poor"`.
- `percentageBreakdown` (xcodeMetrics.ProductData.MetricCategories.Metrics.Datasets.Points.PercentageBreakdown): The percentage of the metric value each metric subtype contributes.
- `value` (number): The metric value. The `unit` field of the [`xcodeMetrics.ProductData.MetricCategories.Metrics`](xcodemetrics/productdata-data.dictionary/metriccategories-data.dictionary/metrics-data.dictionary.md) object specifies the units.
- `version` (string): The app version.

## See Also

- [object xcodeMetrics.ProductData.MetricCategories.Metrics.Datasets.FilterCriteria](xcodemetrics/productdata-data.dictionary/metriccategories-data.dictionary/metrics-data.dictionary/datasets-data.dictionary/filtercriteria-data.dictionary.md)
  The device and percentile criteria by which the system filters a metrics dataset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/xcodemetrics/productdata-data.dictionary/metriccategories-data.dictionary/metrics-data.dictionary/datasets-data.dictionary/points-data.dictionary)*