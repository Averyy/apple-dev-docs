# MXError.Code

**Framework**: MetricKit  
**Kind**: enum  
**Role**: Enumeration

Error codes for error values from app metrics.

**Availability**:
- iOS 16.0+ - Deprecated in 27.2
- iPadOS 16.0+ - Deprecated in 27.2
- Mac Catalyst 16.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`MetricManager.LaunchTaskError`](../metricmanager/launchtaskerror.md) instead.

## Declaration

```swift
enum Code
```

```c
enum MXErrorCode : NSInteger;
```

## Topics

### Launch errors
- [MXError.Code.launchTaskDuplicated](./code/launchtaskduplicated.md)
  A task with the same ID has already been started.
- [MXError.Code.launchTaskInternalFailure](./code/launchtaskinternalfailure.md)
  Internal failures happened inside the framework.
- [MXError.Code.launchTaskInvalidID](./code/launchtaskinvalidid.md)
  The task ID is a `null` value or exceeds the maximum 128 character length.
- [MXError.Code.launchTaskMaxCount](./code/launchtaskmaxcount.md)
  Exceeded the maximum number of tasks.
- [MXError.Code.launchTaskPastDeadline](./code/launchtaskpastdeadline.md)
  The start call was made too late.
- [MXError.Code.launchTaskUnknown](./code/launchtaskunknown.md)
  The task hasn’t been started or has already been finished.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Supporting types
- [class MXCallStackTree](../mxcallstacktree.md)
  An object representing the call stack for an exception.
- [class MXMetaData](../mxmetadata.md)
  An object containing system-level information about the device.
- [class MXAverage](../mxaverage.md)
  A unit of measure for an average.
- [class MXHistogram](../mxhistogram.md)
  An object representing a histogram of data values of the same type of unit.
- [class MXHistogramBucket](../mxhistogrambucket.md)
  An object representing a bucket of data in a histogram.
- [class MXDiagnostic](../mxdiagnostic.md)
  An abstract data class for a diagnostic.
- [class MXMetric](../mxmetric.md)
  An abstract data class for a metric.
- [struct MXError](../mxerror.md)
  Error domain for error handling of app metrics.
- [let MXErrorDomain: String](../mxerrordomain.md)
  Error domain for error values from app metrics.
- [class MXCrashDiagnosticObjectiveCExceptionReason](../mxcrashdiagnosticobjectivecexceptionreason.md)
  An object that represents the exception reason for an uncaught ObjC exception.
- [class MXSignpostRecord](../mxsignpostrecord.md)
  An object representing the record for a signpost interval or event.
- [class MXUnitAveragePixelLuminance](../mxunitaveragepixelluminance.md)
  A unit of measure of pixel luminosity on an OLED display.
- [class MXUnitSignalBars](../mxunitsignalbars.md)
  A unit of measure for the number of bars of cellular network connectivity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxerror/code)*