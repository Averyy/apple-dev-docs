# registerForRemoteNotifications(matching:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Register to receive remote notifications of the specified types via Apple Push Notification service.

**Availability**:
- iOS 3.0+ - Deprecated in 8.0
- iPadOS 3.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use the [`registerForRemoteNotifications()`](./registerforremotenotifications%28%29.md) method instead.

## Declaration

```swift
func registerForRemoteNotifications(matching types: UIRemoteNotificationType)
```

```objc
- (void) registerForRemoteNotificationTypes:(UIRemoteNotificationType) types;
```

#### Discussion

When you send this message, the device initiates the registration process with Apple Push Notification service. If it succeeds, the app delegate receives a device token in the [`application(_:didRegisterForRemoteNotificationsWithDeviceToken:)`](../uiapplicationdelegate/application%28_,didregisterforremotenotificationswithdevicetoken%29.md) method; if registration doesn’t succeed, the delegate is informed via the [`application(_:didFailToRegisterForRemoteNotificationsWithError:)`](../uiapplicationdelegate/application%28_,didfailtoregisterforremotenotificationswitherror%29.md) method. If the app delegate receives a device token, it should connect with its provider and pass it the token.

iOS does not display or play notification types specified in the notification payload that are not one of the requested ones. For example, if alert messages are not one of the accepted notification types, iOS does not display an alert even if one is specified in the notification payload. To find out what the app’s current notification types are, call the [`enabledRemoteNotificationTypes()`](./enabledremotenotificationtypes%28%29.md) method.

## Parameters

- `types`: A bit mask specifying the types of notifications the app accepts. For a list of values, see [`UIRemoteNotificationType`](../uiremotenotificationtype.md).

## See Also

### Deprecated methods
- [func requestSceneSessionActivation(UISceneSession?, userActivity: NSUserActivity?, options: UIScene.ActivationRequestOptions?, errorHandler: ((any Error) -> Void)?)](./requestscenesessionactivation%28_,useractivity,options,errorhandler%29.md)
  Asks the system to activate an existing scene, or create a new scene and associate it with your app.
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
- [- setStatusBarHidden:animated:](./setstatusbarhidden_animated_.md)
  Hides or shows the status bar, optionally animating the transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/registerforremotenotifications(matching:))*