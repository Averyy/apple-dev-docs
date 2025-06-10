# metaData

**Framework**: MetricKit  
**Kind**: property

A set of system-level information for the device.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var metaData: MXMetaData? { get }
```

## See Also

- [var timeStampBegin: Date](mxmetricpayload/timestampbegin.md)
  The starting time of the reporting period.
- [var timeStampEnd: Date](mxmetricpayload/timestampend.md)
  The ending time of the reporting period.
- [var includesMultipleApplicationVersions: Bool](mxmetricpayload/includesmultipleapplicationversions.md)
  A Boolean indicating if the version of the app changed at least once during the reporting period.
- [var latestApplicationVersion: String](mxmetricpayload/latestapplicationversion.md)
  The version of the app on the device at the end of the reporting period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetricpayload/metadata)*