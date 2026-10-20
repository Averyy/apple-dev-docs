# MXCallStackTree

**Framework**: MetricKit  
**Kind**: class  
**Role**: Class

An object representing the call stack for an exception.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`CallStackTree`](./callstacktree.md) instead.

## Declaration

```swift
class MXCallStackTree
```

```objc
@interface MXCallStackTree : NSObject
```

## Topics

### Generating a report
- [func jsonRepresentation() -> Data](./mxcallstacktree/jsonrepresentation%28%29.md)
  Returns the contents of the stack tree in JSON format.
### Initializers
- [init?(coder: NSCoder)](./mxcallstacktree/init%28coder%29.md)

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
- [class MXCrashDiagnosticObjectiveCExceptionReason](./mxcrashdiagnosticobjectivecexceptionreason.md)
  An object that represents the exception reason for an uncaught ObjC exception.
- [class MXSignpostRecord](./mxsignpostrecord.md)
  An object representing the record for a signpost interval or event.
- [class MXUnitAveragePixelLuminance](./mxunitaveragepixelluminance.md)
  A unit of measure of pixel luminosity on an OLED display.
- [class MXUnitSignalBars](./mxunitsignalbars.md)
  A unit of measure for the number of bars of cellular network connectivity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxcallstacktree)*