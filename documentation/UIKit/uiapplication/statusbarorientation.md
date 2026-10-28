# statusBarOrientation

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The current orientation of the app’s status bar.

**Availability**:
- iOS 2.0+ - Deprecated in 13.0
- iPadOS 2.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use the [`interfaceOrientation`](../uiwindowscene/interfaceorientation.md) property of the window scene instead.

## Declaration

```swift
var statusBarOrientation: UIInterfaceOrientation { get set }
```

```objc
@property (nonatomic, readonly) UIInterfaceOrientation statusBarOrientation;
```

## Discussion

The value of this property is a constant that indicates an orientation of the status bar. See [`UIInterfaceOrientation`](../uiinterfaceorientation.md) for details. Setting this property rotates the status bar to the specified orientation without animating the transition. If your app has rotatable window content, however, you shouldn’t arbitrarily set status-bar orientation using this method. The status-bar orientation set by this method doesn’t change if the device changes orientation. For more on rotatable window views, see [View Controller Programming Guide for iOS](https://developer.apple.com/library/archive/featuredarticles/ViewControllerPGforiPhoneOS/index.html#//apple_ref/doc/uid/TP40007457).

## See Also

### Related Documentation
- [func setStatusBarOrientation(UIInterfaceOrientation, animated: Bool)](./setstatusbarorientation%28_,animated%29.md)
  Sets the app’s status bar to the specified orientation, optionally animating the transition.
### Deprecated properties
- [var applicationIconBadgeNumber: Int](./applicationiconbadgenumber.md)
  The number currently set as the badge of the app icon on the Home screen.
- [class let statusBarFrameUserInfoKey: String](./statusbarframeuserinfokey.md)
  A key whose value indicates the new status bar frame.
- [class let statusBarOrientationUserInfoKey: String](./statusbarorientationuserinfokey.md)
  A key whose value indicates the current interface orientation.
- [var currentUserNotificationSettings: UIUserNotificationSettings?](./currentusernotificationsettings.md)
  Returns the user notification settings for the app.
- [var isIgnoringInteractionEvents: Bool](./isignoringinteractionevents.md)
  A Boolean value that indicates whether the receiver is ignoring events initiated by touches on the screen.
- [var isNetworkActivityIndicatorVisible: Bool](./isnetworkactivityindicatorvisible.md)
  A Boolean value that turns an indicator of network activity on or off.
- [var isStatusBarHidden: Bool](./isstatusbarhidden.md)
  A Boolean value that determines whether the status bar is hidden.
- [var keyWindow: UIWindow?](./keywindow.md)
  The app’s key window.
- [var scheduledLocalNotifications: [UILocalNotification]?](./scheduledlocalnotifications.md)
  All currently scheduled local notifications.
- [var statusBarFrame: CGRect](./statusbarframe.md)
  The frame rectangle defining the area of the status bar.
- [var statusBarOrientationAnimationDuration: TimeInterval](./statusbarorientationanimationduration.md)
  The animation duration in seconds for the status bar during a 90 degree orientation change.
- [var statusBarStyle: UIStatusBarStyle](./statusbarstyle.md)
  The current style of the status bar.
- [var windows: [UIWindow]](./windows.md)
  The app’s visible and hidden windows.
- [proximitySensingEnabled](./proximitysensingenabled.md)
  A Boolean value that determines whether proximity sensing is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/statusbarorientation)*