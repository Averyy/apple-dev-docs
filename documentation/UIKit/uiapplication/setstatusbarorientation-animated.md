# setStatusBarOrientation(_:animated:)

**Framework**: UIKit  
**Kind**: method

Sets the app’s status bar to the specified orientation, optionally animating the transition.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func setStatusBarOrientation(_ interfaceOrientation: UIInterfaceOrientation, animated: Bool)
```

#### Discussion

Calling this method changes the value of the  [`statusBarOrientation`](uiapplication/statusbarorientation.md) property and rotates the status bar, animating the transition if animated is [`true`](https://developer.apple.com/documentation/swift/true) . If your app has rotatable window content, however, you should not arbitrarily set status-bar orientation using this method. The status-bar orientation set by this method does not change if the device changes orientation.

## Parameters

- `interfaceOrientation`: A specific orientation of the status bar. See   for details. The default value is  .
- `animated`:   if the transition to the new orientation should be animated;   if it should be immediate, without animation.

## See Also

- [var statusBarOrientationAnimationDuration: TimeInterval](uiapplication/statusbarorientationanimationduration.md)
  The animation duration in seconds for the status bar during a 90 degree orientation change.
- [var statusBarOrientation: UIInterfaceOrientation](uiapplication/statusbarorientation.md)
  The current orientation of the app’s status bar.
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
- [func registerUserNotificationSettings(UIUserNotificationSettings)](uiapplication/registerusernotificationsettings(_:).md)
  Registers your preferred options for notifying the user.
- [func registerForRemoteNotifications(matching: UIRemoteNotificationType)](uiapplication/registerforremotenotifications(matching:).md)
  Register to receive remote notifications of the specified types via Apple Push Notification service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/setstatusbarorientation(_:animated:))*