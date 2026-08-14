# MXDiagnostic

**Framework**: MetricKit  
**Kind**: class

An abstract data class for a diagnostic.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MXDiagnostic
```

## Topics

### Reading data About a diagnostic
- [var applicationVersion: String](mxdiagnostic/applicationversion.md)
  The value of the bundle version key, short form, in the app’s property list.
- [var metaData: MXMetaData](mxdiagnostic/metadata.md)
  A set of system-level information for the device.
- [var signpostData: [MXSignpostRecord]?](mxdiagnostic/signpostdata.md)
### Generating a report
- [func jsonRepresentation() -> Data](mxdiagnostic/jsonrepresentation.md)
  Returns the contents of the diagnostic in JSON format.
- [func dictionaryRepresentation() -> [AnyHashable : Any]](mxdiagnostic/dictionaryrepresentation.md)
  Returns the contents of a diagnostic as a dictionary.
### Initializers
- [init?(coder: NSCoder)](mxdiagnostic/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Inherited By
- [MXAppLaunchDiagnostic](mxapplaunchdiagnostic.md)
- [MXCPUExceptionDiagnostic](mxcpuexceptiondiagnostic.md)
- [MXCrashDiagnostic](mxcrashdiagnostic.md)
- [MXDiskWriteExceptionDiagnostic](mxdiskwriteexceptiondiagnostic.md)
- [MXHangDiagnostic](mxhangdiagnostic.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class MXCallStackTree](mxcallstacktree.md)
  An object representing the call stack for an exception.
- [class MXMetaData](mxmetadata.md)
  An object containing system-level information about the device.
- [class MXAverage](mxaverage.md)
  A unit of measure for an average.
- [class MXHistogram](mxhistogram.md)
  An object representing a histogram of data values of the same type of unit.
- [class MXHistogramBucket](mxhistogrambucket.md)
  An object representing a bucket of data in a histogram.
- [class MXMetric](mxmetric.md)
  An abstract data class for a metric.
- [struct MXError](mxerror.md)
  Error domain for error handling of app metrics.
- [MXError.Code](mxerror/code.md)
  Error codes for error values from app metrics.
- [let MXErrorDomain: String](mxerrordomain.md)
  Error domain for error values from app metrics.
- [class MXCrashDiagnosticObjectiveCExceptionReason](mxcrashdiagnosticobjectivecexceptionreason.md)
  An object that represents the exception reason for an uncaught ObjC exception.
- [class MXSignpostRecord](mxsignpostrecord.md)
  An object representing the record for a signpost interval or event.
- [class MXUnitAveragePixelLuminance](mxunitaveragepixelluminance.md)
  A unit of measure of pixel luminosity on an OLED display.
- [class MXUnitSignalBars](mxunitsignalbars.md)
  A unit of measure for the number of bars of cellular network connectivity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxdiagnostic)*