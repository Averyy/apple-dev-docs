# DiagnosticReport.Environment

**Framework**: MetricKit  
**Kind**: struct

Device, app, and state metadata associated with a diagnostic report.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Environment
```

## Mentions

- [Analyzing app performance with MetricKit](analyzing-app-performance-with-metrickit.md)
- [Monitoring app performance with MetricKit](monitoring-app-performance-with-metrickit.md)

#### Discussion

`DiagnosticReport.Environment` carries device and app context alongside state and signpost data captured around the time of the diagnostic event.

Access the app states that were active when the event occurred through [`states`](diagnosticreport/environment-swift.struct/states.md). Use [`signpostData`](diagnosticreport/environment-swift.struct/signpostdata.md) to correlate signpost events with the diagnostic:

```swift
for await report in manager.diagnosticReports {
    let environment = report.environment
    print(environment.osVersion, environment.applicationVersion)

    for state in environment.states {
        print(state.domain, state.label)
    }
}
```

## Topics

### Device information
- [let deviceType: String](diagnosticreport/environment-swift.struct/devicetype.md)
  The hardware identifier for the device.
- [let osVersion: OSVersion](diagnosticreport/environment-swift.struct/osversion.md)
  The version of the OS on the device including the type of OS, version number, and build number.
- [let platformArchitecture: String](diagnosticreport/environment-swift.struct/platformarchitecture.md)
  The name of the processor architecture for the device.
- [let regionFormat: String](diagnosticreport/environment-swift.struct/regionformat.md)
  The short country code for the region format setting of the device.
### App information
- [let applicationVersion: String](diagnosticreport/environment-swift.struct/applicationversion.md)
  The value of the bundle version key, short form, in the app’s property list.
- [let isTestFlightApp: Bool](diagnosticreport/environment-swift.struct/istestflightapp.md)
  Indicates whether the app is registered with TestFlight.
### System state
- [let lowPowerModeEnabled: Bool](diagnosticreport/environment-swift.struct/lowpowermodeenabled.md)
  Indicates whether low power mode is enabled on the device.
### State reporting context
- [let states: [MetricManager.ReportedState]](diagnosticreport/environment-swift.struct/states.md)
  All states that were active leading up to this diagnostic event.
### Signpost data
- [let signpostData: [SignpostRecord]](diagnosticreport/environment-swift.struct/signpostdata.md)
  Signpost data associated with the diagnostic.
### Instance Properties
- [let applicationBuildVersion: String](diagnosticreport/environment-swift.struct/applicationbuildversion.md)
  The value of the bundle version key in the app’s property list.
- [let bundleIdentifier: String](diagnosticreport/environment-swift.struct/bundleidentifier.md)
  String representation of the bundle ID of the process.
- [let pid: pid_t?](diagnosticreport/environment-swift.struct/pid.md)
  The process ID (PID) of the process.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/diagnosticreport/environment-swift.struct)*