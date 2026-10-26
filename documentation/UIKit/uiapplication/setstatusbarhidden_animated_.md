# setStatusBarHidden:animated:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Hides or shows the status bar, optionally animating the transition.

**Availability**:
- iOS 2.0+ - Deprecated in 3.2
- iPadOS 2.0+ - Deprecated in 3.2
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use the [`setStatusBarHidden(_:with:)`](./setstatusbarhidden%28_,with%29.md) method instead.

## Declaration

```objc
- (void) setStatusBarHidden:(BOOL) hidden animated:(BOOL) animated;
```

#### Discussion

The animation fades the status bar out or in at the top of the interface, depending on the value of `hidden`.

## Parameters

- `hidden`: [`true`](../../Swift/true.md) if the status bar should be hidden, [`false`](../../Swift/false.md) if it should be visible. The default value is [`false`](../../Swift/false.md).
- `animated`: [`true`](../../Swift/true.md) if the transition to or from a hidden state should be animated, [`false`](../../Swift/false.md) otherwise.

## See Also

### Related Documentation
- [var isStatusBarHidden: Bool](./isstatusbarhidden.md)
  A Boolean value that determines whether the status bar is hidden.
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
- [func registerUserNotificationSettings(UIUserNotificationSettings)](./registerusernotificationsettings%28_%29.md)
  Registers your preferred options for notifying the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/setstatusbarhidden:animated:)*