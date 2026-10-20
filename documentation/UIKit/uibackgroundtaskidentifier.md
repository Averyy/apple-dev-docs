# UIBackgroundTaskIdentifier

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

A unique token that identifies a request to run in the background.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
struct UIBackgroundTaskIdentifier
```

```c
typedef NSUInteger UIBackgroundTaskIdentifier;
```

## Topics

### Identifier
- [static let invalid: UIBackgroundTaskIdentifier](./uibackgroundtaskidentifier/invalid.md)
  A token that indicates an invalid task request.
### Initializers
- [init(rawValue: Int)](./uibackgroundtaskidentifier/init%28rawvalue%29.md)
  Creates a new instance with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Managing background tasks
- [var backgroundRefreshStatus: UIBackgroundRefreshStatus](./uiapplication/backgroundrefreshstatus.md)
  Indicates whether the app can refresh content when running in the background.
- [enum UIBackgroundRefreshStatus](./uibackgroundrefreshstatus.md)
  Constants that indicate whether background execution is enabled for the app.
- [class let backgroundRefreshStatusDidChangeNotification: NSNotification.Name](./uiapplication/backgroundrefreshstatusdidchangenotification.md)
  A notification that posts when the app’s status for downloading content in the background changes.
- [func beginBackgroundTask(withName: String?, expirationHandler: (() -> Void)?) -> UIBackgroundTaskIdentifier](./uiapplication/beginbackgroundtask%28withname,expirationhandler%29.md)
  Marks the start of a task with a custom name that should continue if the app enters the background.
- [func beginBackgroundTask(expirationHandler: (() -> Void)?) -> UIBackgroundTaskIdentifier](./uiapplication/beginbackgroundtask%28expirationhandler%29.md)
  Marks the start of a task that should continue if the app enters the background.
- [func endBackgroundTask(UIBackgroundTaskIdentifier)](./uiapplication/endbackgroundtask%28_%29.md)
  Marks the end of a specific long-running background task.
- [var backgroundTimeRemaining: TimeInterval](./uiapplication/backgroundtimeremaining.md)
  The maximum amount of time remaining for the app to run in the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibackgroundtaskidentifier)*