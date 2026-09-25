# xcodeOverview.AppMetadata

**Framework**: App Store Connect API  
**Kind**: dictionary

Metadata about the app that a performance overview describes.

**Availability**:
- App Store Connect API 4.5+

## Declaration

```swift
object xcodeOverview.AppMetadata
```

## Properties

- `bundleId` (string): The bundle ID of the app.
- `appId` (string): The App Store identifier of the app.
- `latestVersion` (string): The most recent version of the app.
- `platform` (string): The platform that the performance data applies to.

## See Also

- [object xcodeOverview.Insights](xcodeoverview/insights-data.dictionary.md)
  Performance insights for an app, including regressions and metrics that are trending up.
- [object xcodeOverview.Signatures](xcodeoverview/signatures-data.dictionary.md)
  The top performance signatures for an app, such as its top hang, launch, and disk-write points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/xcodeoverview/appmetadata-data.dictionary)*