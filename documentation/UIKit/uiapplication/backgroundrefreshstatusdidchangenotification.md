# backgroundRefreshStatusDidChangeNotification

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A notification that posts when the app’s status for downloading content in the background changes.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
class let backgroundRefreshStatusDidChangeNotification: NSNotification.Name
```

```c
extern NSNotificationName const UIApplicationBackgroundRefreshStatusDidChangeNotification;
```

## Discussion

The system sends this notification when the [`backgroundRefreshStatus`](./backgroundrefreshstatus.md) property of the app object changes. That property can change in response to the user disabling multitasking support for the app. The `object` of the notification is the `UIApplication` object. There is no `userInfo` dictionary.

## See Also

### Managing background tasks
- [var backgroundRefreshStatus: UIBackgroundRefreshStatus](./backgroundrefreshstatus.md)
  Indicates whether the app can refresh content when running in the background.
- [enum UIBackgroundRefreshStatus](../uibackgroundrefreshstatus.md)
  Constants that indicate whether background execution is enabled for the app.
- [func beginBackgroundTask(withName: String?, expirationHandler: (() -> Void)?) -> UIBackgroundTaskIdentifier](./beginbackgroundtask%28withname,expirationhandler%29.md)
  Marks the start of a task with a custom name that should continue if the app enters the background.
- [func beginBackgroundTask(expirationHandler: (() -> Void)?) -> UIBackgroundTaskIdentifier](./beginbackgroundtask%28expirationhandler%29.md)
  Marks the start of a task that should continue if the app enters the background.
- [func endBackgroundTask(UIBackgroundTaskIdentifier)](./endbackgroundtask%28_%29.md)
  Marks the end of a specific long-running background task.
- [struct UIBackgroundTaskIdentifier](../uibackgroundtaskidentifier.md)
  A unique token that identifies a request to run in the background.
- [var backgroundTimeRemaining: TimeInterval](./backgroundtimeremaining.md)
  The maximum amount of time remaining for the app to run in the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/backgroundrefreshstatusdidchangenotification)*