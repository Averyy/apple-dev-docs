# UIBackgroundRefreshStatus

**Framework**: UIKit  
**Kind**: enum

Constants that indicate whether background execution is enabled for the app.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum UIBackgroundRefreshStatus
```

## Topics

### Constants
- [UIBackgroundRefreshStatus.restricted](uibackgroundrefreshstatus/restricted.md)
  Background updates are unavailable and the user cannot enable them again.
- [UIBackgroundRefreshStatus.denied](uibackgroundrefreshstatus/denied.md)
  The user explicitly disabled background behavior for this app or for the whole system.
- [UIBackgroundRefreshStatus.available](uibackgroundrefreshstatus/available.md)
  Background updates are available for the app.
### Initializers
- [init?(rawValue: Int)](uibackgroundrefreshstatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var backgroundRefreshStatus: UIBackgroundRefreshStatus](uiapplication/backgroundrefreshstatus.md)
  Indicates whether the app can refresh content when running in the background.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibackgroundrefreshstatus)*