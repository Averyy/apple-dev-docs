# MXCrashDiagnosticObjectiveCExceptionReason

**Framework**: MetricKit  
**Kind**: class  
**Role**: Class

An object that represents the exception reason for an uncaught ObjC exception.

**Availability**:
- iOS 17.0+ - Deprecated in 27.2
- iPadOS 17.0+ - Deprecated in 27.2
- Mac Catalyst 17.0+ - Deprecated in 27.0
- macOS 14.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`CrashDiagnostic.ObjectiveCExceptionReason`](./crashdiagnostic/objectivecexceptionreason.md) instead.

## Declaration

```swift
class MXCrashDiagnosticObjectiveCExceptionReason
```

```objc
@interface MXCrashDiagnosticObjectiveCExceptionReason : NSObject
```

#### Overview

The crash report for an uncaught Objective-C [`NSException`](../Foundation/nsexception.md) can contain detailed information about the type, name and description of the exception object. Use the properties and methods on [`MXCrashDiagnosticObjectiveCExceptionReason`](./mxcrashdiagnosticobjectivecexceptionreason.md) to access this information.

## Topics

### Generating a report
- [func dictionaryRepresentation() -> [AnyHashable : Any]](./mxcrashdiagnosticobjectivecexceptionreason/dictionaryrepresentation%28%29.md)
- [func jsonRepresentation() -> Data](./mxcrashdiagnosticobjectivecexceptionreason/jsonrepresentation%28%29.md)
  Returns the contents of the exception reason in JSON format.
### Reading the data
- [var arguments: [String]](./mxcrashdiagnosticobjectivecexceptionreason/arguments.md)
- [var className: String](./mxcrashdiagnosticobjectivecexceptionreason/classname.md)
- [var composedMessage: String](./mxcrashdiagnosticobjectivecexceptionreason/composedmessage.md)
- [var exceptionName: String](./mxcrashdiagnosticobjectivecexceptionreason/exceptionname.md)
- [var exceptionType: String](./mxcrashdiagnosticobjectivecexceptionreason/exceptiontype.md)
- [var formatString: String](./mxcrashdiagnosticobjectivecexceptionreason/formatstring.md)
### Initializers
- [init?(coder: NSCoder)](./mxcrashdiagnosticobjectivecexceptionreason/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Supporting types
- [class MXCallStackTree](./mxcallstacktree.md)
  An object representing the call stack for an exception.
- [class MXMetaData](./mxmetadata.md)
  An object containing system-level information about the device.
- [class MXAverage](./mxaverage.md)
  A unit of measure for an average.
- [class MXHistogram](./mxhistogram.md)
  An object representing a histogram of data values of the same type of unit.
- [class MXHistogramBucket](./mxhistogrambucket.md)
  An object representing a bucket of data in a histogram.
- [class MXDiagnostic](./mxdiagnostic.md)
  An abstract data class for a diagnostic.
- [class MXMetric](./mxmetric.md)
  An abstract data class for a metric.
- [struct MXError](./mxerror.md)
  Error domain for error handling of app metrics.
- [MXError.Code](./mxerror/code.md)
  Error codes for error values from app metrics.
- [let MXErrorDomain: String](./mxerrordomain.md)
  Error domain for error values from app metrics.
- [class MXSignpostRecord](./mxsignpostrecord.md)
  An object representing the record for a signpost interval or event.
- [class MXUnitAveragePixelLuminance](./mxunitaveragepixelluminance.md)
  A unit of measure of pixel luminosity on an OLED display.
- [class MXUnitSignalBars](./mxunitsignalbars.md)
  A unit of measure for the number of bars of cellular network connectivity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxcrashdiagnosticobjectivecexceptionreason)*