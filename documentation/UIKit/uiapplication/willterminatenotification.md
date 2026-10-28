# willTerminateNotification

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A notification that posts when the app is about to terminate.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
nonisolated
class let willTerminateNotification: NSNotification.Name
```

```c
extern NSNotificationName const UIApplicationWillTerminateNotification;
```

## Discussion

This notification is associated with the delegate [`applicationWillTerminate(_:)`](../uiapplicationdelegate/applicationwillterminate%28_%29.md) method. This notification does not contain a `userInfo` dictionary.

## See Also

### Responding to app life-cycle events
- [func applicationDidEnterBackground(UIApplication)](../uiapplicationdelegate/applicationdidenterbackground%28_%29.md)
  Tells the delegate that the app is now in the background.
- [func applicationWillTerminate(UIApplication)](../uiapplicationdelegate/applicationwillterminate%28_%29.md)
  Tells the delegate when the app is about to terminate.
- [class let didBecomeActiveNotification: NSNotification.Name](./didbecomeactivenotification.md)
  A notification that posts when the app becomes active.
- [class let didEnterBackgroundNotification: NSNotification.Name](./didenterbackgroundnotification.md)
  A notification that posts when the app enters the background.
- [class let willEnterForegroundNotification: NSNotification.Name](./willenterforegroundnotification.md)
  A notification that posts shortly before your app’s UI transitions to the foreground.
- [class let willResignActiveNotification: NSNotification.Name](./willresignactivenotification.md)
  A notification that posts when the app is no longer active and loses focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/willterminatenotification)*