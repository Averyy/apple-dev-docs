# setStatusBarOrientation(_:animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets the app’s status bar to the specified orientation, optionally animating the transition.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`statusBarManager`](../uiwindowscene/statusbarmanager.md) instead.

## Declaration

```swift
func setStatusBarOrientation(_ interfaceOrientation: UIInterfaceOrientation, animated: Bool)
```

```objc
- (void) setStatusBarOrientation:(UIInterfaceOrientation) interfaceOrientation animated:(BOOL) animated;
```

#### Discussion

Calling this method changes the value of the  [`statusBarOrientation`](./statusbarorientation.md) property and rotates the status bar, animating the transition if animated is [`true`](../../Swift/true.md) . If your app has rotatable window content, however, you should not arbitrarily set status-bar orientation using this method. The status-bar orientation set by this method does not change if the device changes orientation.

## Parameters

- `interfaceOrientation`: A specific orientation of the status bar. See [`UIInterfaceOrientation`](../uiinterfaceorientation.md) for details. The default value is [`UIInterfaceOrientation.portrait`](../uiinterfaceorientation/portrait.md).
- `animated`: [`true`](../../Swift/true.md) if the transition to the new orientation should be animated; [`false`](../../Swift/false.md) if it should be immediate, without animation.

## See Also

### Related Documentation
- [var statusBarOrientationAnimationDuration: TimeInterval](./statusbarorientationanimationduration.md)
  The animation duration in seconds for the status bar during a 90 degree orientation change.
- [var statusBarOrientation: UIInterfaceOrientation](./statusbarorientation.md)
  The current orientation of the app’s status bar.
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
- [func registerUserNotificationSettings(UIUserNotificationSettings)](./registerusernotificationsettings%28_%29.md)
  Registers your preferred options for notifying the user.
- [func registerForRemoteNotifications(matching: UIRemoteNotificationType)](./registerforremotenotifications%28matching%29.md)
  Register to receive remote notifications of the specified types via Apple Push Notification service.
- [- setStatusBarHidden:animated:](./setstatusbarhidden_animated_.md)
  Hides or shows the status bar, optionally animating the transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/setstatusbarorientation(_:animated:))*