# enabledRemoteNotificationTypes()

**Framework**: UIKit  
**Kind**: method

Returns the types of notifications the app accepts.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func enabledRemoteNotificationTypes() -> UIRemoteNotificationType
```

#### Return Value

A bit mask whose values indicate the types of notifications the user has requested for the app. See [`UIRemoteNotificationType`](uiremotenotificationtype.md) for valid bit-mask values.

#### Discussion

The values in the returned bit mask indicate the types of notifications currently enabled for the app. These types are first set when the app calls the [`registerForRemoteNotifications(matching:)`](uiapplication/registerforremotenotifications(matching:).md) method to register itself with Apple Push Notification service. Thereafter, the user may modify these accepted notification types in the Notifications preference of the Settings app. This method returns those initial or modified values. iOS does not display or play notification types specified in the notification payload that are not one of the enabled types. For example, the app might accept icon-badging as a form of notification, but might reject sounds and alert messages, even if they are specified in the notification payload.

## See Also

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
- [func registerUserNotificationSettings(UIUserNotificationSettings)](uiapplication/registerusernotificationsettings(_:).md)
  Registers your preferred options for notifying the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/enabledremotenotificationtypes())*