# xcodeMetrics.ProductData

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The metrics information of an app on a specific platform.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```
object xcodeMetrics.ProductData
```

## Topics

### Objects
- [object xcodeMetrics.ProductData.MetricCategories](./productdata-data.dictionary/metriccategories-data.dictionary.md)
  A metric category and its associated array of data and measurements.

## Properties

- `metricCategories` ([xcodeMetrics.ProductData.MetricCategories]): An array of metrics by category.
- `platform` (string): The Apple platform on which the system gathered the metrics about your app.

## See Also

### Objects
- [object xcodeMetrics.Insights](./insights-data.dictionary.md)
  Analysis of power and performance data collected for your app that includes regressions and trends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/xcodemetrics/productdata-data.dictionary)*