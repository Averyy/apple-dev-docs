# setKeepAliveTimeout(_:handler:)

**Framework**: UIKit  
**Kind**: method

Configures a periodic handler for VoIP apps in older versions of iOS.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func setKeepAliveTimeout(_ timeout: TimeInterval, handler keepAliveHandler: (() -> Void)? = nil) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the handler was installed or [`false`](https://developer.apple.com/documentation/Swift/false) if it was not.

#### Discussion

In iOS 8 and later, voice-over-IP (VoIP) apps register for [`registerForRemoteNotifications()`](uiapplication/registerforremotenotifications().md) remote notifications instead of using this method. Using remote notifications eliminates the need for a timeout handler to check in with the VoIP service. Instead, when a calls arrives for the user, the VoIP service sends a VoIP remote notification to the user’s device. Upon receiving this notification, the device launches or wakes the app as needed so that it can handle the incoming call.

In iOS 7 and earlier, VoIP apps use this method to install a handler whose job is to maintain the app’s network connection with a VoIP server. This handler is guaranteed to be called before the specified timeout value but may be called at a slightly different time interval in order to better align execution of your handler with other system tasks, and thereby save power. Your handler has a maximum of 10 seconds to perform any needed tasks and exit. If it does not exit before time expires, the app is suspended.

Timeout values and handlers are not persisted between app launches. Therefore, if your app is terminated for any reason, you must reinstall the handler during the next launch cycle.

For calls to this method to succeed, the app must have the `voip` value in the array associated with the `UIBackgroundModes` key in its `Info.plist` file. Calling this method replaces the previously installed handler and timeout values, if any.

## Parameters

- `timeout`: The maximum interval (measured in seconds) at which your app should be woken up to check its VoIP connection. The minimum acceptable timeout value is 600 seconds.
- `keepAliveHandler`: A block that performs the tasks needed to maintain your VoIP network connection. Setting this parameter to   releases the current handler block and prevents UIKit from scheduling the next wake.

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
- [func registerForRemoteNotifications(matching: UIRemoteNotificationType)](uiapplication/registerforremotenotifications(matching:).md)
  Register to receive remote notifications of the specified types via Apple Push Notification service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/setkeepalivetimeout(_:handler:))*