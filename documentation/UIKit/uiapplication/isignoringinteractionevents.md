# isIgnoringInteractionEvents

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the receiver is ignoring events initiated by touches on the screen.

**Availability**:
- iOS 2.0+ - Deprecated in 13.0
- iPadOS 2.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS - Deprecated in 13.0

> **Deprecated**: Use [`isUserInteractionEnabled`](../uiview/isuserinteractionenabled.md) instead.

## Declaration

```swift
var isIgnoringInteractionEvents: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isIgnoringInteractionEvents) BOOL ignoringInteractionEvents;
```

## Discussion

The value of this property is

[`true`](../../Swift/true.md) if the receiver is ignoring interaction events and if the nested [`beginIgnoringInteractionEvents()`](./beginignoringinteractionevents%28%29.md) and [`endIgnoringInteractionEvents()`](./endignoringinteractionevents%28%29.md) calls are at least one level deep; otherwise, [`false`](../../Swift/false.md).

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
- [proximitySensingEnabled](./proximitysensingenabled.md)
  A Boolean value that determines whether proximity sensing is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/isignoringinteractionevents)*