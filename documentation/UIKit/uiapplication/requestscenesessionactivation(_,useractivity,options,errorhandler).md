# requestSceneSessionActivation(_:userActivity:options:errorHandler:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the system to activate an existing scene, or create a new scene and associate it with your app.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.2
- tvOS 13.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`activateSceneSession(for:errorHandler:)`](./activatescenesession%28for,errorhandler%29.md) (Swift) or [`activateSceneSessionForRequest:errorHandler:`](./activatescenesessionforrequest_errorhandler_.md) (Objective-C) instead.

## Declaration

```swift
func requestSceneSessionActivation(_ sceneSession: UISceneSession?, userActivity: NSUserActivity?, options: UIScene.ActivationRequestOptions?, errorHandler: ((any Error) -> Void)? = nil)
```

```objc
- (void) requestSceneSessionActivation:(UISceneSession *) sceneSession userActivity:(NSUserActivity *) userActivity options:(UISceneActivationRequestOptions *) options errorHandler:(void (^)(NSError *error)) errorHandler;
```

#### Discussion

Call this method when you want the system to display one of your app’s scenes. For example, you might call this method to dispatch work to the scene in the form of an [`NSUserActivity`](../../Foundation/nsuseractivity.md) object. When activating an existing session whose scene is no longer in memory, the system creates a new scene and connects it to your app. Similarly, specifying `nil` for the `sceneSession` parameter causes the system to create a new scene and corresponding session.

## Parameters

- `sceneSession`: The session whose scene you want to activate. Specify `nil` when you want the system to create a new scene for your app.
- `userActivity`: A user activity object to dispatch to the session’s scene. Use this object to communicate details about a task you want the scene to perform.
- `options`: Information for the system to use when creating or activating the scene. For information about how to create this object, see [`UIScene.ActivationRequestOptions`](../uiscene/activationrequestoptions.md).
- `errorHandler`: An error handler block to execute if a problem occurs. The method doesn’t execute this block when it successfully activates the scene. This block has no return value and has the following parameter:

  - **error**: The [`NSError`](../../Foundation/nserror.md) object describing the problem that occurred.

## See Also

### Deprecated methods
- [func beginIgnoringInteractionEvents()](./beginignoringinteractionevents%28%29.md)
  Tells the receiver to suspend the handling of touch-related events.
- [func endIgnoringInteractionEvents()](./endignoringinteractionevents%28%29.md)
  Tells the receiver to resume the handling of touch-related events.
- [func setMinimumBackgroundFetchInterval(TimeInterval)](./setminimumbackgroundfetchinterval%28_%29.md)
  Specifies the minimum amount of time that must elapse between background fetch operations.
- [func scheduleLocalNotification(UILocalNotification)](./schedulelocalnotification%28_%29.md)
  Schedules a local notification for delivery at its encapsulated date and time.
- [func presentLocalNotificationNow(UILocalNotification)](./presentlocalnotificationnow%28_%29.md)
  Presents a local notification immediately.
- [func cancelLocalNotification(UILocalNotification)](./cancellocalnotification%28_%29.md)
  Cancels the delivery of the specified scheduled local notification.
- [func cancelAllLocalNotifications()](./cancelalllocalnotifications%28%29.md)
  Cancels the delivery of all scheduled local notifications.
- [func setKeepAliveTimeout(TimeInterval, handler: (() -> Void)?) -> Bool](./setkeepalivetimeout%28_,handler%29.md)
  Configures a periodic handler for VoIP apps in older versions of iOS.
- [let UIMinimumKeepAliveTimeout: TimeInterval](../uiminimumkeepalivetimeout.md)
  The minimum amount of time (measured in seconds) an app may run a critical background task in the background.
- [func clearKeepAliveTimeout()](./clearkeepalivetimeout%28%29.md)
  Removes a previously installed periodic handler block.
- [func setStatusBarHidden(Bool, with: UIStatusBarAnimation)](./setstatusbarhidden%28_,with%29.md)
  Hides or shows the status bar, optionally animating the transition.
- [func setStatusBarStyle(UIStatusBarStyle, animated: Bool)](./setstatusbarstyle%28_,animated%29.md)
  Sets the style of the status bar, optionally animating the transition to the new style.
- [func setStatusBarOrientation(UIInterfaceOrientation, animated: Bool)](./setstatusbarorientation%28_,animated%29.md)
  Sets the app’s status bar to the specified orientation, optionally animating the transition.
- [func registerUserNotificationSettings(UIUserNotificationSettings)](./registerusernotificationsettings%28_%29.md)
  Registers your preferred options for notifying the user.
- [func registerForRemoteNotifications(matching: UIRemoteNotificationType)](./registerforremotenotifications%28matching%29.md)
  Register to receive remote notifications of the specified types via Apple Push Notification service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/requestscenesessionactivation(_:useractivity:options:errorhandler:))*