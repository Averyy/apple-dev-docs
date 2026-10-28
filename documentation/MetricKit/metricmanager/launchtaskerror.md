# MetricManager.LaunchTaskError

**Framework**: MetricKit  
**Kind**: struct  
**Role**: Structure

An error that describes a problem that occurred while tracking an extended launch task.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
struct LaunchTaskError
```

## Mentions

- [Monitoring app performance with MetricKit](../monitoring-app-performance-with-metrickit.md)

## Discussion

`LaunchTaskError` is delivered to the `onTrackingError` closure passed to [`trackLaunchTask(id:onTrackingError:_:)`](./tracklaunchtask%28id,ontrackingerror,_%29-48k2s.md) or [`trackLaunchTask(id:onTrackingError:_:)`](./tracklaunchtask%28id,ontrackingerror,_%29-jnu1.md). Inspect [`reason`](./launchtaskerror/reason-swift.property.md) to determine the cause:

```swift
await manager.trackLaunchTask(id: "initial-data-load", onTrackingError: { error in
    print("Tracking error for \(error.taskID): \(error.reason)")
}) {
    await loadInitialData()
}
```

## Topics

### Error details
- [let taskID: LaunchTaskID](./launchtaskerror/taskid.md)
  The task ID that caused the error
- [let reason: MetricManager.LaunchTaskError.Reason](./launchtaskerror/reason-swift.property.md)
  The reason for the error
- [MetricManager.LaunchTaskError.Reason](./launchtaskerror/reason-swift.enum.md)
  A value that describes why a launch task tracking operation failed.

## Relationships

### Conforms To
- [Error](../../Swift/error.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Extended launch
- [func trackLaunchTask<Result, Failure>(id: LaunchTaskID, onTrackingError: ((MetricManager.LaunchTaskError) -> Void)?, () async throws(Failure) -> Result) async throws(Failure) -> Result](./tracklaunchtask%28id,ontrackingerror,_%29-48k2s.md)
  Measures the duration of an asynchronous extended launch task.
- [func trackLaunchTask<Result, Failure>(id: LaunchTaskID, onTrackingError: ((MetricManager.LaunchTaskError) -> Void)?, () throws(Failure) -> Result) throws(Failure) -> Result](./tracklaunchtask%28id,ontrackingerror,_%29-jnu1.md)
  Measures the duration of a synchronous extended launch task.
- [struct LaunchTaskID](../launchtaskid.md)
  An identifier for a task measured as part of an extended app launch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/metricmanager/launchtaskerror)*