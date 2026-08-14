# MXCrashDiagnosticObjectiveCExceptionReason

**Framework**: MetricKit  
**Kind**: class

An object that represents the exception reason for an uncaught ObjC exception.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class MXCrashDiagnosticObjectiveCExceptionReason
```

#### Overview

The crash report for an uncaught Objective-C [`NSException`](https://developer.apple.com/documentation/foundation/nsexception) can contain detailed information about the type, name and description of the exception object. Use the properties and methods on [`MXCrashDiagnosticObjectiveCExceptionReason`](mxcrashdiagnosticobjectivecexceptionreason.md) to access this information.

## Topics

### Generating a report
- [func dictionaryRepresentation() -> [AnyHashable : Any]](mxcrashdiagnosticobjectivecexceptionreason/dictionaryrepresentation.md)
- [func jsonRepresentation() -> Data](mxcrashdiagnosticobjectivecexceptionreason/jsonrepresentation.md)
  Returns the contents of the exception reason in JSON format.
### Reading the data
- [var arguments: [String]](mxcrashdiagnosticobjectivecexceptionreason/arguments.md)
- [var className: String](mxcrashdiagnosticobjectivecexceptionreason/classname.md)
- [var composedMessage: String](mxcrashdiagnosticobjectivecexceptionreason/composedmessage.md)
- [var exceptionName: String](mxcrashdiagnosticobjectivecexceptionreason/exceptionname.md)
- [var exceptionType: String](mxcrashdiagnosticobjectivecexceptionreason/exceptiontype.md)
- [var formatString: String](mxcrashdiagnosticobjectivecexceptionreason/formatstring.md)
### Initializers
- [init?(coder: NSCoder)](mxcrashdiagnosticobjectivecexceptionreason/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
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
- [class MXDiagnostic](mxdiagnostic.md)
  An abstract data class for a diagnostic.
- [class MXMetric](mxmetric.md)
  An abstract data class for a metric.
- [struct MXError](mxerror.md)
  Error domain for error handling of app metrics.
- [MXError.Code](mxerror/code.md)
  Error codes for error values from app metrics.
- [let MXErrorDomain: String](mxerrordomain.md)
  Error domain for error values from app metrics.
- [class MXSignpostRecord](mxsignpostrecord.md)
  An object representing the record for a signpost interval or event.
- [class MXUnitAveragePixelLuminance](mxunitaveragepixelluminance.md)
  A unit of measure of pixel luminosity on an OLED display.
- [class MXUnitSignalBars](mxunitsignalbars.md)
  A unit of measure for the number of bars of cellular network connectivity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxcrashdiagnosticobjectivecexceptionreason)*