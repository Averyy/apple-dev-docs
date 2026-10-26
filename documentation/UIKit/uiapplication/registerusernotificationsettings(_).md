# registerUserNotificationSettings(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Registers your preferred options for notifying the user.

**Availability**:
- iOS 8.0+ - Deprecated in 10.0
- iPadOS 8.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`requestAuthorization(options:completionHandler:)`](../../UserNotifications/unusernotificationcenter/requestauthorization%28options,completionhandler%29.md) and [`setNotificationCategories(_:)`](../../UserNotifications/unusernotificationcenter/setnotificationcategories%28_%29.md) instead.

## Declaration

```swift
func registerUserNotificationSettings(_ notificationSettings: UIUserNotificationSettings)
```

```objc
- (void) registerUserNotificationSettings:(UIUserNotificationSettings *) notificationSettings;
```

#### Discussion

If your app displays alerts, play sounds, or badges its icon, you must call this method during your launch cycle to request permission to alert the user in these ways. (You must also make this request if you want to set the [`applicationIconBadgeNumber`](./applicationiconbadgenumber.md) property directly.) Typically, you make this request if your app uses local or remote notifications to alert the user to new information involving your app. The first time your app launches and calls this method, the system asks the user whether your app should be allowed to deliver notifications and stores the response. Thereafter, the system uses the stored response to determine the actual types of notifications you may use.

After calling this method, the app calls the [`application(_:didRegister:)`](../uiapplicationdelegate/application%28_,didregister%29.md) method of its app delegate to report the results. You can use that method to determine if your request was granted or denied by the user.

It is recommended that you call this method before you schedule any local notifications or register with the push notification service. Apps that support custom actions must include all of their supported actions in the `notificationSettings` object.

## Parameters

- `notificationSettings`: The types of notifications that your app wants to use. You also use this object to specify custom actions that can be initiated by the user from an alert displayed in response to a local or remote notification.

## See Also

### Related Documentation
- [var currentUserNotificationSettings: UIUserNotificationSettings?](./currentusernotificationsettings.md)
  Returns the user notification settings for the app.
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
- [func registerForRemoteNotifications(matching: UIRemoteNotificationType)](./registerforremotenotifications%28matching%29.md)
  Register to receive remote notifications of the specified types via Apple Push Notification service.
- [- setStatusBarHidden:animated:](./setstatusbarhidden_animated_.md)
  Hides or shows the status bar, optionally animating the transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/registerusernotificationsettings(_:))*