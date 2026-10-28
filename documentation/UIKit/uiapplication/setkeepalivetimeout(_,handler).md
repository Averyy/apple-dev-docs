# setKeepAliveTimeout(_:handler:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Configures a periodic handler for VoIP apps in older versions of iOS.

**Availability**:
- iOS 4.0+ - Deprecated in 9.0
- iPadOS 4.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: This legacy VoIP API was deprecated in iOS 10.0. Use [PushKit](../../PushKit/PushKit.md) to develop VoIP apps.

## Declaration

```swift
func setKeepAliveTimeout(_ timeout: TimeInterval, handler keepAliveHandler: (() -> Void)? = nil) -> Bool
```

```objc
- (BOOL) setKeepAliveTimeout:(NSTimeInterval) timeout handler:(void (^)()) keepAliveHandler;
```

## Return Value

[`true`](../../Swift/true.md) if the handler was installed or [`false`](../../Swift/false.md) if it was not.

## Discussion

In iOS 8 and later, voice-over-IP (VoIP) apps register for [`registerForRemoteNotifications()`](./registerforremotenotifications%28%29.md) remote notifications instead of using this method. Using remote notifications eliminates the need for a timeout handler to check in with the VoIP service. Instead, when a calls arrives for the user, the VoIP service sends a VoIP remote notification to the user’s device. Upon receiving this notification, the device launches or wakes the app as needed so that it can handle the incoming call.

In iOS 7 and earlier, VoIP apps use this method to install a handler whose job is to maintain the app’s network connection with a VoIP server. This handler is guaranteed to be called before the specified timeout value but may be called at a slightly different time interval in order to better align execution of your handler with other system tasks, and thereby save power. Your handler has a maximum of 10 seconds to perform any needed tasks and exit. If it does not exit before time expires, the app is suspended.

Timeout values and handlers are not persisted between app launches. Therefore, if your app is terminated for any reason, you must reinstall the handler during the next launch cycle.

For calls to this method to succeed, the app must have the `voip` value in the array associated with the `UIBackgroundModes` key in its `Info.plist` file. Calling this method replaces the previously installed handler and timeout values, if any.

## Parameters

- `timeout`: The maximum interval (measured in seconds) at which your app should be woken up to check its VoIP connection. The minimum acceptable timeout value is 600 seconds.
- `keepAliveHandler`: A block that performs the tasks needed to maintain your VoIP network connection. Setting this parameter to `nil` releases the current handler block and prevents UIKit from scheduling the next wake.

## See Also

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
- [func registerForRemoteNotifications(matching: UIRemoteNotificationType)](./registerforremotenotifications%28matching%29.md)
  Register to receive remote notifications of the specified types via Apple Push Notification service.
- [- setStatusBarHidden:animated:](./setstatusbarhidden_animated_.md)
  Hides or shows the status bar, optionally animating the transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/setkeepalivetimeout(_:handler:))*