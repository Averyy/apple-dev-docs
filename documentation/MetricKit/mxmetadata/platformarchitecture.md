# platformArchitecture

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The name of the processor architecture for the device.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`platformArchitecture`](../metricreport/environment-swift.struct/platformarchitecture.md) or [`platformArchitecture`](../diagnosticreport/environment-swift.struct/platformarchitecture.md) instead.

## Declaration

```swift
var platformArchitecture: String { get }
```

```objc
@property (strong, readonly, nonnull) NSString * platformArchitecture;
```

## See Also

### Reading data about a payload
- [var applicationBuildVersion: String](./applicationbuildversion.md)
  The value of the bundle version key in the app’s property list.
- [var deviceType: String](./devicetype.md)
  The hardware identifier for the device.
- [var isTestFlightApp: Bool](./istestflightapp.md)
  Indicates whether the app is registered with TestFlight.
- [var lowPowerModeEnabled: Bool](./lowpowermodeenabled.md)
  Indicates whether low power mode is enabled on the device.
- [var osVersion: String](./osversion.md)
  The version of the OS on the device including the type of OS, version number, and build number.
- [var regionFormat: String](./regionformat.md)
  The short country code for the region format setting of the device.
- [var pid: pid_t](./pid.md)
  The process ID (PID) of the process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetadata/platformarchitecture)*