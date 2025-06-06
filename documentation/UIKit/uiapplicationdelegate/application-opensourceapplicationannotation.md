# application(_:open:sourceApplication:annotation:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate to open a resource identified by a URL.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
optional func application(_ application: UIApplication, open url: URL, sourceApplication: String?, annotation: Any) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the delegate successfully handled the request or [`false`](https://developer.apple.com/documentation/swift/false) if the attempt to open the URL resource failed.

#### Discussion

Your implementation of this method should open the specified URL and update its user interface accordingly. If your app had to be launched to open the URL, the app calls the [`application(_:willFinishLaunchingWithOptions:)`](uiapplicationdelegate/application(_:willfinishlaunchingwithoptions:).md) and [`application(_:didFinishLaunchingWithOptions:)`](uiapplicationdelegate/application(_:didfinishlaunchingwithoptions:).md) methods first, followed by this method. The return values of those methods can be used to prevent this method from being called. (If the app is already running, only this method is called.)

If the URL refers to a file that was opened through a document interaction controller, the `annotation` parameter may contain additional data that the source app wanted to send along with the URL. The format of this data is defined by the app that sent it but the data must consist of objects that can be put into a property list.

Files sent to your app through AirDrop or a document interaction controller are placed in the `Documents/Inbox` directory of your app’s home directory. Your app has permission to read and delete files in this directory but does not have permission to write to them. If you want to modify a file, you must move it to a different directory first. In addition, files in that directory are usually encrypted using data protection. If the file is protected and the user locks the device before this method is called, you will be unable to read the file’s contents immediately. In that case, you should save the URL and try to open the file later rather than return [`false`](https://developer.apple.com/documentation/swift/false) from this method. Use the [`isProtectedDataAvailable`](uiapplication/isprotecteddataavailable.md) property of the app object to determine if data protection is currently enabled.

There is no matching notification for this method.

## Parameters

- `application`: Your singleton app object.
- `url`: The URL resource to open. This resource can be a network resource or a file. For information about the Apple-registered URL schemes, see  .
- `sourceApplication`: The bundle ID of the app that is requesting your app to open the URL ( ).
- `annotation`: A   supplied by the source app to communicate information to the receiving app.

## See Also

- [func application(UIApplication, didFinishLaunchingWithOptions: [UIApplication.LaunchOptionsKey : Any]?) -> Bool](uiapplicationdelegate/application(_:didfinishlaunchingwithoptions:).md)
  Tells the delegate that the launch process is almost done and the app is almost ready to run.
- [func openURL(URL) -> Bool](uiapplication/openurl(_:).md)
  Attempts to open the resource at the specified URL.
- [func application(UIApplication, didRegister: UIUserNotificationSettings)](uiapplicationdelegate/application(_:didregister:).md)
  Called to tell the delegate the types of local and remote notifications that can be used to get the user’s attention.
- [func application(UIApplication, didReceive: UILocalNotification)](uiapplicationdelegate/application(_:didreceive:).md)
  Sent to the delegate when a running app receives a local notification.
- [func application(UIApplication, didReceiveRemoteNotification: [AnyHashable : Any])](uiapplicationdelegate/application(_:didreceiveremotenotification:).md)
  Called when your app has received a remote notification.
- [func application(UIApplication, handleActionWithIdentifier: String?, for: UILocalNotification, completionHandler: () -> Void)](uiapplicationdelegate/application(_:handleactionwithidentifier:for:completionhandler:).md)
  Called when your app has been activated because user selected a custom action from the alert panel of a local notification.
- [func application(UIApplication, handleActionWithIdentifier: String?, for: UILocalNotification, withResponseInfo: [AnyHashable : Any], completionHandler: () -> Void)](uiapplicationdelegate/application(_:handleactionwithidentifier:for:withresponseinfo:completionhandler:).md)
  Called when your app has been activated by the user selecting an action from a local notification.
- [func application(UIApplication, handleActionWithIdentifier: String?, forRemoteNotification: [AnyHashable : Any], completionHandler: () -> Void)](uiapplicationdelegate/application(_:handleactionwithidentifier:forremotenotification:completionhandler:).md)
  Tells the app delegate to perform the custom action specified by a remote notification.
- [func application(UIApplication, handleActionWithIdentifier: String?, forRemoteNotification: [AnyHashable : Any], withResponseInfo: [AnyHashable : Any], completionHandler: () -> Void)](uiapplicationdelegate/application(_:handleactionwithidentifier:forremotenotification:withresponseinfo:completionhandler:).md)
  Called when your app has been activated by the user selecting an action from a remote notification.
- [func application(UIApplication, handleOpen: URL) -> Bool](uiapplicationdelegate/application(_:handleopen:).md)
  Asks the delegate to open a resource identified by URL.
- [func application(UIApplication, willChangeStatusBarOrientation: UIInterfaceOrientation, duration: TimeInterval)](uiapplicationdelegate/application(_:willchangestatusbarorientation:duration:).md)
  Tells the delegate when the interface orientation of the status bar is about to change.
- [func application(UIApplication, didChangeStatusBarOrientation: UIInterfaceOrientation)](uiapplicationdelegate/application(_:didchangestatusbarorientation:).md)
  Tells the delegate when the interface orientation of the status bar has changed.
- [func application(UIApplication, willChangeStatusBarFrame: CGRect)](uiapplicationdelegate/application(_:willchangestatusbarframe:).md)
  Tells the delegate when the frame of the status bar is about to change.
- [func application(UIApplication, didChangeStatusBarFrame: CGRect)](uiapplicationdelegate/application(_:didchangestatusbarframe:).md)
  Tells the delegate when the frame of the status bar has changed.
- [func application(UIApplication, handle: INIntent, completionHandler: (INIntentResponse) -> Void)](uiapplicationdelegate/application(_:handle:completionhandler:).md)
  Asks the delegate to handle the specified SiriKit intent directly.
- [func application(UIApplication, performFetchWithCompletionHandler: (UIBackgroundFetchResult) -> Void)](uiapplicationdelegate/application(_:performfetchwithcompletionhandler:).md)
  Tells the app that it can begin a fetch operation if it has data to download.
- [func application(UIApplication, shouldSaveApplicationState: NSCoder) -> Bool](uiapplicationdelegate/application(_:shouldsaveapplicationstate:).md)
  Asks the delegate whether to preserve the app’s state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:open:sourceapplication:annotation:))*