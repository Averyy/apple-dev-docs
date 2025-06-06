# applicationWillResignActive(_:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the app is about to become inactive.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func applicationWillResignActive(_ application: UIApplication)
```

## Mentions

- [About the background execution sequence](about-the-background-execution-sequence.md)

#### Discussion

> ❗ **Important**:  If you’re using scenes (see [`Scenes`](scenes.md)), UIKit will not call this method. Use [`sceneWillResignActive(_:)`](uiscenedelegate/scenewillresignactive(_:).md) instead to pause any activity or save state. UIKit posts a [`willResignActiveNotification`](uiapplication/willresignactivenotification.md) regardless of whether your app uses scenes.

 If you’re using scenes (see [`Scenes`](scenes.md)), UIKit will not call this method. Use [`sceneWillResignActive(_:)`](uiscenedelegate/scenewillresignactive(_:).md) instead to pause any activity or save state. UIKit posts a [`willResignActiveNotification`](uiapplication/willresignactivenotification.md) regardless of whether your app uses scenes.

UIKit calls this method to let your app know that it is about to move from the active to inactive state. The app moves to the inactive state because of temporary interruptions like an incoming phone call or SMS message, or when the user quits the app and it begins the transition to the background state. An app in the inactive state continues to run but doesn’t dispatch incoming events to responders.

Use this method to pause ongoing tasks, disable timers, and throttle down OpenGL ES frame rates. Games should use this method to pause the game. An app in the inactive state should do minimal work while it waits to transition to either the active or background state.

If your app has unsaved user data, you can save it to ensure that it isn’t lost. However, it is recommended that you save user data at appropriate points throughout the execution of your app, usually in response to specific actions. For example, save data when the user dismisses a data entry screen. Don’t rely on specific app state transitions to save all of your app’s critical data.

After calling this method, UIKit also posts a [`willResignActiveNotification`](uiapplication/willresignactivenotification.md) to give interested objects a chance to respond to the transition.

## Parameters

- `application`: Your singleton app object.

## See Also

- [func applicationDidBecomeActive(UIApplication)](uiapplicationdelegate/applicationdidbecomeactive(_:).md)
  Tells the delegate that the app has become active.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/applicationwillresignactive(_:))*