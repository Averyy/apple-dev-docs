# application(_:handleOpen:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate to open a resource identified by URL.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use the [`application(_:open:options:)`](./application%28_,open,options%29.md) method instead.

## Declaration

```swift
optional func application(_ application: UIApplication, handleOpen url: URL) -> Bool
```

```objc
- (BOOL) application:(UIApplication *) application handleOpenURL:(NSURL *) url;
```

## Return Value

[`true`](../../Swift/true.md) if the delegate successfully handled the request; [`false`](../../Swift/false.md) if the attempt to handle the URL failed.

## Discussion

If the delegate also implements the [`application(_:open:sourceApplication:annotation:)`](./application%28_,open,sourceapplication,annotation%29.md) method, that method is called instead of this one.

This method is not called if the delegate returns [`false`](../../Swift/false.md) from both the [`application(_:willFinishLaunchingWithOptions:)`](./application%28_,willfinishlaunchingwithoptions%29.md) and [`application(_:didFinishLaunchingWithOptions:)`](./application%28_,didfinishlaunchingwithoptions%29.md) methods. (If only one of the two methods is implemented, its return value determines whether this method is called.) If your app implements the [`applicationDidFinishLaunching(_:)`](./applicationdidfinishlaunching%28_%29.md) method instead of [`application(_:didFinishLaunchingWithOptions:)`](./application%28_,didfinishlaunchingwithoptions%29.md), this method is called to open the specified URL after the app has been initialized.

If a URL arrives while your app is suspended or running in the background, the system moves your app to the foreground prior to calling this method.

There is no equivalent notification for this delegation method.

## Parameters

- `application`: Your singleton app object.
- `url`: An object representing a URL (Universal Resource Locator). See the appendix of [App Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007072) for Apple-registered schemes for URLs.

## See Also

### Related Documentation
- [func application(UIApplication, didFinishLaunchingWithOptions: [UIApplication.LaunchOptionsKey : Any]?) -> Bool](./application%28_,didfinishlaunchingwithoptions%29.md)
  Tells the delegate that the launch process is almost done and the app is almost ready to run.
- [func application(UIApplication, willFinishLaunchingWithOptions: [UIApplication.LaunchOptionsKey : Any]?) -> Bool](./application%28_,willfinishlaunchingwithoptions%29.md)
  Tells the delegate that the launch process has begun.
- [func openURL(URL) -> Bool](../uiapplication/openurl%28_%29.md)
  Attempts to open the resource at the specified URL.
### Deprecated
- [func application(UIApplication, didRegister: UIUserNotificationSettings)](./application%28_,didregister%29.md)
  Called to tell the delegate the types of local and remote notifications that can be used to get the user’s attention.
- [func application(UIApplication, didReceive: UILocalNotification)](./application%28_,didreceive%29.md)
  Sent to the delegate when a running app receives a local notification.
- [func application(UIApplication, didReceiveRemoteNotification: [AnyHashable : Any])](./application%28_,didreceiveremotenotification%29.md)
  Called when your app has received a remote notification.
- [func application(UIApplication, handleActionWithIdentifier: String?, for: UILocalNotification, completionHandler: () -> Void)](./application%28_,handleactionwithidentifier,for,completionhandler%29.md)
  Called when your app has been activated because user selected a custom action from the alert panel of a local notification.
- [func application(UIApplication, handleActionWithIdentifier: String?, for: UILocalNotification, withResponseInfo: [AnyHashable : Any], completionHandler: () -> Void)](./application%28_,handleactionwithidentifier,for,withresponseinfo,completionhandler%29.md)
  Called when your app has been activated by the user selecting an action from a local notification.
- [func application(UIApplication, handleActionWithIdentifier: String?, forRemoteNotification: [AnyHashable : Any], completionHandler: () -> Void)](./application%28_,handleactionwithidentifier,forremotenotification,completionhandler%29.md)
  Tells the app delegate to perform the custom action specified by a remote notification.
- [func application(UIApplication, handleActionWithIdentifier: String?, forRemoteNotification: [AnyHashable : Any], withResponseInfo: [AnyHashable : Any], completionHandler: () -> Void)](./application%28_,handleactionwithidentifier,forremotenotification,withresponseinfo,completionhandler%29.md)
  Called when your app has been activated by the user selecting an action from a remote notification.
- [func application(UIApplication, open: URL, sourceApplication: String?, annotation: Any) -> Bool](./application%28_,open,sourceapplication,annotation%29.md)
  Asks the delegate to open a resource identified by a URL.
- [func application(UIApplication, willChangeStatusBarOrientation: UIInterfaceOrientation, duration: TimeInterval)](./application%28_,willchangestatusbarorientation,duration%29.md)
  Tells the delegate when the interface orientation of the status bar is about to change.
- [func application(UIApplication, didChangeStatusBarOrientation: UIInterfaceOrientation)](./application%28_,didchangestatusbarorientation%29.md)
  Tells the delegate when the interface orientation of the status bar has changed.
- [func application(UIApplication, willChangeStatusBarFrame: CGRect)](./application%28_,willchangestatusbarframe%29.md)
  Tells the delegate when the frame of the status bar is about to change.
- [func application(UIApplication, didChangeStatusBarFrame: CGRect)](./application%28_,didchangestatusbarframe%29.md)
  Tells the delegate when the frame of the status bar has changed.
- [func application(UIApplication, handle: INIntent, completionHandler: (INIntentResponse) -> Void)](./application%28_,handle,completionhandler%29.md)
  Asks the delegate to handle the specified SiriKit intent directly.
- [func application(UIApplication, performFetchWithCompletionHandler: (UIBackgroundFetchResult) -> Void)](./application%28_,performfetchwithcompletionhandler%29.md)
  Tells the app that it can begin a fetch operation if it has data to download.
- [func application(UIApplication, shouldSaveApplicationState: NSCoder) -> Bool](./application%28_,shouldsaveapplicationstate%29.md)
  Asks the delegate whether to preserve the app’s state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:handleopen:))*