# xcodeOverview.Insights

**Framework**: App Store Connect API  
**Kind**: dictionary

Performance insights for an app, including regressions and metrics that are trending up.

**Availability**:
- App Store Connect API 4.5+

## Declaration

```swift
object xcodeOverview.Insights
```

## Properties

- `regressions` ([MetricsInsight]): The metrics that regressed relative to a previous version.
- `trendingUp` ([MetricsInsight]): The metrics that are improving relative to a previous version.

## See Also

- [object xcodeOverview.AppMetadata](xcodeoverview/appmetadata-data.dictionary.md)
  Metadata about the app that a performance overview describes.
- [object xcodeOverview.Signatures](xcodeoverview/signatures-data.dictionary.md)
  The top performance signatures for an app, such as its top hang, launch, and disk-write points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/xcodeoverview/insights-data.dictionary)*