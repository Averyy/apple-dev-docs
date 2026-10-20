# xcodeOverview.Signatures

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The top performance signatures for an app, such as its top hang, launch, and disk-write points.

**Availability**:
- App Store Connect API 4.5+

## Declaration

```
object xcodeOverview.Signatures
```

## Properties

- `topHangPoint` ([PerformanceSignature]): The code locations responsible for the most hangs.
- `topLaunchPoint` ([PerformanceSignature]): The code locations responsible for the longest launch times.
- `topDiskWritePoint` ([PerformanceSignature]): The code locations responsible for the most disk writes.

## See Also

### Objects
- [object xcodeOverview.AppMetadata](./appmetadata-data.dictionary.md)
  Metadata about the app that a performance overview describes.
- [object xcodeOverview.Insights](./insights-data.dictionary.md)
  Performance insights for an app, including regressions and metrics that are trending up.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/xcodeoverview/signatures-data.dictionary)*