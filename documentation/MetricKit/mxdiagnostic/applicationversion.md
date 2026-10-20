# applicationVersion

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The value of the bundle version key, short form, in the app’s property list.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`applicationVersion`](../diagnosticreport/environment-swift.struct/applicationversion.md) instead.

## Declaration

```swift
var applicationVersion: String { get }
```

```objc
@property (strong, readonly, nonnull) NSString * applicationVersion;
```

#### Discussion

Returns the value of [`CFBundleShortVersionString`](../../BundleResources/information-property-list/cfbundleshortversionstring.md) from this app’s information property list.

## See Also

### Reading data About a diagnostic
- [var metaData: MXMetaData](./metadata.md)
  A set of system-level information for the device.
- [var signpostData: [MXSignpostRecord]?](./signpostdata.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxdiagnostic/applicationversion)*