# metaData

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

A set of system-level information for the device.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`MetricReport.Environment`](../metricreport/environment-swift.struct.md) instead.

## Declaration

```swift
var metaData: MXMetaData? { get }
```

```objc
@property (strong, readonly, nullable) MXMetaData * metaData;
```

## See Also

### Reading information about the payload
- [var timeStampBegin: Date](./timestampbegin.md)
  The starting time of the reporting period.
- [var timeStampEnd: Date](./timestampend.md)
  The ending time of the reporting period.
- [var includesMultipleApplicationVersions: Bool](./includesmultipleapplicationversions.md)
  A Boolean indicating if the version of the app changed at least once during the reporting period.
- [var latestApplicationVersion: String](./latestapplicationversion.md)
  The version of the app on the device at the end of the reporting period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetricpayload/metadata)*