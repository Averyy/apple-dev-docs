# launchTaskInternalFailure

**Framework**: MetricKit  
**Kind**: property

Internal failures happened inside the framework.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
static var launchTaskInternalFailure: MXError.Code { get }
```

## See Also

- [static var launchTaskDuplicated: MXError.Code](mxerror/launchtaskduplicated.md)
  A task with the same ID has already been started.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxerror/launchtaskinternalfailure)*