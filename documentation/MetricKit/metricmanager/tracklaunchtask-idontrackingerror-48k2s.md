# trackLaunchTask(id:onTrackingError:_:)

**Framework**: MetricKit  
**Kind**: method

Measures the duration of an asynchronous extended launch task.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
final func trackLaunchTask<Result, Failure>(id: LaunchTaskID, onTrackingError: ((MetricManager.LaunchTaskError) -> Void)? = nil, _ operation: () async throws(Failure) -> Result) async throws(Failure) -> Result where Failure : Error
```

## Mentions

- [Monitoring app performance with MetricKit](monitoring-app-performance-with-metrickit.md)

#### Discussion

Use this method to wrap asynchronous work that extends your app’s perceived launch time, such as fetching configuration data, loading initial content, or initializing a local database. Pass a [`LaunchTaskID`](launchtaskid.md) and an `async` closure wrapping the work to measure. Measurement begins when the closure starts and ends it when the closure returns,  regardless of whether the closure throws.

```swift
await manager.trackLaunchTask(id: "initial-data-load") {
    await loadInitialData()
}
```

Pass an `onTrackingError` closure to observe [`MetricManager.LaunchTaskError`](metricmanager/launchtaskerror.md) values without interrupting the tracked work:

```swift
await manager.trackLaunchTask(id: "initial-data-load", onTrackingError: { error in
    logger.warning("Tracking error: \(error.reason)")
}) {
    await loadInitialData()
}
```

This method replaces the paired `MXMetricManager.extendLaunchMeasurement(forTaskID:)` and `MXMetricManager.finishExtendedLaunchMeasurement(forTaskID:)` calls. To track synchronous launch work instead, use [`trackLaunchTask(id:onTrackingError:_:)`](metricmanager/tracklaunchtask(id:ontrackingerror:_:)-jnu1.md).

## See Also

- [func trackLaunchTask<Result, Failure>(id: LaunchTaskID, onTrackingError: ((MetricManager.LaunchTaskError) -> Void)?, () throws(Failure) -> Result) throws(Failure) -> Result](metricmanager/tracklaunchtask(id:ontrackingerror:_:)-jnu1.md)
  Measures the duration of a synchronous extended launch task.
- [MetricManager.LaunchTaskError](metricmanager/launchtaskerror.md)
  An error that describes a problem that occurred while tracking an extended launch task.
- [struct LaunchTaskID](launchtaskid.md)
  An identifier for a task measured as part of an extended app launch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/metricmanager/tracklaunchtask(id:ontrackingerror:_:)-48k2s)*