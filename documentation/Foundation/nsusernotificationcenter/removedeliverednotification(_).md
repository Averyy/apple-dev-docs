# removeDeliveredNotification(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Remove a delivered user notification from the user notification center.

**Availability**:
- macOS 10.8+ - Deprecated in 11.0

> **Deprecated**: All NSUserNotifications API should be replaced with UserNotifications.frameworks API

## Declaration

```swift
func removeDeliveredNotification(_ notification: NSUserNotification)
```

```objc
- (void) removeDeliveredNotification:(NSUserNotification *) notification;
```

## Discussion

If the user notification is not in [`deliveredNotifications`](./deliverednotifications.md), nothing happens.

## Parameters

- `notification`: The user notification.

## See Also

### Managing the Delivered Notifications
- [func deliver(NSUserNotification)](./deliver%28_%29.md)
  Deliver the specified user notification.
- [var deliveredNotifications: [NSUserNotification]](./deliverednotifications.md)
  An array of all user notifications delivered to the notification center.
- [func removeAllDeliveredNotifications()](./removealldeliverednotifications%28%29.md)
  Remove all delivered user notifications from the user notification center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotificationcenter/removedeliverednotification(_:))*