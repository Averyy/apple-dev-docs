# application(_:didRegister:)

**Framework**: UIKit  
**Kind**: method

Called to tell the delegate the types of local and remote notifications that can be used to get the user’s attention.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
optional func application(_ application: UIApplication, didRegister notificationSettings: UIUserNotificationSettings)
```

#### Discussion

Apps that use local or remote notifications to alert the user to new information must register the types of notifications they want to use by calling the [`registerUserNotificationSettings(_:)`](uiapplication/registerusernotificationsettings(_:).md) method of the app object. The system compares your app’s request with the user’s preferences to determine the types of local and remote notifications allowed, and returns the results to your app by calling this method. Check the contents of the `notificationSettings` parameter whenever this method is called.

Because the user can change notification settings in the Settings app at any time, call the [`currentUserNotificationSettings`](uiapplication/currentusernotificationsettings.md) method before your app performs work to prepare a notification for presentation.

The first time you register your app’s preferred notification types, the system asks the user whether your app should be allowed to deliver notifications and stores the user’s response. The system does not prompt the user on subsequent calls to the [`registerUserNotificationSettings(_:)`](uiapplication/registerusernotificationsettings(_:).md) method, but the user can always change notification preferences using Settings.

A user’s notification settings control only whether the system  local or remote notifications onscreen. Regardless of the notification settings, local and remote notifications are delivered to your app at the appropriate times.

## Parameters

- `application`: The app object that registered the user notification settings.
- `notificationSettings`: The user’s specified notification settings for your app. The settings in this object may be different than the ones you originally requested.

## See Also

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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:didregister:))*