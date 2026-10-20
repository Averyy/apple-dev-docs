# isTestFlightApp

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

Indicates whether the app is registered with TestFlight.

**Availability**:
- iOS 17.0+ - Deprecated in 27.2
- iPadOS 17.0+ - Deprecated in 27.2
- Mac Catalyst 17.0+ - Deprecated in 27.0
- macOS 14.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`isTestFlightApp`](../metricreport/environment-swift.struct/istestflightapp.md) or [`isTestFlightApp`](../diagnosticreport/environment-swift.struct/istestflightapp.md) instead.

## Declaration

```swift
var isTestFlightApp: Bool { get }
```

```objc
@property (readonly) bool isTestFlightApp;
```

## See Also

### Reading data about a payload
- [var applicationBuildVersion: String](./applicationbuildversion.md)
  The value of the bundle version key in the app’s property list.
- [var deviceType: String](./devicetype.md)
  The hardware identifier for the device.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetadata/istestflightapp)*