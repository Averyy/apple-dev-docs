# applicationIconBadgeNumber

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The number currently set as the badge of the app icon on the Home screen.

**Availability**:
- iOS 2.0+ - Deprecated in 17.0
- iPadOS 2.0+ - Deprecated in 17.0
- Mac Catalyst 13.1+ - Deprecated in 17.0
- tvOS - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`setBadgeCount(_:withCompletionHandler:)`](../../UserNotifications/unusernotificationcenter/setbadgecount%28_,withcompletionhandler%29.md) instead.

## Declaration

```swift
var applicationIconBadgeNumber: Int { get set }
```

```objc
@property (nonatomic) NSInteger applicationIconBadgeNumber;
```

## Discussion

Set to 0 (zero) to hide the badge number. The default value of this property is 0.

## See Also

### Deprecated properties
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
- [proximitySensingEnabled](./proximitysensingenabled.md)
  A Boolean value that determines whether proximity sensing is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/applicationiconbadgenumber)*