# trackLaunchTask(id:onTrackingError:_:)

**Framework**: MetricKit  
**Kind**: method

Measures the duration of a synchronous extended launch task.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
final func trackLaunchTask<Result, Failure>(id: LaunchTaskID, onTrackingError: ((MetricManager.LaunchTaskError) -> Void)? = nil, _ operation: () throws(Failure) -> Result) throws(Failure) -> Result where Failure : Error
```

#### Discussion

Use this method to wrap synchronous work that extends your app’s perceived launch time. Pass a [`LaunchTaskID`](launchtaskid.md) and a synchronous closure wrapping the work to measure. Measurement begins when the closure starts and ends it when the closure returns, regardless of whether the closure throws.

```swift
manager.trackLaunchTask(id: "register-services") {
    registerAllServices()
}
```

Pass an `onTrackingError` closure to observe [`MetricManager.LaunchTaskError`](metricmanager/launchtaskerror.md) values without interrupting the tracked work:

```swift
manager.trackLaunchTask(id: "register-services", onTrackingError: { error in
    logger.warning("Tracking error: \(error.reason)")
}) {
    registerAllServices()
}
```

To track asynchronous launch work instead, use [`trackLaunchTask(id:onTrackingError:_:)`](metricmanager/tracklaunchtask(id:ontrackingerror:_:)-48k2s.md).

## See Also

- [func trackLaunchTask<Result, Failure>(id: LaunchTaskID, onTrackingError: ((MetricManager.LaunchTaskError) -> Void)?, () async throws(Failure) -> Result) async throws(Failure) -> Result](metricmanager/tracklaunchtask(id:ontrackingerror:_:)-48k2s.md)
  Measures the duration of an asynchronous extended launch task.
- [MetricManager.LaunchTaskError](metricmanager/launchtaskerror.md)
  An error that describes a problem that occurred while tracking an extended launch task.
- [struct LaunchTaskID](launchtaskid.md)
  An identifier for a task measured as part of an extended app launch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/metricmanager/tracklaunchtask(id:ontrackingerror:_:)-jnu1)*