# DiagnosticReport.Environment

**Framework**: MetricKit  
**Kind**: struct  
**Role**: Structure

Device, app, and state metadata associated with a diagnostic report.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Environment
```

## Mentions

- [Analyzing app performance with MetricKit](../analyzing-app-performance-with-metrickit.md)
- [Monitoring app performance with MetricKit](../monitoring-app-performance-with-metrickit.md)

## Discussion

`DiagnosticReport.Environment` carries device and app context alongside state and signpost data captured around the time of the diagnostic event.

Access the app states that were active when the event occurred through [`states`](./environment-swift.struct/states.md). Use [`signpostData`](./environment-swift.struct/signpostdata.md) to correlate signpost events with the diagnostic:

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
- [let deviceType: String](./environment-swift.struct/devicetype.md)
  The hardware identifier for the device.
- [let osVersion: OSVersion](./environment-swift.struct/osversion.md)
  The version of the OS on the device including the type of OS, version number, and build number.
- [let platformArchitecture: String](./environment-swift.struct/platformarchitecture.md)
  The name of the processor architecture for the device.
- [let regionFormat: String](./environment-swift.struct/regionformat.md)
  The short country code for the region format setting of the device.
### App information
- [let applicationVersion: String](./environment-swift.struct/applicationversion.md)
  The value of the bundle version key, short form, in the app’s property list.
- [let isTestFlightApp: Bool](./environment-swift.struct/istestflightapp.md)
  Indicates whether the app is registered with TestFlight.
### System state
- [let lowPowerModeEnabled: Bool](./environment-swift.struct/lowpowermodeenabled.md)
  Indicates whether low power mode is enabled on the device.
### State reporting context
- [let states: [MetricManager.ReportedState]](./environment-swift.struct/states.md)
  All states that were active leading up to this diagnostic event.
### Signpost data
- [let signpostData: [SignpostRecord]](./environment-swift.struct/signpostdata.md)
  Signpost data associated with the diagnostic.
### Instance Properties
- [let applicationBuildVersion: String](./environment-swift.struct/applicationbuildversion.md)
  The value of the bundle version key in the app’s property list.
- [let bundleIdentifier: String](./environment-swift.struct/bundleidentifier.md)
  String representation of the bundle ID of the process.
- [let pid: pid_t?](./environment-swift.struct/pid.md)
  The process ID (PID) of the process.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/diagnosticreport/environment-swift.struct)*