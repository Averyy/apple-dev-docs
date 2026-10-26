# application(_:handle:completionHandler:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate to handle the specified SiriKit intent directly.

**Availability**:
- iOS 11.0+ - Deprecated in 14.0
- iPadOS 11.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- tvOS 11.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`application(_:handlerFor:)`](./application%28_,handlerfor%29.md) instead to provide an object to resolve, confirm, and handle intents in your app.

## Declaration

```swift
optional func application(_ application: UIApplication, handle intent: INIntent, completionHandler: @escaping (INIntentResponse) -> Void)
```

```swift
optional func application(_ application: UIApplication, handle intent: INIntent) async -> INIntentResponse
```

```objc
- (void) application:(UIApplication *) application handleIntent:(INIntent *) intent completionHandler:(void (^)(INIntentResponse *intentResponse)) completionHandler;
```

#### Discussion

With this method, an app can handle an intent directly, rather than handling it in the app’s Intent extension. You might use this method to implement workflows that you can’t implement easily in your extension. For example, you might use it to start or manage a user’s workout session. If your app isn’t running, SiriKit launches your app in the background so that the Siri interface remains active.

Your Intents app extension is still responsible for resolving and confirming the intent details. Your extension’s [`handler(for:)`](../../Intents/inintenthandlerproviding/handler%28for%29.md) method must create a response object that resolves and confirms the intent details. In the response object’s `handle(intent:completion:)` implementation, return a response object with a status code of `failureRequiringAppLaunch`. Upon receiving your response, SiriKit launches the app and calls [`application(_:handle:completionHandler:)`](./application%28_,handle,completionhandler%29.md). In your implementation of this app delegate method, handle the intent by performing the user’s intended action if possible. Then call the provided completion handler with a response object that indicates if your app performed the intent or provides a reason it could not. For details about how to handle a specific intent, see the class reference for that intent in [SiriKit](../../SiriKit/SiriKit.md).

## Parameters

- `application`: The shared app object.
- `intent`: The intent object that contains information about the SiriKit request. Use this object to identify what the user intends and what kind of response to provide.
- `completionHandler`: The handler block to execute with your response. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **intentResponse**: The response object you create to report the status of the request. The exact type of this object must correspond to the type of intent delivered. For example, if the `intent` parameter contains an [`INStartWorkoutIntent`](../../Intents/instartworkoutintent.md) object, you must create an [`INStartWorkoutIntentResponse`](../../Intents/instartworkoutintentresponse.md) object. This parameter must not be `nil`.

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
- [func application(UIApplication, performFetchWithCompletionHandler: (UIBackgroundFetchResult) -> Void)](./application%28_,performfetchwithcompletionhandler%29.md)
  Tells the app that it can begin a fetch operation if it has data to download.
- [func application(UIApplication, shouldSaveApplicationState: NSCoder) -> Bool](./application%28_,shouldsaveapplicationstate%29.md)
  Asks the delegate whether to preserve the app’s state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:handle:completionhandler:))*