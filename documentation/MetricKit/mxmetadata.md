# MXMetaData

**Framework**: MetricKit  
**Kind**: class

An object containing system-level information about the device.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MXMetaData
```

## Topics

### Reading data about a payload
- [var applicationBuildVersion: String](mxmetadata/applicationbuildversion.md)
  The value of the bundle version key in the app’s property list.
- [var deviceType: String](mxmetadata/devicetype.md)
  The hardware identifier for the device.
- [var isTestFlightApp: Bool](mxmetadata/istestflightapp.md)
  Indicates whether the app is registered with TestFlight.
- [var lowPowerModeEnabled: Bool](mxmetadata/lowpowermodeenabled.md)
  Indicates whether low power mode is enabled on the device.
- [var osVersion: String](mxmetadata/osversion.md)
  The version of the OS on the device including the type of OS, version number, and build number.
- [var platformArchitecture: String](mxmetadata/platformarchitecture.md)
  The name of the processor architecture for the device.
- [var regionFormat: String](mxmetadata/regionformat.md)
  The short country code for the region format setting of the device.
- [var pid: pid_t](mxmetadata/pid.md)
  The process ID (PID) of the process.
### Generating a report
- [func jsonRepresentation() -> Data](mxmetadata/jsonrepresentation.md)
  Returns the contents of the metadata in JSON format.
- [func dictionaryRepresentation() -> [AnyHashable : Any]](mxmetadata/dictionaryrepresentation.md)
  Returns the contents of the metadata as a dictionary.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class MXCallStackTree](mxcallstacktree.md)
  An object representing the call stack for an exception.
- [class MXAverage](mxaverage.md)
  A unit of measure for an average.
- [class MXHistogram](mxhistogram.md)
  An object representing a histogram of data values of the same type of unit.
- [class MXDiagnostic](mxdiagnostic.md)
  An abstract data class for a diagnostic.
- [class MXMetric](mxmetric.md)
  An abstract data class for a metric.
- [MXError.Code](mxerror/code.md)
  Error codes for error values from app metrics.
- [let MXErrorDomain: String](mxerrordomain.md)
  Error domain for error values from app metrics.
- [struct MXError](mxerror.md)
  Error domain for error handling of app metrics.
- [class MXCrashDiagnosticObjectiveCExceptionReason](mxcrashdiagnosticobjectivecexceptionreason.md)
  An object that represents the exception reason for an uncaught ObjC exception.
- [class MXSignpostRecord](mxsignpostrecord.md)
  An object representing the record for a signpost interval or event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetadata)*