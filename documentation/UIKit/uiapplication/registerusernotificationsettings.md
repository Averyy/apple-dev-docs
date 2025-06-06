# registerUserNotificationSettings(_:)

**Framework**: UIKit  
**Kind**: method

Registers your preferred options for notifying the user.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func registerUserNotificationSettings(_ notificationSettings: UIUserNotificationSettings)
```

#### Discussion

If your app displays alerts, play sounds, or badges its icon, you must call this method during your launch cycle to request permission to alert the user in these ways. (You must also make this request if you want to set the [`applicationIconBadgeNumber`](uiapplication/applicationiconbadgenumber.md) property directly.) Typically, you make this request if your app uses local or remote notifications to alert the user to new information involving your app. The first time your app launches and calls this method, the system asks the user whether your app should be allowed to deliver notifications and stores the response. Thereafter, the system uses the stored response to determine the actual types of notifications you may use.

After calling this method, the app calls the [`application(_:didRegister:)`](uiapplicationdelegate/application(_:didregister:).md) method of its app delegate to report the results. You can use that method to determine if your request was granted or denied by the user.

It is recommended that you call this method before you schedule any local notifications or register with the push notification service. Apps that support custom actions must include all of their supported actions in the `notificationSettings` object.

## Parameters

- `notificationSettings`: The types of notifications that your app wants to use. You also use this object to specify custom actions that can be initiated by the user from an alert displayed in response to a local or remote notification.

## See Also

- [var currentUserNotificationSettings: UIUserNotificationSettings?](uiapplication/currentusernotificationsettings.md)
  Returns the user notification settings for the app.
- [func requestSceneSessionActivation(UISceneSession?, userActivity: NSUserActivity?, options: UIScene.ActivationRequestOptions?, errorHandler: ((any Error) -> Void)?)](uiapplication/requestscenesessionactivation(_:useractivity:options:errorhandler:).md)
  Asks the system to activate an existing scene, or create a new scene and associate it with your app.
- [func beginIgnoringInteractionEvents()](uiapplication/beginignoringinteractionevents.md)
  Tells the receiver to suspend the handling of touch-related events.
- [func endIgnoringInteractionEvents()](uiapplication/endignoringinteractionevents.md)
  Tells the receiver to resume the handling of touch-related events.
- [func setMinimumBackgroundFetchInterval(TimeInterval)](uiapplication/setminimumbackgroundfetchinterval(_:).md)
  Specifies the minimum amount of time that must elapse between background fetch operations.
- [func scheduleLocalNotification(UILocalNotification)](uiapplication/schedulelocalnotification(_:).md)
  Schedules a local notification for delivery at its encapsulated date and time.
- [func presentLocalNotificationNow(UILocalNotification)](uiapplication/presentlocalnotificationnow(_:).md)
  Presents a local notification immediately.
- [func cancelLocalNotification(UILocalNotification)](uiapplication/cancellocalnotification(_:).md)
  Cancels the delivery of the specified scheduled local notification.
- [func cancelAllLocalNotifications()](uiapplication/cancelalllocalnotifications.md)
  Cancels the delivery of all scheduled local notifications.
- [func setKeepAliveTimeout(TimeInterval, handler: (() -> Void)?) -> Bool](uiapplication/setkeepalivetimeout(_:handler:).md)
  Configures a periodic handler for VoIP apps in older versions of iOS.
- [let UIMinimumKeepAliveTimeout: TimeInterval](uiminimumkeepalivetimeout.md)
  The minimum amount of time (measured in seconds) an app may run a critical background task in the background.
- [func clearKeepAliveTimeout()](uiapplication/clearkeepalivetimeout.md)
  Removes a previously installed periodic handler block.
- [func setStatusBarHidden(Bool, with: UIStatusBarAnimation)](uiapplication/setstatusbarhidden(_:with:).md)
  Hides or shows the status bar, optionally animating the transition.
- [func setStatusBarStyle(UIStatusBarStyle, animated: Bool)](uiapplication/setstatusbarstyle(_:animated:).md)
  Sets the style of the status bar, optionally animating the transition to the new style.
- [func setStatusBarOrientation(UIInterfaceOrientation, animated: Bool)](uiapplication/setstatusbarorientation(_:animated:).md)
  Sets the app’s status bar to the specified orientation, optionally animating the transition.
- [func registerForRemoteNotifications(matching: UIRemoteNotificationType)](uiapplication/registerforremotenotifications(matching:).md)
  Register to receive remote notifications of the specified types via Apple Push Notification service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/registerusernotificationsettings(_:))*