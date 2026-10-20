# latestApplicationVersion

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The version of the app on the device at the end of the reporting period.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`latestApplicationVersion`](../metricreport/environment-swift.struct/latestapplicationversion.md) instead.

## Declaration

```swift
var latestApplicationVersion: String { get }
```

```objc
@property (strong, readonly, nonnull) NSString * latestApplicationVersion;
```

## See Also

### Reading information about the payload
- [var timeStampBegin: Date](./timestampbegin.md)
  The starting time of the reporting period.
- [var timeStampEnd: Date](./timestampend.md)
  The ending time of the reporting period.
- [var includesMultipleApplicationVersions: Bool](./includesmultipleapplicationversions.md)
  A Boolean indicating if the version of the app changed at least once during the reporting period.
- [var metaData: MXMetaData?](./metadata.md)
  A set of system-level information for the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetricpayload/latestapplicationversion)*