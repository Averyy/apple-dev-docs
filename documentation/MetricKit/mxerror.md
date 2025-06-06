# MXError

**Framework**: MetricKit  
**Kind**: struct

Error domain for error handling of app metrics.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
struct MXError
```

## Topics

### Getting the error properties
- [MXError.Code](mxerror/code.md)
  Error codes for error values from app metrics.
- [let MXErrorDomain: String](mxerrordomain.md)
  Error domain for error values from app metrics.
### Getting the launch error properties
- [static var launchTaskDuplicated: MXError.Code](mxerror/launchtaskduplicated.md)
  A task with the same ID has already been started.
- [static var launchTaskInternalFailure: MXError.Code](mxerror/launchtaskinternalfailure.md)
  Internal failures happened inside the framework.
- [static var launchTaskInvalidID: MXError.Code](mxerror/launchtaskinvalidid.md)
  The task ID is a `null` value or exceeds the maximum 128 character length.
- [static var launchTaskMaxCount: MXError.Code](mxerror/launchtaskmaxcount.md)
  Exceeded the maximum number of tasks.
- [static var launchTaskPastDeadline: MXError.Code](mxerror/launchtaskpastdeadline.md)
  The start call was made too late.
- [static var launchTaskUnknown: MXError.Code](mxerror/launchtaskunknown.md)
  The task hasn’t been started or has already been finished.
- [MXError.Code](mxerror/code.md)
  Error codes for error values from app metrics.
- [let MXErrorDomain: String](mxerrordomain.md)
  Error domain for error values from app metrics.
### Type Properties
- [static var errorDomain: String](mxerror/errordomain.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class MXCallStackTree](mxcallstacktree.md)
  An object representing the call stack for an exception.
- [class MXMetaData](mxmetadata.md)
  An object containing system-level information about the device.
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
- [class MXCrashDiagnosticObjectiveCExceptionReason](mxcrashdiagnosticobjectivecexceptionreason.md)
  An object that represents the exception reason for an uncaught ObjC exception.
- [class MXSignpostRecord](mxsignpostrecord.md)
  An object representing the record for a signpost interval or event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxerror)*