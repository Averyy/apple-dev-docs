# openURL(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Attempts to open the resource at the specified URL.

**Availability**:
- iOS 2.0+ - Deprecated in 10.0
- iPadOS 2.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS - Deprecated in 10.0

> **Deprecated**: Calling this method has no effect. Use the [`open(_:options:completionHandler:)`](./open%28_,options,completionhandler%29.md) method instead.

## Declaration

```swift
func openURL(_ url: URL) -> Bool
```

```objc
- (BOOL) openURL:(NSURL *) url;
```

#### Return Value

[`true`](../../Swift/true.md) if the resource located by the URL was successfully opened; otherwise [`false`](../../Swift/false.md).

#### Discussion

The URL you pass to this method can identify a resource in the app that calls the method, or a resource to be handled by another app. If the resource is to be handled another app, invoking this method might cause the calling app to quit so the other can launch.

To check if there is an installed app that can handle a scheme, call the [`canOpenURL(_:)`](./canopenurl%28_%29.md) method before calling this one. Be sure to read the description of that method for an important note about registering the schemes you want to employ.

## Parameters

- `url`: A URL (Universal Resource Locator). UIKit supports many common schemes, including the `http`, `https`, `tel`, `facetime`, and `mailto` schemes. You can also employ custom URL schemes associated with apps installed on the device.

## See Also

### Related Documentation
- [func application(UIApplication, handleOpen: URL) -> Bool](../uiapplicationdelegate/application%28_,handleopen%29.md)
  Asks the delegate to open a resource identified by URL.
- [func canOpenURL(URL) -> Bool](./canopenurl%28_%29.md)
  Returns a Boolean value that indicates whether an app is available to handle a URL scheme.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/openurl(_:))*