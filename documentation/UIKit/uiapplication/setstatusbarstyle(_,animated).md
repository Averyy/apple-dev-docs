# setStatusBarStyle(_:animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets the style of the status bar, optionally animating the transition to the new style.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`preferredStatusBarStyle`](../uiviewcontroller/preferredstatusbarstyle.md) instead.

## Declaration

```swift
func setStatusBarStyle(_ statusBarStyle: UIStatusBarStyle, animated: Bool)
```

```objc
- (void) setStatusBarStyle:(UIStatusBarStyle) statusBarStyle animated:(BOOL) animated;
```

#### Discussion

The animation slides the status bar out toward the top of the interface.

In iOS 7 and later, status bar behavior is determined by view controllers, and so calling this method has no effect by default. When view controller-based status bar appearance is disabled, this method behaves normally. To opt out of the view controller-based status bar appearance behavior, you must add the `UIViewControllerBasedStatusBarAppearance` key with a value of [`false`](../../Swift/false.md) to your app’s `Info.plist` file, but doing so is not recommended.

## Parameters

- `statusBarStyle`: A constant that specifies a style for the status bar. See the descriptions of the constants in [`UIStatusBarStyle`](../uistatusbarstyle.md) for details.
- `animated`: [`true`](../../Swift/true.md) if the transition to the new style should be animated; otherwise [`false`](../../Swift/false.md) .

## See Also

### Related Documentation
- [var statusBarStyle: UIStatusBarStyle](./statusbarstyle.md)
  The current style of the status bar.
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
- [func setStatusBarOrientation(UIInterfaceOrientation, animated: Bool)](./setstatusbarorientation%28_,animated%29.md)
  Sets the app’s status bar to the specified orientation, optionally animating the transition.
- [func registerUserNotificationSettings(UIUserNotificationSettings)](./registerusernotificationsettings%28_%29.md)
  Registers your preferred options for notifying the user.
- [func registerForRemoteNotifications(matching: UIRemoteNotificationType)](./registerforremotenotifications%28matching%29.md)
  Register to receive remote notifications of the specified types via Apple Push Notification service.
- [- setStatusBarHidden:animated:](./setstatusbarhidden_animated_.md)
  Hides or shows the status bar, optionally animating the transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/setstatusbarstyle(_:animated:))*