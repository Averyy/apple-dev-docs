# proximitySensingEnabled

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether proximity sensing is enabled.

**Availability**:
- iOS 2.0+ - Deprecated in 3.0
- iPadOS 2.0+ - Deprecated in 3.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use the [`isProximityMonitoringEnabled`](../uidevice/isproximitymonitoringenabled.md) and [`proximityState`](../uidevice/proximitystate.md) properties of the [`UIDevice`](../uidevice.md) class instead.

## Declaration

```objc
@property (nonatomic, getter=isProximitySensingEnabled) BOOL proximitySensingEnabled;
```

## Discussion

[`true`](../../Swift/true.md) if proximity sensing is enabled; otherwise [`false`](../../Swift/false.md). Enabling proximity sensing tells iOS that it may need to blank the screen if the user’s face is near it. Proximity sensing is disabled by default.

## See Also

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
- [var statusBarOrientation: UIInterfaceOrientation](./statusbarorientation.md)
  The current orientation of the app’s status bar.
- [var statusBarOrientationAnimationDuration: TimeInterval](./statusbarorientationanimationduration.md)
  The animation duration in seconds for the status bar during a 90 degree orientation change.
- [var statusBarStyle: UIStatusBarStyle](./statusbarstyle.md)
  The current style of the status bar.
- [var windows: [UIWindow]](./windows.md)
  The app’s visible and hidden windows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/proximitysensingenabled)*