# signpostData

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 17.0+ - Deprecated in 27.2
- iPadOS 17.0+ - Deprecated in 27.2
- Mac Catalyst 17.0+ - Deprecated in 27.0
- macOS 14.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`signpostData`](../diagnosticreport/environment-swift.struct/signpostdata.md) instead.

## Declaration

```swift
var signpostData: [MXSignpostRecord]? { get }
```

```objc
@property (strong, readonly, nullable) NSArray<MXSignpostRecord *> * signpostData;
```

## See Also

### Reading data About a diagnostic
- [var applicationVersion: String](./applicationversion.md)
  The value of the bundle version key, short form, in the app’s property list.
- [var metaData: MXMetaData](./metadata.md)
  A set of system-level information for the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxdiagnostic/signpostdata)*