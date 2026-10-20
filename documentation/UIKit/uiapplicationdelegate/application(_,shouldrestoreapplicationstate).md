# application(_:shouldRestoreApplicationState:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate whether to restore the app’s saved state.

**Availability**:
- iOS 6.0+ - Deprecated in 13.2
- iPadOS 6.0+ - Deprecated in 13.2
- Mac Catalyst 13.1+ - Deprecated in 13.2
- tvOS - Deprecated in 13.2

> **Deprecated**: Use [`application(_:shouldRestoreSecureApplicationState:)`](./application%28_,shouldrestoresecureapplicationstate%29.md) instead.

## Declaration

```swift
optional func application(_ application: UIApplication, shouldRestoreApplicationState coder: NSCoder) -> Bool
```

```objc
- (BOOL) application:(UIApplication *) application shouldRestoreApplicationState:(NSCoder *) coder;
```

## Mentions

- [About the UI restoration process](../about-the-ui-restoration-process.md)

#### Return Value

[`true`](../../Swift/true.md) if the app’s state should be restored; otherwise, [`false`](../../Swift/false.md).

#### Discussion

Apps must implement this method and the [`application(_:shouldSaveApplicationState:)`](./application%28_,shouldsaveapplicationstate%29.md) method for state preservation to occur. In addition, your implementation of this method must return [`true`](../../Swift/true.md) each time UIKit tries to restore the state of your app. You can use the information in the provided coder object to decide whether or not to proceed with state restoration. For example, you might return [`false`](../../Swift/false.md) if the data in the coder is from a different version of your app and can’t be effectively restored to the current version.

## Parameters

- `application`: Your singleton app object.
- `coder`: The keyed archiver containing the app’s previously saved state information.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:shouldrestoreapplicationstate:))*