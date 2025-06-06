# beginBackgroundTask(withName:expirationHandler:)

**Framework**: UIKit  
**Kind**: method

Marks the start of a task with a custom name that should continue if the app enters the background.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func beginBackgroundTask(withName taskName: String?, expirationHandler handler: (@MainActor () -> Void)? = nil) -> UIBackgroundTaskIdentifier
```

## Mentions

- [Extending your app’s background execution time](extending-your-app-s-background-execution-time.md)

#### Return Value

A unique identifier for the new background task. You must pass this value to the [`endBackgroundTask(_:)`](uiapplication/endbackgroundtask(_:).md) method to mark the end of this task. This method returns [`invalid`](uibackgroundtaskidentifier/invalid.md) if running in the background isn’t possible.

#### Discussion

This method requests additional background execution time for your app. Call this method when leaving a task unfinished might be detrimental to your app’s user experience. For example, call this method before writing data to a file to prevent the system from suspending your app while the operation is in progress. For background tasks requiring more time, use [`Background Tasks`](https://developer.apple.com/documentation/BackgroundTasks).

Call this method as early as possible before starting your task, preferably before your app actually enters the background. The method requests the task assertion for your app asynchronously. If you call this method shortly before your app is due to be suspended, there’s a chance that the system might suspend your app before that task assertion is granted. For example, don’t call this method at the very end of your [`applicationDidEnterBackground(_:)`](uiapplicationdelegate/applicationdidenterbackground(_:).md) method and expect your app to continue running. If the system is unable to grant the task assertion, it calls your expiration handler.

Each call to this method must be balanced by a matching call to the [`endBackgroundTask(_:)`](uiapplication/endbackgroundtask(_:).md) method. Apps running background tasks have a finite amount of time in which to run them. (You can find out the maximum background time available using the [`backgroundTimeRemaining`](uiapplication/backgroundtimeremaining.md) property.) If you don’t call [`endBackgroundTask(_:)`](uiapplication/endbackgroundtask(_:).md) for each task before time expires, the system kills the app. If you provide a block object in the handler parameter, the system calls your handler before time expires to give you a chance to end the task.

You can call this method at any point in your app’s execution. You may also call this method multiple times to mark the beginning of several background tasks that run in parallel. However, each task must be ended separately. You identify a given task using the value returned by this method.

This method can be safely called on a non-main thread. To extend the execution time of an app extension, use the [`performExpiringActivity(withReason:using:)`](https://developer.apple.com/documentation/foundation/processinfo/1617030-performexpiringactivity) method of [`ProcessInfo`](https://developer.apple.com/documentation/Foundation/ProcessInfo) instead.

## Parameters

- `taskName`: The name to display in the debugger when viewing the background task. If you specify   for this parameter, the method generates a name based on the name of the calling function or method.
- `handler`: A handler to be called shortly before the app’s remaining background time reaches 0. Use this handler to clean up and mark the end of the background task. Failure to end the task explicitly will result in the termination of the app. The system calls the handler synchronously on the main thread, blocking the app’s suspension momentarily.

## See Also

- [Background Tasks](../BackgroundTasks/BackgroundTasks.md)
  Request the system to launch your app in the background to run tasks.
- [var backgroundRefreshStatus: UIBackgroundRefreshStatus](uiapplication/backgroundrefreshstatus.md)
  Indicates whether the app can refresh content when running in the background.
- [enum UIBackgroundRefreshStatus](uibackgroundrefreshstatus.md)
  Constants that indicate whether background execution is enabled for the app.
- [class let backgroundRefreshStatusDidChangeNotification: NSNotification.Name](uiapplication/backgroundrefreshstatusdidchangenotification.md)
  A notification that posts when the app’s status for downloading content in the background changes.
- [func beginBackgroundTask(expirationHandler: (() -> Void)?) -> UIBackgroundTaskIdentifier](uiapplication/beginbackgroundtask(expirationhandler:).md)
  Marks the start of a task that should continue if the app enters the background.
- [func endBackgroundTask(UIBackgroundTaskIdentifier)](uiapplication/endbackgroundtask(_:).md)
  Marks the end of a specific long-running background task.
- [struct UIBackgroundTaskIdentifier](uibackgroundtaskidentifier.md)
  A unique token that identifies a request to run in the background.
- [var backgroundTimeRemaining: TimeInterval](uiapplication/backgroundtimeremaining.md)
  The maximum amount of time remaining for the app to run in the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/beginbackgroundtask(withname:expirationhandler:))*