# MetricManager.LaunchTaskError

**Framework**: MetricKit  
**Kind**: struct

An error that describes a problem that occurred while tracking an extended launch task.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
struct LaunchTaskError
```

## Mentions

- [Monitoring app performance with MetricKit](monitoring-app-performance-with-metrickit.md)

#### Discussion

`LaunchTaskError` is delivered to the `onTrackingError` closure passed to [`trackLaunchTask(id:onTrackingError:_:)`](metricmanager/tracklaunchtask(id:ontrackingerror:_:)-48k2s.md) or [`trackLaunchTask(id:onTrackingError:_:)`](metricmanager/tracklaunchtask(id:ontrackingerror:_:)-jnu1.md). Inspect [`reason`](metricmanager/launchtaskerror/reason-swift.property.md) to determine the cause:

```swift
await manager.trackLaunchTask(id: "initial-data-load", onTrackingError: { error in
    print("Tracking error for \(error.taskID): \(error.reason)")
}) {
    await loadInitialData()
}
```

## Topics

### Error details
- [let taskID: LaunchTaskID](metricmanager/launchtaskerror/taskid.md)
  The task ID that caused the error
- [let reason: MetricManager.LaunchTaskError.Reason](metricmanager/launchtaskerror/reason-swift.property.md)
  The reason for the error
- [MetricManager.LaunchTaskError.Reason](metricmanager/launchtaskerror/reason-swift.enum.md)
  A value that describes why a launch task tracking operation failed.

## Relationships

### Conforms To
- [Error](../swift/error.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func trackLaunchTask<Result, Failure>(id: LaunchTaskID, onTrackingError: ((MetricManager.LaunchTaskError) -> Void)?, () async throws(Failure) -> Result) async throws(Failure) -> Result](metricmanager/tracklaunchtask(id:ontrackingerror:_:)-48k2s.md)
  Measures the duration of an asynchronous extended launch task.
- [func trackLaunchTask<Result, Failure>(id: LaunchTaskID, onTrackingError: ((MetricManager.LaunchTaskError) -> Void)?, () throws(Failure) -> Result) throws(Failure) -> Result](metricmanager/tracklaunchtask(id:ontrackingerror:_:)-jnu1.md)
  Measures the duration of a synchronous extended launch task.
- [struct LaunchTaskID](launchtaskid.md)
  An identifier for a task measured as part of an extended app launch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/metricmanager/launchtaskerror)*