# canOpenURL(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether an app is available to handle a URL scheme.

**Availability**:
- iOS 3.0+ - Deprecated in 27.0
- iPadOS 3.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Attempt to open the URL and handle any failure instead of validating it first. Using universal links instead of custom URL schemes removes the need for this validation entirely.

## Declaration

```swift
nonisolated
func canOpenURL(_ url: URL) -> Bool
```

```objc
- (BOOL) canOpenURL:(NSURL *) url;
```

#### Return Value

[`false`](../../Swift/false.md) if the device doesn’t have an installed app registered to handle the URL’s scheme, or if you haven’t declared the URL’s scheme in your `Info.plist` file; otherwise, [`true`](../../Swift/true.md).

#### Discussion

When this method returns [`true`](../../Swift/true.md), iOS guarantees subsequent calls to the [`open(_:options:completionHandler:)`](./open%28_,options,completionhandler%29.md) method with the same URL will successfully launch an app that can handle the URL. The return value doesn’t indicate the validity of the URL, whether the specified resource exists, or, in the case of a universal link, whether the device has an installed app registered to respond to the universal link.

You can call this method safely on a thread that isn’t the main thread.

> ❗ **Important**:  If you link your app on or after iOS 9.0, you must declare the URL schemes you pass to this method by adding the `LSApplicationQueriesSchemes` key to your app’s `Info.plist` file. This method always returns [`false`](../../Swift/false.md) for undeclared schemes, even if the device doesn’t have a registered app installed. Apps linked on or after iOS 15 are limited to a maximum of 50 entries in the `LSApplicationQueriesSchemes` key. Apps linked on or after iOS 27 are limited to a maximum of 25 entries in the `LSApplicationQueriesSchemes` key. To learn more about the key, see [LSApplicationQueriesSchemes](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/LaunchServicesKeys.html#//apple_ref/doc/plist/info/LSApplicationQueriesSchemes).

If you link your app against an earlier version of iOS but it is running in iOS 9.0 or later, you can call this method up to 50 times. After reaching that limit, subsequent calls always return [`false`](../../Swift/false.md). If the user reinstalls or upgrades the app, iOS resets the limit.

Unlike this method, the [`open(_:options:completionHandler:)`](./open%28_,options,completionhandler%29.md) method isn’t constrained by the `LSApplicationQueriesSchemes` requirement. If an app is available to handle the URL, the system will launch it, even if you haven’t declared the scheme.

Using universal links instead of custom URL schemes removes the need to use this method to validate target links; if no app is available to handle a universal link, iOS routes it to the person’s default browser, allowing the associated website to respond. For more information on universal links, see [Allowing apps and websites to link to your content](../../Xcode/allowing-apps-and-websites-to-link-to-your-content.md).

## Parameters

- `url`: A URL (Universal Resource Locator). At runtime, the system determines if the device has an installed app registered to handle the URL’s scheme. The device can have more than one app registered to handle a scheme.

  The URL can have a common scheme such as `http`, `https`, `tel`, or `facetime`, or a custom scheme. For information about supported schemes, see [Apple URL Scheme Reference](https://developer.apple.com/library/archive/featuredarticles/iPhoneURLScheme_Reference/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007899).

## See Also

### Related Documentation
- [func openURL(URL) -> Bool](./openurl%28_%29.md)
  Attempts to open the resource at the specified URL.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/canopenurl(_:))*