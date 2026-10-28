# application(_:willContinueUserActivityWithType:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate if your app takes responsibility for notifying users when a continuation activity takes longer than expected.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

> **Deprecated**: Use UIScene lifecycle and scene(_:willContinueUserActivityWithType:) from UISceneDelegate instead.

## Declaration

```swift
optional func application(_ application: UIApplication, willContinueUserActivityWithType userActivityType: String) -> Bool
```

```objc
- (BOOL) application:(UIApplication *) application willContinueUserActivityWithType:(NSString *) userActivityType;
```

## Return Value

[`true`](../../Swift/true.md) if you want to notify the user that a continuation is in progress or [`false`](../../Swift/false.md) if you want iOS to notify the user.

## Discussion

Use this method to provide immediate feedback to the user that an activity is about to continue on this device. The app calls this method as soon as the user confirms that an activity should be continued but possibly before the data associated with that activity is available.

Your implementation of this method should prepare to initiate the activity. If you notify the user as part of your preparations, return [`true`](../../Swift/true.md) from this method so that iOS does not also notify the user. If you do not implement this method or your implementation returns [`false`](../../Swift/false.md), iOS notifes the user.

This method is not called if either [`application(_:willFinishLaunchingWithOptions:)`](./application%28_,willfinishlaunchingwithoptions%29.md) or [`application(_:didFinishLaunchingWithOptions:)`](./application%28_,didfinishlaunchingwithoptions%29.md) returns [`false`](../../Swift/false.md).

## Parameters

- `application`: Your shared app object.
- `userActivityType`: The requested activity type.

## See Also

### Deprecated methods
- [func applicationDidBecomeActive(UIApplication)](./applicationdidbecomeactive%28_%29.md)
  Tells the delegate that the app has become active.
- [func applicationWillResignActive(UIApplication)](./applicationwillresignactive%28_%29.md)
  Tells the delegate that the app is about to become inactive.
- [func applicationWillEnterForeground(UIApplication)](./applicationwillenterforeground%28_%29.md)
  Tells the delegate that the app is about to enter the foreground.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:willcontinueuseractivitywithtype:))*