# applicationBuildVersion

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The value of the bundle version key in the app’s property list.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`MetricReport.Environment`](../metricreport/environment-swift.struct.md) or [`DiagnosticReport.Environment`](../diagnosticreport/environment-swift.struct.md) instead.

## Declaration

```swift
var applicationBuildVersion: String { get }
```

```objc
@property (strong, readonly, nonnull) NSString * applicationBuildVersion;
```

#### Discussion

Returns the value of [`CFBundleVersion`](../../BundleResources/information-property-list/cfbundleversion.md) from this app’s information property list.

## See Also

### Reading data about a payload
- [var deviceType: String](./devicetype.md)
  The hardware identifier for the device.
- [var isTestFlightApp: Bool](./istestflightapp.md)
  Indicates whether the app is registered with TestFlight.
- [var lowPowerModeEnabled: Bool](./lowpowermodeenabled.md)
  Indicates whether low power mode is enabled on the device.
- [var osVersion: String](./osversion.md)
  The version of the OS on the device including the type of OS, version number, and build number.
- [var platformArchitecture: String](./platformarchitecture.md)
  The name of the processor architecture for the device.
- [var regionFormat: String](./regionformat.md)
  The short country code for the region format setting of the device.
- [var pid: pid_t](./pid.md)
  The process ID (PID) of the process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetadata/applicationbuildversion)*