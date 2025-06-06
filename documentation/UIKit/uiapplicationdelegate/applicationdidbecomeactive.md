# applicationDidBecomeActive(_:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the app has become active.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func applicationDidBecomeActive(_ application: UIApplication)
```

#### Discussion

> ❗ **Important**:  If you’re using scenes (see [`Scenes`](scenes.md)), UIKit will not call this method. Use [`sceneDidBecomeActive(_:)`](uiscenedelegate/scenedidbecomeactive(_:).md) instead to restart any tasks or refresh your app’s user interface. UIKit posts a [`didBecomeActiveNotification`](uiapplication/didbecomeactivenotification.md) regardless of whether your app uses scenes.

 If you’re using scenes (see [`Scenes`](scenes.md)), UIKit will not call this method. Use [`sceneDidBecomeActive(_:)`](uiscenedelegate/scenedidbecomeactive(_:).md) instead to restart any tasks or refresh your app’s user interface. UIKit posts a [`didBecomeActiveNotification`](uiapplication/didbecomeactivenotification.md) regardless of whether your app uses scenes.

UIKit calls this method to let your app know that it moved from the inactive to active state. The app moves to the active state because it was launched by the user or the system, or because the user ignores an interruption (like an incoming phone call or SMS message) that sent the app temporarily to the inactive state.

Use this method to restart any tasks that were paused (or not yet started) while the app was inactive. For example, use it to restart timers or throttle up OpenGL ES frame rates. If your app was previously in the background, you can also use it to refresh your app’s user interface.

After calling this method, UIKit posts a [`didBecomeActiveNotification`](uiapplication/didbecomeactivenotification.md) to give interested objects a chance to respond to the transition.

## Parameters

- `application`: Your singleton app object.

## See Also

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
- [class let willEnterForegroundNotification: NSNotification.Name](uiapplication/willenterforegroundnotification.md)
  A notification that posts shortly before an app leaves the background state on its way to becoming the active app.
- [class let willResignActiveNotification: NSNotification.Name](uiapplication/willresignactivenotification.md)
  A notification that posts when the app is no longer active and loses focus.
- [class let willTerminateNotification: NSNotification.Name](uiapplication/willterminatenotification.md)
  A notification that posts when the app is about to terminate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/applicationdidbecomeactive(_:))*