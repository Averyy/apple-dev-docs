# applicationWillEnterForeground(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the app is about to enter the foreground.

**Availability**:
- iOS 4.0+ - Deprecated in 26.0
- iPadOS 4.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

> **Deprecated**: Use UIScene lifecycle and sceneWillEnterForeground(_:) from UISceneDelegate or the UIApplication.willEnterForegroundNotification instead.

## Declaration

```swift
optional func applicationWillEnterForeground(_ application: UIApplication)
```

```objc
- (void) applicationWillEnterForeground:(UIApplication *) application;
```

## Mentions

- [Transitioning to the UIKit scene-based life cycle](../transitioning-to-the-uikit-scene-based-life-cycle.md)

## Discussion

In iOS 4.0 and later, UIKit calls this method as part of the transition from the background to the active state. You can use this method to undo many of the changes you made to your app upon entering the background. The call to this method is invariably followed by a call to the [`applicationDidBecomeActive(_:)`](./applicationdidbecomeactive%28_%29.md) method, which then moves the app from the inactive to the active state.

UIKit also posts a [`willEnterForegroundNotification`](../uiapplication/willenterforegroundnotification.md) shortly before calling this method to give interested objects a chance to respond to the transition.

> ❗ **Important**:  If your app adopts the scene-based life cycle (see [Scenes](../scenes.md)), UIKit doesn’t call this method. Use [`sceneWillEnterForeground(_:)`](../uiscenedelegate/scenewillenterforeground%28_%29.md) instead to prepare your scene to enter the foreground. UIKit posts a [`willEnterForegroundNotification`](../uiapplication/willenterforegroundnotification.md) regardless of whether your app adopts the scene-based life cycle, but in that case the notification reflects your app’s aggregate state ([`applicationState`](../uiapplication/applicationstate.md)) rather than any single scene’s transition. UIKit posts it when that aggregate state moves from background to foreground. If a person performs an action that brings an additional scene to the foreground while your app’s aggregate state is already in the foreground, that action doesn’t change the aggregate state, so UIKit doesn’t post the notification again.

## Parameters

- `application`: Your singleton app object.

## See Also

### Deprecated methods
- [func applicationDidBecomeActive(UIApplication)](./applicationdidbecomeactive%28_%29.md)
  Tells the delegate that the app has become active.
- [func applicationWillResignActive(UIApplication)](./applicationwillresignactive%28_%29.md)
  Tells the delegate that the app is about to become inactive.
- [func application(UIApplication, willContinueUserActivityWithType: String) -> Bool](./application%28_,willcontinueuseractivitywithtype%29.md)
  Tells the delegate if your app takes responsibility for notifying users when a continuation activity takes longer than expected.
- [func application(UIApplication, continue: NSUserActivity, restorationHandler: ([any UIUserActivityRestoring]?) -> Void) -> Bool](./application%28_,continue,restorationhandler%29.md)
  Tells the delegate that the data for continuing an activity is available.
- [func application(UIApplication, didUpdate: NSUserActivity)](./application%28_,didupdate%29.md)
  Tells the delegate that the activity was updated.
- [func application(UIApplication, didFailToContinueUserActivityWithType: String, error: any Error)](./application%28_,didfailtocontinueuseractivitywithtype,error%29.md)
  Tells the delegate that the activity couldn’t be continued.
- [func application(UIApplication, performActionFor: UIApplicationShortcutItem, completionHandler: (Bool) -> Void)](./application%28_,performactionfor,completionhandler%29.md)
  Tells the delegate that the user selected a Home screen quick action for your app, except when you’ve intercepted the interaction in a launch method.
- [func application(UIApplication, open: URL, options: [UIApplication.OpenURLOptionsKey : Any]) -> Bool](./application%28_,open,options%29.md)
  Asks the delegate to open a resource specified by a URL, and provides a dictionary of launch options.
- [func application(UIApplication, userDidAcceptCloudKitShareWith: CKShareMetadata)](./application%28_,userdidacceptcloudkitsharewith%29.md)
  Tells the delegate that the app now has access to shared information in CloudKit.
- [func application(UIApplication, supportedInterfaceOrientationsFor: UIWindow?) -> UIInterfaceOrientationMask](./application%28_,supportedinterfaceorientationsfor%29.md)
  Asks the delegate for the interface orientations to use for the view controllers in the specified window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/applicationwillenterforeground(_:))*