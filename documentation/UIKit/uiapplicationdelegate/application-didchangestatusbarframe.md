# application(_:didChangeStatusBarFrame:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate when the frame of the status bar has changed.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
optional func application(_ application: UIApplication, didChangeStatusBarFrame oldStatusBarFrame: CGRect)
```

#### Discussion

After calling this method, the app also posts a [`didChangeStatusBarFrameNotification`](uiapplication/didchangestatusbarframenotification.md) notification to give interested objects a chance to respond to the change.

## Parameters

- `application`: Your singleton app object.
- `oldStatusBarFrame`: The previous frame of the status bar, in screen coordinates.

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
- [func application(UIApplication, handle: INIntent, completionHandler: (INIntentResponse) -> Void)](uiapplicationdelegate/application(_:handle:completionhandler:).md)
  Asks the delegate to handle the specified SiriKit intent directly.
- [func application(UIApplication, performFetchWithCompletionHandler: (UIBackgroundFetchResult) -> Void)](uiapplicationdelegate/application(_:performfetchwithcompletionhandler:).md)
  Tells the app that it can begin a fetch operation if it has data to download.
- [func application(UIApplication, shouldSaveApplicationState: NSCoder) -> Bool](uiapplicationdelegate/application(_:shouldsaveapplicationstate:).md)
  Asks the delegate whether to preserve the app’s state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:didchangestatusbarframe:))*