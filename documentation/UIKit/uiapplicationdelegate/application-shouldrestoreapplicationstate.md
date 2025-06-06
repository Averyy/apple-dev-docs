# application(_:shouldRestoreApplicationState:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate whether to restore the app’s saved state.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
optional func application(_ application: UIApplication, shouldRestoreApplicationState coder: NSCoder) -> Bool
```

## Mentions

- [About the UI restoration process](about-the-ui-restoration-process.md)

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the app’s state should be restored; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

Apps must implement this method and the [`application(_:shouldSaveApplicationState:)`](uiapplicationdelegate/application(_:shouldsaveapplicationstate:).md) method for state preservation to occur. In addition, your implementation of this method must return [`true`](https://developer.apple.com/documentation/swift/true) each time UIKit tries to restore the state of your app. You can use the information in the provided coder object to decide whether or not to proceed with state restoration. For example, you might return [`false`](https://developer.apple.com/documentation/swift/false) if the data in the coder is from a different version of your app and can’t be effectively restored to the current version.

## Parameters

- `application`: Your singleton app object.
- `coder`: The keyed archiver containing the app’s previously saved state information.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:shouldrestoreapplicationstate:))*