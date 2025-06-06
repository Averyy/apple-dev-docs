# applicationVersion

**Framework**: MetricKit  
**Kind**: property

The value of the bundle version key, short form, in the app’s property list.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var applicationVersion: String { get }
```

#### Discussion

Returns the value of [`CFBundleShortVersionString`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleShortVersionString) from this app’s information property list.

## See Also

- [var metaData: MXMetaData](mxdiagnostic/metadata.md)
  A set of system-level information for the device.
- [var signpostData: [MXSignpostRecord]?](mxdiagnostic/signpostdata.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxdiagnostic/applicationversion)*