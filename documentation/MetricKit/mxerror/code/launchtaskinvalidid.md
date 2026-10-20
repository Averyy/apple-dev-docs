# MXError.Code.launchTaskInvalidID

**Framework**: MetricKit  
**Kind**: case  
**Role**: Case

The task ID is a `null` value or exceeds the maximum 128 character length.

**Availability**:
- iOS 16.0+ - Deprecated in 27.2
- iPadOS 16.0+ - Deprecated in 27.2
- Mac Catalyst 16.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`MetricManager.LaunchTaskError.Reason.invalidID`](../../metricmanager/launchtaskerror/reason-swift.enum/invalidid.md) instead.

## Declaration

```swift
case launchTaskInvalidID
```

```c
MXErrorLaunchTaskInvalidID
```

## See Also

### Launch errors
- [MXError.Code.launchTaskDuplicated](./launchtaskduplicated.md)
  A task with the same ID has already been started.
- [MXError.Code.launchTaskInternalFailure](./launchtaskinternalfailure.md)
  Internal failures happened inside the framework.
- [MXError.Code.launchTaskMaxCount](./launchtaskmaxcount.md)
  Exceeded the maximum number of tasks.
- [MXError.Code.launchTaskPastDeadline](./launchtaskpastdeadline.md)
  The start call was made too late.
- [MXError.Code.launchTaskUnknown](./launchtaskunknown.md)
  The task hasn’t been started or has already been finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxerror/code/launchtaskinvalidid)*