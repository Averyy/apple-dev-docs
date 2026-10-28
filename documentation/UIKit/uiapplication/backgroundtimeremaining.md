# backgroundTimeRemaining

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The maximum amount of time remaining for the app to run in the background.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
nonisolated
var backgroundTimeRemaining: TimeInterval { get }
```

```objc
@property (nonatomic, readonly) NSTimeInterval backgroundTimeRemaining;
```

## Mentions

- [Extending your app’s background execution time](../extending-your-app-s-background-execution-time.md)

## Discussion

The value is valid only after the app enters the background and has started at least one task using [`beginBackgroundTask(expirationHandler:)`](./beginbackgroundtask%28expirationhandler%29.md) in the foreground.

System conditions may end background execution earlier, either by calling the expiration handler, or by terminating the app.

This method can be safely called on a non-main thread.

## See Also

### Managing background tasks
- [var backgroundRefreshStatus: UIBackgroundRefreshStatus](./backgroundrefreshstatus.md)
  Indicates whether the app can refresh content when running in the background.
- [enum UIBackgroundRefreshStatus](../uibackgroundrefreshstatus.md)
  Constants that indicate whether background execution is enabled for the app.
- [class let backgroundRefreshStatusDidChangeNotification: NSNotification.Name](./backgroundrefreshstatusdidchangenotification.md)
  A notification that posts when the app’s status for downloading content in the background changes.
- [func beginBackgroundTask(withName: String?, expirationHandler: (() -> Void)?) -> UIBackgroundTaskIdentifier](./beginbackgroundtask%28withname,expirationhandler%29.md)
  Marks the start of a task with a custom name that should continue if the app enters the background.
- [func beginBackgroundTask(expirationHandler: (() -> Void)?) -> UIBackgroundTaskIdentifier](./beginbackgroundtask%28expirationhandler%29.md)
  Marks the start of a task that should continue if the app enters the background.
- [func endBackgroundTask(UIBackgroundTaskIdentifier)](./endbackgroundtask%28_%29.md)
  Marks the end of a specific long-running background task.
- [struct UIBackgroundTaskIdentifier](../uibackgroundtaskidentifier.md)
  A unique token that identifies a request to run in the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/backgroundtimeremaining)*