# registerForRemoteNotifications(matching:)

**Framework**: UIKit  
**Kind**: method

Register to receive remote notifications of the specified types via Apple Push Notification service.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func registerForRemoteNotifications(matching types: UIRemoteNotificationType)
```

#### Discussion

When you send this message, the device initiates the registration process with Apple Push Notification service. If it succeeds, the app delegate receives a device token in the [`application(_:didRegisterForRemoteNotificationsWithDeviceToken:)`](uiapplicationdelegate/application(_:didregisterforremotenotificationswithdevicetoken:).md) method; if registration doesn’t succeed, the delegate is informed via the [`application(_:didFailToRegisterForRemoteNotificationsWithError:)`](uiapplicationdelegate/application(_:didfailtoregisterforremotenotificationswitherror:).md) method. If the app delegate receives a device token, it should connect with its provider and pass it the token.

iOS does not display or play notification types specified in the notification payload that are not one of the requested ones. For example, if alert messages are not one of the accepted notification types, iOS does not display an alert even if one is specified in the notification payload. To find out what the app’s current notification types are, call the [`enabledRemoteNotificationTypes()`](uiapplication/enabledremotenotificationtypes().md) method.

## Parameters

- `types`: A bit mask specifying the types of notifications the app accepts. For a list of values, see  .

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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/registerforremotenotifications(matching:))*