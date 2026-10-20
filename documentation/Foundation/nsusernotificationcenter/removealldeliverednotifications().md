# removeAllDeliveredNotifications()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Remove all delivered user notifications from the user notification center.

**Availability**:
- macOS 10.8+ - Deprecated in 11.0

> **Deprecated**: All NSUserNotifications API should be replaced with UserNotifications.frameworks API

## Declaration

```swift
func removeAllDeliveredNotifications()
```

```objc
- (void) removeAllDeliveredNotifications;
```

## See Also

### Managing the Delivered Notifications
- [func deliver(NSUserNotification)](./deliver%28_%29.md)
  Deliver the specified user notification.
- [var deliveredNotifications: [NSUserNotification]](./deliverednotifications.md)
  An array of all user notifications delivered to the notification center.
- [func removeDeliveredNotification(NSUserNotification)](./removedeliverednotification%28_%29.md)
  Remove a delivered user notification from the user notification center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotificationcenter/removealldeliverednotifications())*