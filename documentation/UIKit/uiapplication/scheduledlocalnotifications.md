# scheduledLocalNotifications

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

All currently scheduled local notifications.

**Availability**:
- iOS 4.0+ - Deprecated in 10.0
- iPadOS 4.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use the [`UNUserNotificationCenter`](../../UserNotifications/unusernotificationcenter.md) class to schedule local notifications instead.

## Declaration

```swift
var scheduledLocalNotifications: [UILocalNotification]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSArray<UILocalNotification *> * scheduledLocalNotifications;
```

## Discussion

This property holds an array of [`UILocalNotification`](../uilocalnotification.md) objects representing the current scheduled local notifications. Use this property to access the currently scheduled notifications, perhaps to cancel them. Assigning a new value to this property implicitly schedules all of the notifications in the new array.

This method may be faster than using [`scheduleLocalNotification(_:)`](./schedulelocalnotification%28_%29.md) when scheduling a large number of notifications.

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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/scheduledlocalnotifications)*