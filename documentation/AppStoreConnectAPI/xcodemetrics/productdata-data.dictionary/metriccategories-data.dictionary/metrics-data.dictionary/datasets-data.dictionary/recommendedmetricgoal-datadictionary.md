# xcodeMetrics.ProductData.MetricCategories.Metrics.Datasets.RecommendedMetricGoal

**Framework**: App Store Connect API  
**Kind**: dictionary

A recommeded value of a goal for a specific app metric.

**Availability**:
- App Store Connect API 4.0+

## Declaration

```swift
object xcodeMetrics.ProductData.MetricCategories.Metrics.Datasets.RecommendedMetricGoal
```

##### Overview

Xcode compares your app’s metrics against two types of goals: *similar-app goals*, which are based on metrics from apps with functional and technical similarities to yours, and *historical performance goals*, which are based on your app’s own historical data.

When Xcode has enough information to determine a goal for a metric, it is available in this resource. Use this information to plan and prioritize performance-engineering work.

## Properties

- `detail` (string): A human-readable description of the recommended metric goal.
- `value` (number): The recommended metric value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/xcodemetrics/productdata-data.dictionary/metriccategories-data.dictionary/metrics-data.dictionary/datasets-data.dictionary/recommendedmetricgoal-data.dictionary)*