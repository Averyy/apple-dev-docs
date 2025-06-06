# scheduledLocalNotifications

**Framework**: UIKit  
**Kind**: property

All currently scheduled local notifications.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var scheduledLocalNotifications: [UILocalNotification]? { get set }
```

#### Discussion

This property holds an array of [`UILocalNotification`](uilocalnotification.md) objects representing the current scheduled local notifications. Use this property to access the currently scheduled notifications, perhaps to cancel them. Assigning a new value to this property implicitly schedules all of the notifications in the new array.

This method may be faster than using [`scheduleLocalNotification(_:)`](uiapplication/schedulelocalnotification(_:).md) when scheduling a large number of notifications.

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
- [var isNetworkActivityIndicatorVisible: Bool](uiapplication/isnetworkactivityindicatorvisible.md)
  A Boolean value that turns an indicator of network activity on or off.
- [var isStatusBarHidden: Bool](uiapplication/isstatusbarhidden.md)
  A Boolean value that determines whether the status bar is hidden.
- [var keyWindow: UIWindow?](uiapplication/keywindow.md)
  The app’s key window.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/scheduledlocalnotifications)*