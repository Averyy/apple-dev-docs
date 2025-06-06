# requestSceneSessionActivation(_:userActivity:options:errorHandler:)

**Framework**: UIKit  
**Kind**: method

Asks the system to activate an existing scene, or create a new scene and associate it with your app.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func requestSceneSessionActivation(_ sceneSession: UISceneSession?, userActivity: NSUserActivity?, options: UIScene.ActivationRequestOptions?, errorHandler: ((any Error) -> Void)? = nil)
```

#### Discussion

Call this method when you want the system to display one of your app’s scenes. For example, you might call this method to dispatch work to the scene in the form of an [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) object. When activating an existing session whose scene is no longer in memory, the system creates a new scene and connects it to your app. Similarly, specifying `nil` for the `sceneSession` parameter causes the system to create a new scene and corresponding session.

## Parameters

- `sceneSession`: The session whose scene you want to activate. Specify   when you want the system to create a new scene for your app.
- `userActivity`: A user activity object to dispatch to the session’s scene. Use this object to communicate details about a task you want the scene to perform.
- `options`: Information for the system to use when creating or activating the scene. For information about how to create this object, see  .
- `errorHandler`: An error handler block to execute if a problem occurs. The method doesn’t execute this block when it successfully activates the scene. This block has no return value and has the following parameter:

## See Also

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
- [func registerForRemoteNotifications(matching: UIRemoteNotificationType)](uiapplication/registerforremotenotifications(matching:).md)
  Register to receive remote notifications of the specified types via Apple Push Notification service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/requestscenesessionactivation(_:useractivity:options:errorhandler:))*