# xcodeMetrics.ProductData.MetricCategories.Metrics.GoalKeys

**Framework**: App Store Connect API  
**Kind**: dictionary

A classification of a metrics value and the lower- and upper-bound values that qualify a metrics value for the classification.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```swift
object xcodeMetrics.ProductData.MetricCategories.Metrics.GoalKeys
```

## Properties

- `goalKey` (string): The name of the classification, such as `“good”`, `“fair”`, and `“poor”`.
- `lowerBound` (integer): The lower bound value to qualify for the goal key.
- `upperBound` (integer): The upper bound value to qualify for the goal key.

## See Also

- [object xcodeMetrics.ProductData.MetricCategories.Metrics.Datasets](xcodemetrics/productdata-data.dictionary/metriccategories-data.dictionary/metrics-data.dictionary/datasets-data.dictionary.md)
  A set of data containing metric values for each app version, filtered by percentile and device type.
- [object xcodeMetrics.ProductData.MetricCategories.Metrics.Unit](xcodemetrics/productdata-data.dictionary/metriccategories-data.dictionary/metrics-data.dictionary/unit-data.dictionary.md)
  A unit of measurement and its display name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/xcodemetrics/productdata-data.dictionary/metriccategories-data.dictionary/metrics-data.dictionary/goalkeys-data.dictionary)*