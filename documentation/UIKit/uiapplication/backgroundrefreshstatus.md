# backgroundRefreshStatus

**Framework**: UIKit  
**Kind**: property

Indicates whether the app can refresh content when running in the background.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var backgroundRefreshStatus: UIBackgroundRefreshStatus { get }
```

#### Discussion

You can use this property to determine whether Background App Refresh—an app’s ability to open in the background to perform refresh tasks—is enabled, and warn the user if it is not. Don’t warn the user if the value of this property is set to [`UIBackgroundRefreshStatus.restricted`](uibackgroundrefreshstatus/restricted.md). A restricted user, such as one who is managed under parental controls, can’t enable Background App Refresh.

Background App Refresh is disabled automatically when a device is operating in low-power mode. When this happens, the time available for performing background tasks is reduced to save power.

## See Also

- [enum UIBackgroundRefreshStatus](uibackgroundrefreshstatus.md)
  Constants that indicate whether background execution is enabled for the app.
- [class let backgroundRefreshStatusDidChangeNotification: NSNotification.Name](uiapplication/backgroundrefreshstatusdidchangenotification.md)
  A notification that posts when the app’s status for downloading content in the background changes.
- [func beginBackgroundTask(withName: String?, expirationHandler: (() -> Void)?) -> UIBackgroundTaskIdentifier](uiapplication/beginbackgroundtask(withname:expirationhandler:).md)
  Marks the start of a task with a custom name that should continue if the app enters the background.
- [func beginBackgroundTask(expirationHandler: (() -> Void)?) -> UIBackgroundTaskIdentifier](uiapplication/beginbackgroundtask(expirationhandler:).md)
  Marks the start of a task that should continue if the app enters the background.
- [func endBackgroundTask(UIBackgroundTaskIdentifier)](uiapplication/endbackgroundtask(_:).md)
  Marks the end of a specific long-running background task.
- [struct UIBackgroundTaskIdentifier](uibackgroundtaskidentifier.md)
  A unique token that identifies a request to run in the background.
- [var backgroundTimeRemaining: TimeInterval](uiapplication/backgroundtimeremaining.md)
  The maximum amount of time remaining for the app to run in the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/backgroundrefreshstatus)*