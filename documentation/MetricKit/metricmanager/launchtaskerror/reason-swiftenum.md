# MetricManager.LaunchTaskError.Reason

**Framework**: MetricKit  
**Kind**: enum

A value that describes why a launch task tracking operation failed.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
enum Reason
```

## Topics

### Error reasons
- [MetricManager.LaunchTaskError.Reason.invalidID](metricmanager/launchtaskerror/reason-swift.enum/invalidid.md)
  The task ID is a null value or exceeds the maximum 128 character length.
- [MetricManager.LaunchTaskError.Reason.maxCountExceeded](metricmanager/launchtaskerror/reason-swift.enum/maxcountexceeded.md)
  Exceeded the maximum number of tasks.
- [MetricManager.LaunchTaskError.Reason.pastDeadline](metricmanager/launchtaskerror/reason-swift.enum/pastdeadline.md)
  The start call was made too late.
- [MetricManager.LaunchTaskError.Reason.duplicateTask](metricmanager/launchtaskerror/reason-swift.enum/duplicatetask.md)
  A task with the same ID has already been started.
- [MetricManager.LaunchTaskError.Reason.taskUnknown](metricmanager/launchtaskerror/reason-swift.enum/taskunknown.md)
  The task hasn’t been started or has already been finished.
- [MetricManager.LaunchTaskError.Reason.internalFailure](metricmanager/launchtaskerror/reason-swift.enum/internalfailure.md)
  Internal failures happened inside the framework.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [let taskID: LaunchTaskID](metricmanager/launchtaskerror/taskid.md)
  The task ID that caused the error
- [let reason: MetricManager.LaunchTaskError.Reason](metricmanager/launchtaskerror/reason-swift.property.md)
  The reason for the error


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/metricmanager/launchtaskerror/reason-swift.enum)*