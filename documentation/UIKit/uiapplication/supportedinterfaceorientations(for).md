# supportedInterfaceOrientations(for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the default set of interface orientations to use for the view controllers in the specified window.

**Availability**:
- iOS 6.0+ - Deprecated in 27.0
- iPadOS 6.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use [`supportedInterfaceOrientations(for:)`](../uiwindowscenedelegate/supportedinterfaceorientations%28for%29.md) instead.

## Declaration

```swift
func supportedInterfaceOrientations(for window: UIWindow?) -> UIInterfaceOrientationMask
```

```objc
- (UIInterfaceOrientationMask) supportedInterfaceOrientationsForWindow:(UIWindow *) window;
```

#### Return Value

A bit mask specifying which orientations are supported. See [`UIInterfaceOrientationMask`](../uiinterfaceorientationmask.md) for valid bit-mask values. The value returned by this method must not be `0`.

#### Discussion

Starting in iOS 8, you should employ the [`UITraitCollection`](../uitraitcollection.md) and [`UITraitEnvironment`](../uitraitenvironment.md) APIs, and size class properties as used in those APIs, instead of using this method or otherwise writing your app in terms of interface orientation.

This method returns the default interface orientations for the app. These orientations are used only for view controllers that do not specify their own. If your app delegate implements the [`application(_:supportedInterfaceOrientationsFor:)`](../uiapplicationdelegate/application%28_,supportedinterfaceorientationsfor%29.md) method, the system does not call this method.

The default implementation of this method returns the app’s default set of supported interface orientations, as you define them in the [UISupportedInterfaceOrientations](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/iPhoneOSKeys.html#//apple_ref/doc/uid/TP40009252-SW10) key of the `Info.plist` file in your Xcode project. If the file does not contain that key, this method returns all interface orientations for the iPad idiom and returns all interface orientations except the portrait upside-down orientation for the iPhone idiom.

## Parameters

- `window`: The window whose default interface orientations you want to retrieve.

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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/supportedinterfaceorientations(for:))*