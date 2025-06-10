# timeStampBegin

**Framework**: MetricKit  
**Kind**: property

The starting time of the reporting period.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var timeStampBegin: Date { get }
```

## See Also

- [var timeStampEnd: Date](mxmetricpayload/timestampend.md)
  The ending time of the reporting period.
- [var includesMultipleApplicationVersions: Bool](mxmetricpayload/includesmultipleapplicationversions.md)
  A Boolean indicating if the version of the app changed at least once during the reporting period.
- [var latestApplicationVersion: String](mxmetricpayload/latestapplicationversion.md)
  The version of the app on the device at the end of the reporting period.
- [var metaData: MXMetaData?](mxmetricpayload/metadata.md)
  A set of system-level information for the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetricpayload/timestampbegin)*