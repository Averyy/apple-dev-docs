# application(_:handleActionWithIdentifier:forRemoteNotification:withResponseInfo:completionHandler:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Called when your app has been activated by the user selecting an action from a remote notification.

**Availability**:
- iOS 9.0+ - Deprecated in 10.0
- iPadOS 9.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`userNotificationCenter(_:didReceive:withCompletionHandler:)`](../../UserNotifications/unusernotificationcenterdelegate/usernotificationcenter%28_,didreceive,withcompletionhandler%29.md) instead.

## Declaration

*iOS, iPadOS, Mac Catalyst*

```swift
optional func application(_ application: UIApplication, handleActionWithIdentifier identifier: String?, forRemoteNotification userInfo: [AnyHashable : Any], withResponseInfo responseInfo: [AnyHashable : Any], completionHandler: @escaping () -> Void)
```

*Mac Catalyst*

```swift
optional func application(_ application: UIApplication, handleActionWithIdentifier identifier: String?, forRemoteNotification userInfo: [AnyHashable : Any], withResponseInfo responseInfo: [AnyHashable : Any]) async
```

```objc
- (void) application:(UIApplication *) application handleActionWithIdentifier:(NSString *) identifier forRemoteNotification:(NSDictionary *) userInfo withResponseInfo:(NSDictionary *) responseInfo completionHandler:(void (^)()) completionHandler;
```

## Discussion

A `nil` value in the `identifier` parameter indicates the default action.

Call the completion handler as soon as you’ve finished handling the action.

## Parameters

- `application`: The app object that was activated for the user-selected action.
- `identifier`: The identifier for the custom action.
- `userInfo`: A dictionary that contains information related to the remote notification, potentially including a badge number for the app icon, an alert sound, an alert message to display to the user, a notification identifier, and custom data. The provider originates it as a JSON-defined dictionary that iOS converts to an [`NSDictionary`](../../Foundation/nsdictionary.md) object; the dictionary might contain only property-list objects plus [`NSNull`](../../Foundation/nsnull.md).
- `responseInfo`: The data dictionary sent by the action.
- `completionHandler`: A block that you must call when you are finished performing the action.

## See Also

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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:handleactionwithidentifier:forremotenotification:withresponseinfo:completionhandler:))*