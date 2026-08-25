# willEnterForegroundNotification

**Framework**: UIKit  
**Kind**: property

A notification that posts shortly before your app’s UI transitions to the foreground.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
nonisolated
class let willEnterForegroundNotification: NSNotification.Name
```

## Mentions

- [Transitioning to the UIKit scene-based life cycle](transitioning-to-the-uikit-scene-based-life-cycle.md)

#### Discussion

The `object` of the notification is the [`UIApplication`](uiapplication.md) object. There is no `userInfo` dictionary.

If your app adopts the scene-based life cycle, this notification isn’t an app-level mirror of [`willEnterForegroundNotification`](uiscene/willenterforegroundnotification.md). That scene notification comes from an individual scene’s own life-cycle transition. This notification instead reflects your app’s aggregate state across all of its scenes. UIKit posts this notification when that aggregate state moves from background to foreground. If a person performs an action that brings an additional scene to the foreground while your app’s aggregate state is already in the foreground, that action doesn’t change the aggregate state, so this notification doesn’t fire again.

If your app launches directly into the foreground, UIKit posts this notification around launch time, as the launching scene transitions to the foreground and becomes visible. If your app launches into the background instead, for example to handle a silent push notification or a location update, this notification doesn’t fire at launch. It arrives later, only if your app actually enters the foreground.

## See Also

- [func applicationDidBecomeActive(UIApplication)](uiapplicationdelegate/applicationdidbecomeactive(_:).md)
  Tells the delegate that the app has become active.
- [func applicationWillResignActive(UIApplication)](uiapplicationdelegate/applicationwillresignactive(_:).md)
  Tells the delegate that the app is about to become inactive.
- [func applicationDidEnterBackground(UIApplication)](uiapplicationdelegate/applicationdidenterbackground(_:).md)
  Tells the delegate that the app is now in the background.
- [func applicationWillEnterForeground(UIApplication)](uiapplicationdelegate/applicationwillenterforeground(_:).md)
  Tells the delegate that the app is about to enter the foreground.
- [func applicationWillTerminate(UIApplication)](uiapplicationdelegate/applicationwillterminate(_:).md)
  Tells the delegate when the app is about to terminate.
- [class let didBecomeActiveNotification: NSNotification.Name](uiapplication/didbecomeactivenotification.md)
  A notification that posts when the app becomes active.
- [class let didEnterBackgroundNotification: NSNotification.Name](uiapplication/didenterbackgroundnotification.md)
  A notification that posts when the app enters the background.
- [class let willResignActiveNotification: NSNotification.Name](uiapplication/willresignactivenotification.md)
  A notification that posts when the app is no longer active and loses focus.
- [class let willTerminateNotification: NSNotification.Name](uiapplication/willterminatenotification.md)
  A notification that posts when the app is about to terminate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/willenterforegroundnotification)*