# MXError.Code.launchTaskUnknown

**Framework**: MetricKit  
**Kind**: case

The task hasn’t been started or has already been finished.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
case launchTaskUnknown
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxerror/code/launchtaskunknown)*