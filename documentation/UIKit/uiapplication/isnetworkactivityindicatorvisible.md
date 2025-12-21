# isNetworkActivityIndicatorVisible

**Framework**: UIKit  
**Kind**: property

A Boolean value that turns an indicator of network activity on or off.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var isNetworkActivityIndicatorVisible: Bool { get set }
```

#### Discussion

Specify [`true`](https://developer.apple.com/documentation/Swift/true) if the app should show network activity and [`false`](https://developer.apple.com/documentation/Swift/false) if it should not. The default value is [`false`](https://developer.apple.com/documentation/Swift/false). A spinning indicator in the status bar shows network activity. The app may explicitly hide or show this indicator.

## See Also

- [var applicationIconBadgeNumber: Int](uiapplication/applicationiconbadgenumber.md)
  The number currently set as the badge of the app icon on the Home screen.
- [class let statusBarFrameUserInfoKey: String](uiapplication/statusbarframeuserinfokey.md)
  A key whose value indicates the new status bar frame.
- [class let statusBarOrientationUserInfoKey: String](uiapplication/statusbarorientationuserinfokey.md)
  A key whose value indicates the current interface orientation.
- [var currentUserNotificationSettings: UIUserNotificationSettings?](uiapplication/currentusernotificationsettings.md)
  Returns the user notification settings for the app.
- [var isIgnoringInteractionEvents: Bool](uiapplication/isignoringinteractionevents.md)
  A Boolean value that indicates whether the receiver is ignoring events initiated by touches on the screen.
- [var isStatusBarHidden: Bool](uiapplication/isstatusbarhidden.md)
  A Boolean value that determines whether the status bar is hidden.
- [var keyWindow: UIWindow?](uiapplication/keywindow.md)
  The app’s key window.
- [var scheduledLocalNotifications: [UILocalNotification]?](uiapplication/scheduledlocalnotifications.md)
  All currently scheduled local notifications.
- [var statusBarFrame: CGRect](uiapplication/statusbarframe.md)
  The frame rectangle defining the area of the status bar.
- [var statusBarOrientation: UIInterfaceOrientation](uiapplication/statusbarorientation.md)
  The current orientation of the app’s status bar.
- [var statusBarOrientationAnimationDuration: TimeInterval](uiapplication/statusbarorientationanimationduration.md)
  The animation duration in seconds for the status bar during a 90 degree orientation change.
- [var statusBarStyle: UIStatusBarStyle](uiapplication/statusbarstyle.md)
  The current style of the status bar.
- [var windows: [UIWindow]](uiapplication/windows.md)
  The app’s visible and hidden windows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/isnetworkactivityindicatorvisible)*