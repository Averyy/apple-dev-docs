# applicationWillEnterForeground(_:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the app is about to enter the foreground.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func applicationWillEnterForeground(_ application: UIApplication)
```

## Mentions

- [Transitioning to the UIKit scene-based life cycle](transitioning-to-the-uikit-scene-based-life-cycle.md)

#### Discussion

In iOS 4.0 and later, UIKit calls this method as part of the transition from the background to the active state. You can use this method to undo many of the changes you made to your app upon entering the background. The call to this method is invariably followed by a call to the [`applicationDidBecomeActive(_:)`](uiapplicationdelegate/applicationdidbecomeactive(_:).md) method, which then moves the app from the inactive to the active state.

UIKit also posts a [`willEnterForegroundNotification`](uiapplication/willenterforegroundnotification.md) shortly before calling this method to give interested objects a chance to respond to the transition.

> ❗ **Important**:  If your app adopts the scene-based life cycle (see [`Scenes`](scenes.md)), UIKit doesn’t call this method. Use [`sceneWillEnterForeground(_:)`](uiscenedelegate/scenewillenterforeground(_:).md) instead to prepare your scene to enter the foreground. UIKit posts a [`willEnterForegroundNotification`](uiapplication/willenterforegroundnotification.md) regardless of whether your app adopts the scene-based life cycle, but in that case the notification reflects your app’s aggregate state ([`applicationState`](uiapplication/applicationstate.md)) rather than any single scene’s transition. UIKit posts it when that aggregate state moves from background to foreground. If a person performs an action that brings an additional scene to the foreground while your app’s aggregate state is already in the foreground, that action doesn’t change the aggregate state, so UIKit doesn’t post the notification again.

## Parameters

- `application`: Your singleton app object.

## See Also

- [func applicationDidBecomeActive(UIApplication)](uiapplicationdelegate/applicationdidbecomeactive(_:).md)
  Tells the delegate that the app has become active.
- [func applicationWillResignActive(UIApplication)](uiapplicationdelegate/applicationwillresignactive(_:).md)
  Tells the delegate that the app is about to become inactive.
- [func applicationDidEnterBackground(UIApplication)](uiapplicationdelegate/applicationdidenterbackground(_:).md)
  Tells the delegate that the app is now in the background.
- [func applicationWillTerminate(UIApplication)](uiapplicationdelegate/applicationwillterminate(_:).md)
  Tells the delegate when the app is about to terminate.
- [class let didBecomeActiveNotification: NSNotification.Name](uiapplication/didbecomeactivenotification.md)
  A notification that posts when the app becomes active.
- [class let didEnterBackgroundNotification: NSNotification.Name](uiapplication/didenterbackgroundnotification.md)
  A notification that posts when the app enters the background.
- [class let willEnterForegroundNotification: NSNotification.Name](uiapplication/willenterforegroundnotification.md)
  A notification that posts shortly before your app’s UI transitions to the foreground.
- [class let willResignActiveNotification: NSNotification.Name](uiapplication/willresignactivenotification.md)
  A notification that posts when the app is no longer active and loses focus.
- [class let willTerminateNotification: NSNotification.Name](uiapplication/willterminatenotification.md)
  A notification that posts when the app is about to terminate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/applicationwillenterforeground(_:))*