# application(_:didReceiveRemoteNotification:)

**Framework**: UIKit  
**Kind**: method

Called when your app has received a remote notification.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
optional func application(_ application: UIApplication, didReceiveRemoteNotification userInfo: [AnyHashable : Any])
```

#### Discussion

Implement the [`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`](uiapplicationdelegate/application(_:didreceiveremotenotification:fetchcompletionhandler:).md) method instead of this one whenever possible. If your delegate implements both methods, the app object calls the [`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`](uiapplicationdelegate/application(_:didreceiveremotenotification:fetchcompletionhandler:).md) method.

If the app is running, the app calls this method to process incoming remote notifications. The `userInfo` dictionary contains the `aps` key whose value is another dictionary with the remaining notification data. Although you should not need the information in the `aps` dictionary, you can retrieve its contents using the following keys:

- `alert`—The value is either a string for the alert message or a dictionary with two keys: `body` and `show-view`. The value of the `body` key is a string containing the alert message and the value of the `show-view` key is a Boolean. If the value of the `show-view` key is `false`, the alert’s View button is not shown. The default is to show the View button which, if the user taps it, launches the app.
- `badge`—A number indicating the quantity of data items to download from the provider. This number is to be displayed on the app icon. The absence of a `badge` property indicates that any number currently badging the icon should be removed.
- `sound`—The name of a sound file in the app bundle to play as an alert sound. If “default” is specified, the default sound should be played.

The `userInfo` dictionary may also have custom data defined by the provider according to the JSON schema. The properties for custom data should be specified at the same level as the `aps` dictionary. However, custom-defined properties should not be used for mass data transport because there is a strict size limit per notification (256 bytes) and delivery is not guaranteed.

If the app is not running when a remote notification arrives, the method launches the app and provides the appropriate information in the launch options dictionary. The app does not call this method to handle that remote notification. Instead, your implementation of the [`application(_:willFinishLaunchingWithOptions:)`](uiapplicationdelegate/application(_:willfinishlaunchingwithoptions:).md) or [`application(_:didFinishLaunchingWithOptions:)`](uiapplicationdelegate/application(_:didfinishlaunchingwithoptions:).md) method needs to get the remote notification payload data and respond appropriately.

For more information about how to implement remote notifications in your app, see [`Local and Remote Notification Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/index.html#//apple_ref/doc/uid/TP40008194).

## Parameters

- `application`: The app object that received the remote notification.
- `userInfo`: A dictionary that contains information related to the remote notification, potentially including a badge number for the app icon, an alert sound, an alert message to display to the user, a notification identifier, and custom data. The provider originates it as a JSON-defined dictionary that iOS converts to an   object; the dictionary might contain only property-list objects plus  .

## See Also

- [func application(UIApplication, didRegisterForRemoteNotificationsWithDeviceToken: Data)](uiapplicationdelegate/application(_:didregisterforremotenotificationswithdevicetoken:).md)
  Tells the delegate that the app successfully registered with Apple Push Notification service (APNs).
- [func application(UIApplication, didFailToRegisterForRemoteNotificationsWithError: any Error)](uiapplicationdelegate/application(_:didfailtoregisterforremotenotificationswitherror:).md)
  Tells the delegate when Apple Push Notification service cannot successfully complete the registration process.
- [func application(UIApplication, didRegister: UIUserNotificationSettings)](uiapplicationdelegate/application(_:didregister:).md)
  Called to tell the delegate the types of local and remote notifications that can be used to get the user’s attention.
- [func application(UIApplication, didReceive: UILocalNotification)](uiapplicationdelegate/application(_:didreceive:).md)
  Sent to the delegate when a running app receives a local notification.
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
- [func application(UIApplication, open: URL, sourceApplication: String?, annotation: Any) -> Bool](uiapplicationdelegate/application(_:open:sourceapplication:annotation:).md)
  Asks the delegate to open a resource identified by a URL.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:didreceiveremotenotification:))*