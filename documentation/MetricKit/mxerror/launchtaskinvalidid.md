# launchTaskInvalidID

**Framework**: MetricKit  
**Kind**: property  
**Role**: Type Property

The task ID is a `null` value or exceeds the maximum 128 character length.

**Availability**:
- iOS 16.0+ - Deprecated in 27.2
- iPadOS 16.0+ - Deprecated in 27.2
- Mac Catalyst 16.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`MetricManager.LaunchTaskError.Reason.invalidID`](../metricmanager/launchtaskerror/reason-swift.enum/invalidid.md) instead.

## Declaration

```swift
static var launchTaskInvalidID: MXError.Code { get }
```

## See Also

### Getting the launch error properties
- [static var errorDomain: String](./errordomain.md)
- [static var launchTaskDuplicated: MXError.Code](./launchtaskduplicated.md)
  A task with the same ID has already been started.
- [static var launchTaskInternalFailure: MXError.Code](./launchtaskinternalfailure.md)
  Internal failures happened inside the framework.
- [static var launchTaskMaxCount: MXError.Code](./launchtaskmaxcount.md)
  Exceeded the maximum number of tasks.
- [static var launchTaskPastDeadline: MXError.Code](./launchtaskpastdeadline.md)
  The start call was made too late.
- [static var launchTaskUnknown: MXError.Code](./launchtaskunknown.md)
  The task hasn’t been started or has already been finished.
- [MXError.Code](./code.md)
  Error codes for error values from app metrics.
- [let MXErrorDomain: String](../mxerrordomain.md)
  Error domain for error values from app metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxerror/launchtaskinvalidid)*