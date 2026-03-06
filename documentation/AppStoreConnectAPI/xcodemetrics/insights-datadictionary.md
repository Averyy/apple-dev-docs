# xcodeMetrics.Insights

**Framework**: App Store Connect API  
**Kind**: dictionary

Analysis of power and performance data collected for your app that includes regressions and trends.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```swift
object xcodeMetrics.Insights
```

## Properties

- `regressions` ([MetricsInsight]): An array of metrics that have significantly increased between app versions.
- `trendingUp` ([MetricsInsight]): An array of metrics that have moderately increased between app versions.

## See Also

- [object xcodeMetrics.ProductData](xcodemetrics/productdata-data.dictionary.md)
  The metrics information of an app on a specific platform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/xcodemetrics/insights-data.dictionary)*