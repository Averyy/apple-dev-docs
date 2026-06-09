# MetricManager.LaunchTaskError.Reason.duplicateTask

**Framework**: MetricKit  
**Kind**: case

A task with the same ID has already been started.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
case duplicateTask
```

## See Also

- [MetricManager.LaunchTaskError.Reason.invalidID](metricmanager/launchtaskerror/reason-swift.enum/invalidid.md)
  The task ID is a null value or exceeds the maximum 128 character length.
- [MetricManager.LaunchTaskError.Reason.maxCountExceeded](metricmanager/launchtaskerror/reason-swift.enum/maxcountexceeded.md)
  Exceeded the maximum number of tasks.
- [MetricManager.LaunchTaskError.Reason.pastDeadline](metricmanager/launchtaskerror/reason-swift.enum/pastdeadline.md)
  The start call was made too late.
- [MetricManager.LaunchTaskError.Reason.taskUnknown](metricmanager/launchtaskerror/reason-swift.enum/taskunknown.md)
  The task hasn’t been started or has already been finished.
- [MetricManager.LaunchTaskError.Reason.internalFailure](metricmanager/launchtaskerror/reason-swift.enum/internalfailure.md)
  Internal failures happened inside the framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/metricmanager/launchtaskerror/reason-swift.enum/duplicatetask)*