# setStatusBarStyle(_:animated:)

**Framework**: UIKit  
**Kind**: method

Sets the style of the status bar, optionally animating the transition to the new style.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func setStatusBarStyle(_ statusBarStyle: UIStatusBarStyle, animated: Bool)
```

#### Discussion

The animation slides the status bar out toward the top of the interface.

In iOS 7 and later, status bar behavior is determined by view controllers, and so calling this method has no effect by default. When view controller-based status bar appearance is disabled, this method behaves normally. To opt out of the view controller-based status bar appearance behavior, you must add the `UIViewControllerBasedStatusBarAppearance` key with a value of [`false`](https://developer.apple.com/documentation/swift/false) to your app’s `Info.plist` file, but doing so is not recommended.

## Parameters

- `statusBarStyle`: A constant that specifies a style for the status bar. See the descriptions of the constants in   for details.
- `animated`:   if the transition to the new style should be animated; otherwise   .

## See Also

- [var statusBarStyle: UIStatusBarStyle](uiapplication/statusbarstyle.md)
  The current style of the status bar.
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
- [func setStatusBarOrientation(UIInterfaceOrientation, animated: Bool)](uiapplication/setstatusbarorientation(_:animated:).md)
  Sets the app’s status bar to the specified orientation, optionally animating the transition.
- [func registerUserNotificationSettings(UIUserNotificationSettings)](uiapplication/registerusernotificationsettings(_:).md)
  Registers your preferred options for notifying the user.
- [func registerForRemoteNotifications(matching: UIRemoteNotificationType)](uiapplication/registerforremotenotifications(matching:).md)
  Register to receive remote notifications of the specified types via Apple Push Notification service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/setstatusbarstyle(_:animated:))*