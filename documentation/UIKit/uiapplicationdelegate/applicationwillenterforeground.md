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
@MainActor
optional func applicationWillEnterForeground(_ application: UIApplication)
```

#### Discussion

> ❗ **Important**:  If you’re using scenes (see [`Scenes`](scenes.md)), UIKit will not call this method. Use [`sceneWillEnterForeground(_:)`](uiscenedelegate/scenewillenterforeground(_:).md) instead to prepare your app to enter the foreground. UIKit posts a [`willEnterForegroundNotification`](uiapplication/willenterforegroundnotification.md) regardless of whether your app uses [`Scenes`](scenes.md).

In iOS 4.0 and later, UIKit calls this method as part of the transition from the background to the active state. You can use this method to undo many of the changes you made to your app upon entering the background. The call to this method is invariably followed by a call to the [`applicationDidBecomeActive(_:)`](uiapplicationdelegate/applicationdidbecomeactive(_:).md) method, which then moves the app from the inactive to the active state.

UIKit also posts a [`willEnterForegroundNotification`](uiapplication/willenterforegroundnotification.md) shortly before calling this method to give interested objects a chance to respond to the transition.

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
  A notification that posts shortly before an app leaves the background state on its way to becoming the active app.
- [class let willResignActiveNotification: NSNotification.Name](uiapplication/willresignactivenotification.md)
  A notification that posts when the app is no longer active and loses focus.
- [class let willTerminateNotification: NSNotification.Name](uiapplication/willterminatenotification.md)
  A notification that posts when the app is about to terminate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/applicationwillenterforeground(_:))*