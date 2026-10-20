# pid

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The process ID (PID) of the process.

**Availability**:
- iOS 17.0+ - Deprecated in 27.2
- iPadOS 17.0+ - Deprecated in 27.2
- Mac Catalyst 17.0+ - Deprecated in 27.0
- macOS 14.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`DiagnosticReport.Environment`](../diagnosticreport/environment-swift.struct.md) instead.

## Declaration

```swift
var pid: pid_t { get }
```

```objc
@property (readonly) pid_t pid;
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
- [var platformArchitecture: String](./platformarchitecture.md)
  The name of the processor architecture for the device.
- [var regionFormat: String](./regionformat.md)
  The short country code for the region format setting of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetadata/pid)*