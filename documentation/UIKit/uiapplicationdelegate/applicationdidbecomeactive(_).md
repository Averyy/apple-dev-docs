# applicationDidBecomeActive(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the app has become active.

**Availability**:
- iOS 2.0+ - Deprecated in 26.0
- iPadOS 2.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

> **Deprecated**: Use UIScene lifecycle and sceneDidBecomeActive(_:) from UISceneDelegate or the UIApplication.didBecomeActiveNotification instead.

## Declaration

```swift
optional func applicationDidBecomeActive(_ application: UIApplication)
```

```objc
- (void) applicationDidBecomeActive:(UIApplication *) application;
```

## Mentions

- [Transitioning to the UIKit scene-based life cycle](../transitioning-to-the-uikit-scene-based-life-cycle.md)

#### Discussion

> ❗ **Important**:  If you’re using scenes (see [Scenes](../scenes.md)), UIKit will not call this method. Use [`sceneDidBecomeActive(_:)`](../uiscenedelegate/scenedidbecomeactive%28_%29.md) instead to restart any tasks or refresh your app’s user interface. UIKit posts a [`didBecomeActiveNotification`](../uiapplication/didbecomeactivenotification.md) regardless of whether your app uses scenes.

UIKit calls this method to let your app know that it moved from the inactive to active state. The app moves to the active state because it was launched by the user or the system, or because the user ignores an interruption (like an incoming phone call or SMS message) that sent the app temporarily to the inactive state.

Use this method to restart any tasks that were paused (or not yet started) while the app was inactive. For example, use it to restart timers or throttle up OpenGL ES frame rates. If your app was previously in the background, you can also use it to refresh your app’s user interface.

After calling this method, UIKit posts a [`didBecomeActiveNotification`](../uiapplication/didbecomeactivenotification.md) to give interested objects a chance to respond to the transition.

## Parameters

- `application`: Your singleton app object.

## See Also

### Deprecated methods
- [func applicationWillResignActive(UIApplication)](./applicationwillresignactive%28_%29.md)
  Tells the delegate that the app is about to become inactive.
- [func applicationWillEnterForeground(UIApplication)](./applicationwillenterforeground%28_%29.md)
  Tells the delegate that the app is about to enter the foreground.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/applicationdidbecomeactive(_:))*