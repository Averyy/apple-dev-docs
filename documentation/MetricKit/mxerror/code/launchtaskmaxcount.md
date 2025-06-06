# MXError.Code.launchTaskMaxCount

**Framework**: MetricKit  
**Kind**: case

Exceeded the maximum number of tasks.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
case launchTaskMaxCount
```

## See Also

- [MXError.Code.launchTaskDuplicated](mxerror/code/launchtaskduplicated.md)
  A task with the same ID has already been started.
- [MXError.Code.launchTaskInternalFailure](mxerror/code/launchtaskinternalfailure.md)
  Internal failures happened inside the framework.
- [MXError.Code.launchTaskInvalidID](mxerror/code/launchtaskinvalidid.md)
  The task ID is a `null` value or exceeds the maximum 128 character length.
- [MXError.Code.launchTaskPastDeadline](mxerror/code/launchtaskpastdeadline.md)
  The start call was made too late.
- [MXError.Code.launchTaskUnknown](mxerror/code/launchtaskunknown.md)
  The task hasn’t been started or has already been finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxerror/code/launchtaskmaxcount)*