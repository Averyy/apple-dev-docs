# MXError.Code

**Framework**: MetricKit  
**Kind**: enum

Error codes for error values from app metrics.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
enum Code
```

## Topics

### Launch errors
- [MXError.Code.launchTaskDuplicated](mxerror/code/launchtaskduplicated.md)
  A task with the same ID has already been started.
- [MXError.Code.launchTaskInternalFailure](mxerror/code/launchtaskinternalfailure.md)
  Internal failures happened inside the framework.
- [MXError.Code.launchTaskInvalidID](mxerror/code/launchtaskinvalidid.md)
  The task ID is a `null` value or exceeds the maximum 128 character length.
- [MXError.Code.launchTaskMaxCount](mxerror/code/launchtaskmaxcount.md)
  Exceeded the maximum number of tasks.
- [MXError.Code.launchTaskPastDeadline](mxerror/code/launchtaskpastdeadline.md)
  The start call was made too late.
- [MXError.Code.launchTaskUnknown](mxerror/code/launchtaskunknown.md)
  The task hasn’t been started or has already been finished.
### Initializers
- [init?(rawValue: Int)](mxerror/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [let MXErrorDomain: String](mxerrordomain.md)
  Error domain for error values from app metrics.
- [struct MXError](mxerror.md)
  Error domain for error handling of app metrics.
- [class MXCrashDiagnosticObjectiveCExceptionReason](mxcrashdiagnosticobjectivecexceptionreason.md)
  An object that represents the exception reason for an uncaught ObjC exception.
- [class MXSignpostRecord](mxsignpostrecord.md)
  An object representing the record for a signpost interval or event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxerror/code)*