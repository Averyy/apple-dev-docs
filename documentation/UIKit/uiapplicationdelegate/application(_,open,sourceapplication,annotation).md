# application(_:open:sourceApplication:annotation:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate to open a resource identified by a URL.

**Availability**:
- iOS 4.2+ - Deprecated in 9.0
- iPadOS 4.2+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`application(_:open:options:)`](./application%28_,open,options%29.md) instead.

## Declaration

```swift
optional func application(_ application: UIApplication, open url: URL, sourceApplication: String?, annotation: Any) -> Bool
```

```objc
- (BOOL) application:(UIApplication *) application openURL:(NSURL *) url sourceApplication:(NSString *) sourceApplication annotation:(id) annotation;
```

#### Return Value

[`true`](../../Swift/true.md) if the delegate successfully handled the request or [`false`](../../Swift/false.md) if the attempt to open the URL resource failed.

#### Discussion

Your implementation of this method should open the specified URL and update its user interface accordingly. If your app had to be launched to open the URL, the app calls the [`application(_:willFinishLaunchingWithOptions:)`](./application%28_,willfinishlaunchingwithoptions%29.md) and [`application(_:didFinishLaunchingWithOptions:)`](./application%28_,didfinishlaunchingwithoptions%29.md) methods first, followed by this method. The return values of those methods can be used to prevent this method from being called. (If the app is already running, only this method is called.)

If the URL refers to a file that was opened through a document interaction controller, the `annotation` parameter may contain additional data that the source app wanted to send along with the URL. The format of this data is defined by the app that sent it but the data must consist of objects that can be put into a property list.

Files sent to your app through AirDrop or a document interaction controller are placed in the `Documents/Inbox` directory of your app’s home directory. Your app has permission to read and delete files in this directory but does not have permission to write to them. If you want to modify a file, you must move it to a different directory first. In addition, files in that directory are usually encrypted using data protection. If the file is protected and the user locks the device before this method is called, you will be unable to read the file’s contents immediately. In that case, you should save the URL and try to open the file later rather than return [`false`](../../Swift/false.md) from this method. Use the [`isProtectedDataAvailable`](../uiapplication/isprotecteddataavailable.md) property of the app object to determine if data protection is currently enabled.

There is no matching notification for this method.

## Parameters

- `application`: Your singleton app object.
- `url`: The URL resource to open. This resource can be a network resource or a file. For information about the Apple-registered URL schemes, see [Apple URL Scheme Reference](https://developer.apple.com/library/archive/featuredarticles/iPhoneURLScheme_Reference/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007899).
- `sourceApplication`: The bundle ID of the app that is requesting your app to open the URL (`url`).
- `annotation`: A [Property list](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/PropertyList.html#//apple_ref/doc/uid/TP40008195-CH44) supplied by the source app to communicate information to the receiving app.

## See Also

### Related Documentation
- [func application(UIApplication, didFinishLaunchingWithOptions: [UIApplication.LaunchOptionsKey : Any]?) -> Bool](./application%28_,didfinishlaunchingwithoptions%29.md)
  Tells the delegate that the launch process is almost done and the app is almost ready to run.
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
- [func application(UIApplication, handleOpen: URL) -> Bool](./application%28_,handleopen%29.md)
  Asks the delegate to open a resource identified by URL.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:open:sourceapplication:annotation:))*