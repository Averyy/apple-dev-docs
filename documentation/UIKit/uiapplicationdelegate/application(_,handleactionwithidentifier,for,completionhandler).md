# application(_:handleActionWithIdentifier:for:completionHandler:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Called when your app has been activated because user selected a custom action from the alert panel of a local notification.

**Availability**:
- iOS 8.0+ - Deprecated in 10.0
- iPadOS 8.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`userNotificationCenter(_:didReceive:withCompletionHandler:)`](../../UserNotifications/unusernotificationcenterdelegate/usernotificationcenter%28_,didreceive,withcompletionhandler%29.md) instead.

## Declaration

*iOS, iPadOS, Mac Catalyst*

```swift
optional func application(_ application: UIApplication, handleActionWithIdentifier identifier: String?, for notification: UILocalNotification, completionHandler: @escaping () -> Void)
```

*Mac Catalyst*

```swift
optional func application(_ application: UIApplication, handleActionWithIdentifier identifier: String?, for notification: UILocalNotification) async
```

```objc
- (void) application:(UIApplication *) application handleActionWithIdentifier:(NSString *) identifier forLocalNotification:(UILocalNotification *) notification completionHandler:(void (^)()) completionHandler;
```

## Discussion

The app calls this method when the user taps an action button in an alert displayed in response to a local notification. Local notifications that include a registered category name in their [`category`](../uilocalnotification/category.md) property display buttons for the actions in that category. If the user taps one of those buttons, the system wakes up the app (launching it if needed) and calls this method in the background. Your implementation of this method should perform the action associated with the specified `identifier` and execute the block in the `completionHandler` parameter as soon as you are done. Failure to execute the completion handler block at the end of your implementation will cause your app to be terminated.

To configure the actions for a given category, create a UIUserNotificationActionSettings object and register it with the app when you call the [`registerUserNotificationSettings(_:)`](../uiapplication/registerusernotificationsettings%28_%29.md) method.

## Parameters

- `application`: The app object that received the local notification.
- `identifier`: The identifier associated with the custom action. This string corresponds to the identifier from the UILocalNotificationAction object that was used to configure the action in the local notification.
- `notification`: The local notification object that was triggered.
- `completionHandler`: A block to call when you are finished performing the action.

## See Also

### Deprecated
- [func application(UIApplication, didRegister: UIUserNotificationSettings)](./application%28_,didregister%29.md)
  Called to tell the delegate the types of local and remote notifications that can be used to get the user’s attention.
- [func application(UIApplication, didReceive: UILocalNotification)](./application%28_,didreceive%29.md)
  Sent to the delegate when a running app receives a local notification.
- [func application(UIApplication, didReceiveRemoteNotification: [AnyHashable : Any])](./application%28_,didreceiveremotenotification%29.md)
  Called when your app has received a remote notification.
- [func application(UIApplication, handleActionWithIdentifier: String?, for: UILocalNotification, withResponseInfo: [AnyHashable : Any], completionHandler: () -> Void)](./application%28_,handleactionwithidentifier,for,withresponseinfo,completionhandler%29.md)
  Called when your app has been activated by the user selecting an action from a local notification.
- [func application(UIApplication, handleActionWithIdentifier: String?, forRemoteNotification: [AnyHashable : Any], completionHandler: () -> Void)](./application%28_,handleactionwithidentifier,forremotenotification,completionhandler%29.md)
  Tells the app delegate to perform the custom action specified by a remote notification.
- [func application(UIApplication, handleActionWithIdentifier: String?, forRemoteNotification: [AnyHashable : Any], withResponseInfo: [AnyHashable : Any], completionHandler: () -> Void)](./application%28_,handleactionwithidentifier,forremotenotification,withresponseinfo,completionhandler%29.md)
  Called when your app has been activated by the user selecting an action from a remote notification.
- [func application(UIApplication, handleOpen: URL) -> Bool](./application%28_,handleopen%29.md)
  Asks the delegate to open a resource identified by URL.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:handleactionwithidentifier:for:completionhandler:))*