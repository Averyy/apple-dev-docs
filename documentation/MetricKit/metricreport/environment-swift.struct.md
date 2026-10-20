# MetricReport.Environment

**Framework**: MetricKit  
**Kind**: struct  
**Role**: Structure

Device and app metadata associated with a metric report.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
struct Environment
```

## Mentions

- [Analyzing app performance with MetricKit](../analyzing-app-performance-with-metrickit.md)

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
- [let latestApplicationVersion: String](./environment-swift.struct/latestapplicationversion.md)
  The version of the app on the device at the end of the reporting period.
- [let includesMultipleApplicationVersions: Bool](./environment-swift.struct/includesmultipleapplicationversions.md)
  A Boolean indicating if the version of the app changed at least once during the reporting period.
- [let isTestFlightApp: Bool](./environment-swift.struct/istestflightapp.md)
  Indicates whether the app is registered with TestFlight.
### System state
- [let lowPowerModeEnabled: Bool](./environment-swift.struct/lowpowermodeenabled.md)
  Indicates whether low power mode is enabled on the device.
- [let hasExceededStateLimit: Bool](./environment-swift.struct/hasexceededstatelimit.md)
  A Boolean indicating if the number of emitted states exceeded the aggregation limit.
### Instance Properties
- [let applicationBuildVersion: String](./environment-swift.struct/applicationbuildversion.md)
  The value of the bundle version key in the app’s property list.
- [let bundleIdentifier: String](./environment-swift.struct/bundleidentifier.md)
  String representation of the bundle ID of the process.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/metricreport/environment-swift.struct)*