# MXError.Code.launchTaskUnknown

**Framework**: MetricKit  
**Kind**: case  
**Role**: Case

The task hasn’t been started or has already been finished.

**Availability**:
- iOS 16.0+ - Deprecated in 27.2
- iPadOS 16.0+ - Deprecated in 27.2
- Mac Catalyst 16.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`MetricManager.LaunchTaskError.Reason.taskUnknown`](../../metricmanager/launchtaskerror/reason-swift.enum/taskunknown.md) instead.

## Declaration

```swift
case launchTaskUnknown
```

```c
MXErrorLaunchTaskUnknown
```

## See Also

### Launch errors
- [MXError.Code.launchTaskDuplicated](./launchtaskduplicated.md)
  A task with the same ID has already been started.
- [MXError.Code.launchTaskInternalFailure](./launchtaskinternalfailure.md)
  Internal failures happened inside the framework.
- [MXError.Code.launchTaskInvalidID](./launchtaskinvalidid.md)
  The task ID is a `null` value or exceeds the maximum 128 character length.
- [MXError.Code.launchTaskMaxCount](./launchtaskmaxcount.md)
  Exceeded the maximum number of tasks.
- [MXError.Code.launchTaskPastDeadline](./launchtaskpastdeadline.md)
  The start call was made too late.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxerror/code/launchtaskunknown)*