# application(_:open:options:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate to open a resource specified by a URL, and provides a dictionary of launch options.

**Availability**:
- iOS 9.0+ - Deprecated in 26.0
- iPadOS 9.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

> **Deprecated**: Use UIScene lifecycle and scene(_:openURLContexts:) from UISceneDelegate instead.

## Declaration

```swift
optional func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool
```

```objc
- (BOOL) application:(UIApplication *) app openURL:(NSURL *) url options:(NSDictionary<NSString *,id> *) options;
```

## Mentions

- [Enabling document sharing](../enabling-document-sharing.md)

## Return Value

[`true`](../../Swift/true.md) if the delegate successfully handled the request or [`false`](../../Swift/false.md) if the attempt to open the URL resource failed.

## Discussion

This method is not called if your implementations return [`false`](../../Swift/false.md) from both the [`application(_:willFinishLaunchingWithOptions:)`](./application%28_,willfinishlaunchingwithoptions%29.md) and [`application(_:didFinishLaunchingWithOptions:)`](./application%28_,didfinishlaunchingwithoptions%29.md) methods. (If only one of the two methods is implemented, its return value determines whether this method is called.) If your app implements the [`applicationDidFinishLaunching(_:)`](./applicationdidfinishlaunching%28_%29.md) method instead of [`application(_:didFinishLaunchingWithOptions:)`](./application%28_,didfinishlaunchingwithoptions%29.md), this method is called to open the specified URL after the app has been initialized.

If a URL arrives while your app is suspended or running in the background, the system moves your app to the foreground prior to calling this method.

There is no equivalent notification for this delegation method.

## Parameters

- `app`: Your singleton app object.
- `url`: The URL resource to open. This resource can be a network resource or a file. For information about the Apple-registered URL schemes, see [Apple URL Scheme Reference](https://developer.apple.com/library/archive/featuredarticles/iPhoneURLScheme_Reference/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007899).
- `options`: A dictionary of URL handling options. For information about the possible keys in this dictionary and how to handle them, see `UIApplicationOpenURLOptionsKey`. By default, the value of this parameter is an empty dictionary.

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
- [func application(UIApplication, userDidAcceptCloudKitShareWith: CKShareMetadata)](./application%28_,userdidacceptcloudkitsharewith%29.md)
  Tells the delegate that the app now has access to shared information in CloudKit.
- [func application(UIApplication, supportedInterfaceOrientationsFor: UIWindow?) -> UIInterfaceOrientationMask](./application%28_,supportedinterfaceorientationsfor%29.md)
  Asks the delegate for the interface orientations to use for the view controllers in the specified window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:open:options:))*