# osVersion

**Framework**: MetricKit  
**Kind**: property

The version of the OS on the device including the type of OS, version number, and build number.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var osVersion: String { get }
```

#### Discussion

The OS version is the same as the one used in crash reports.

## See Also

- [var applicationBuildVersion: String](mxmetadata/applicationbuildversion.md)
  The value of the bundle version key in the app’s property list.
- [var deviceType: String](mxmetadata/devicetype.md)
  The hardware identifier for the device.
- [var isTestFlightApp: Bool](mxmetadata/istestflightapp.md)
  Indicates whether the app is registered with TestFlight.
- [var lowPowerModeEnabled: Bool](mxmetadata/lowpowermodeenabled.md)
  Indicates whether low power mode is enabled on the device.
- [var platformArchitecture: String](mxmetadata/platformarchitecture.md)
  The name of the processor architecture for the device.
- [var regionFormat: String](mxmetadata/regionformat.md)
  The short country code for the region format setting of the device.
- [var pid: pid_t](mxmetadata/pid.md)
  The process ID (PID) of the process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetadata/osversion)*