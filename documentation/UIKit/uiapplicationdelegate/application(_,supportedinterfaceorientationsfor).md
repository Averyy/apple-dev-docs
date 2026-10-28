# application(_:supportedInterfaceOrientationsFor:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate for the interface orientations to use for the view controllers in the specified window.

**Availability**:
- iOS 6.0+ - Deprecated in 27.0
- iPadOS 6.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use [`supportedInterfaceOrientations(for:)`](../uiwindowscenedelegate/supportedinterfaceorientations%28for%29.md) instead.

## Declaration

```swift
optional func application(_ application: UIApplication, supportedInterfaceOrientationsFor window: UIWindow?) -> UIInterfaceOrientationMask
```

```objc
- (UIInterfaceOrientationMask) application:(UIApplication *) application supportedInterfaceOrientationsForWindow:(UIWindow *) window;
```

## Return Value

A bit mask of the [`UIInterfaceOrientationMask`](../uiinterfaceorientationmask.md) constants that indicate the orientations to use for the view controllers.

## Discussion

This method returns the total set of interface orientations supported by the app. When determining whether to rotate a particular view controller, the orientations returned by this method are intersected with the orientations supported by the root view controller or topmost presented view controller. The app and view controller must agree before the rotation is allowed.

If you do not implement this method, the app uses the values in the `UIInterfaceOrientation` key of the app’s `Info.plist` as the default interface orientations.

## Parameters

- `application`: Your singleton app object.
- `window`: The window whose interface orientations you want to retrieve.

## See Also

### Deprecated methods
- [func applicationDidBecomeActive(UIApplication)](./applicationdidbecomeactive%28_%29.md)
  Tells the delegate that the app has become active.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:supportedinterfaceorientationsfor:))*