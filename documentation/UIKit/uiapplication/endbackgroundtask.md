# endBackgroundTask(_:)

**Framework**: UIKit  
**Kind**: method

Marks the end of a specific long-running background task.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func endBackgroundTask(_ identifier: UIBackgroundTaskIdentifier)
```

## Mentions

- [Extending your app’s background execution time](extending-your-app-s-background-execution-time.md)

#### Discussion

You must call this method to end a task that was started using the [`beginBackgroundTask(expirationHandler:)`](uiapplication/beginbackgroundtask(expirationhandler:).md) method. If you do not, the system may terminate your app.

This method can be safely called on a non-main thread.

## Parameters

- `identifier`: An identifier returned by the   method.

## See Also

- [var backgroundRefreshStatus: UIBackgroundRefreshStatus](uiapplication/backgroundrefreshstatus.md)
  Indicates whether the app can refresh content when running in the background.
- [enum UIBackgroundRefreshStatus](uibackgroundrefreshstatus.md)
  Constants that indicate whether background execution is enabled for the app.
- [class let backgroundRefreshStatusDidChangeNotification: NSNotification.Name](uiapplication/backgroundrefreshstatusdidchangenotification.md)
  A notification that posts when the app’s status for downloading content in the background changes.
- [func beginBackgroundTask(withName: String?, expirationHandler: (() -> Void)?) -> UIBackgroundTaskIdentifier](uiapplication/beginbackgroundtask(withname:expirationhandler:).md)
  Marks the start of a task with a custom name that should continue if the app enters the background.
- [func beginBackgroundTask(expirationHandler: (() -> Void)?) -> UIBackgroundTaskIdentifier](uiapplication/beginbackgroundtask(expirationhandler:).md)
  Marks the start of a task that should continue if the app enters the background.
- [struct UIBackgroundTaskIdentifier](uibackgroundtaskidentifier.md)
  A unique token that identifies a request to run in the background.
- [var backgroundTimeRemaining: TimeInterval](uiapplication/backgroundtimeremaining.md)
  The maximum amount of time remaining for the app to run in the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/endbackgroundtask(_:))*