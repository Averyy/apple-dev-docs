# metaData

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

A set of system-level information for the device.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`DiagnosticReport.Environment`](../diagnosticreport/environment-swift.struct.md) instead.

## Declaration

```swift
var metaData: MXMetaData { get }
```

```objc
@property (strong, readonly, nonnull) MXMetaData * metaData;
```

## See Also

### Reading data About a diagnostic
- [var applicationVersion: String](./applicationversion.md)
  The value of the bundle version key, short form, in the app’s property list.
- [var signpostData: [MXSignpostRecord]?](./signpostdata.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxdiagnostic/metadata)*