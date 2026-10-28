# application(_:performActionFor:completionHandler:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the user selected a Home screen quick action for your app, except when you’ve intercepted the interaction in a launch method.

**Availability**:
- iOS 9.0+ - Deprecated in 26.0
- iPadOS 9.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

> **Deprecated**: Use UIScene lifecycle and windowScene(_:performActionFor:completionHandler:) from UIWindowSceneDelegate instead.

## Declaration

```swift
optional func application(_ application: UIApplication, performActionFor shortcutItem: UIApplicationShortcutItem, completionHandler: @escaping (Bool) -> Void)
```

```swift
optional func application(_ application: UIApplication, performActionFor shortcutItem: UIApplicationShortcutItem) async -> Bool
```

```objc
- (void) application:(UIApplication *) application performActionForShortcutItem:(UIApplicationShortcutItem *) shortcutItem completionHandler:(void (^)(BOOL succeeded)) completionHandler;
```

## Discussion

> ❗ **Important**:  This method is not called for scene-based apps. If you have a scene-based app, implement [`windowScene(_:performActionFor:completionHandler:)`](../uiwindowscenedelegate/windowscene%28_,performactionfor,completionhandler%29.md) in your scene delegate instead.

Implement this method to respond to the user’s selection of a Home screen quick action for your app. When finished, call the completion handler, with an appropriate Boolean value.

It’s your responsibility to ensure the system calls this method conditionally, depending on whether or not one of your app launch methods ([`application(_:willFinishLaunchingWithOptions:)`](./application%28_,willfinishlaunchingwithoptions%29.md) or [`application(_:didFinishLaunchingWithOptions:)`](./application%28_,didfinishlaunchingwithoptions%29.md)) has already handled a quick action invocation. The system calls a launch method (before calling this method) when a user selects a quick action for your app and your app *launches* instead of *activating*.

The requested quick action might employ code paths different than those used otherwise when your app launches. For example, your app normally launches to display view A, but your app was launched in response to a quick action that needs view B. To handle such cases, upon launch, check whether your app is being launched via a quick action. Perform this check in your [`application(_:willFinishLaunchingWithOptions:)`](./application%28_,willfinishlaunchingwithoptions%29.md) or [`application(_:didFinishLaunchingWithOptions:)`](./application%28_,didfinishlaunchingwithoptions%29.md) method by checking for the [`shortcutItem`](../uiapplication/launchoptionskey/shortcutitem.md) launch option key. The [`UIApplicationShortcutItem`](../uiapplicationshortcutitem.md) object is available as the value of the launch option key.

If you find that your app was indeed launched using a quick action, perform the requested quick action within the launch method and return a value of [`false`](../../Swift/false.md) from that method. When you return a value of [`false`](../../Swift/false.md), the system doesn’t call the [`application(_:performActionFor:completionHandler:)`](./application%28_,performactionfor,completionhandler%29.md) method.

## Parameters

- `application`: Your shared app object.
- `shortcutItem`: The quick action for which you’re providing an implementation in this method.
- `completionHandler`: The block you call after your quick action implementation completes, returning [`true`](../../Swift/true.md) or [`false`](../../Swift/false.md) depending on the success or failure of your implementation code.

  - **succeeded**: A Boolean value that indicates whether or not your implementation succeeded.

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
- [func application(UIApplication, open: URL, options: [UIApplication.OpenURLOptionsKey : Any]) -> Bool](./application%28_,open,options%29.md)
  Asks the delegate to open a resource specified by a URL, and provides a dictionary of launch options.
- [func application(UIApplication, userDidAcceptCloudKitShareWith: CKShareMetadata)](./application%28_,userdidacceptcloudkitsharewith%29.md)
  Tells the delegate that the app now has access to shared information in CloudKit.
- [func application(UIApplication, supportedInterfaceOrientationsFor: UIWindow?) -> UIInterfaceOrientationMask](./application%28_,supportedinterfaceorientationsfor%29.md)
  Asks the delegate for the interface orientations to use for the view controllers in the specified window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:performactionfor:completionhandler:))*