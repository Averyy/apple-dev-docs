# deliver(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Deliver the specified user notification.

**Availability**:
- macOS 10.8+ - Deprecated in 11.0

> **Deprecated**: All NSUserNotifications API should be replaced with UserNotifications.frameworks API

## Declaration

```swift
func deliver(_ notification: NSUserNotification)
```

```objc
- (void) deliverNotification:(NSUserNotification *) notification;
```

## Discussion

The notification will be presented to the user (subject to the user’s preferences). The [`isPresented`](../nsusernotification/ispresented.md) property of the [`NSUserNotification`](../nsusernotification.md) object will always be set to [`true`](../../Swift/true.md) if a notification is delivered using this method.

## Parameters

- `notification`: The user notification.

## See Also

### Related Documentation
- [func removeScheduledNotification(NSUserNotification)](./removeschedulednotification%28_%29.md)
  Removes the specified user notification for the scheduled notifications.
### Managing the Delivered Notifications
- [var deliveredNotifications: [NSUserNotification]](./deliverednotifications.md)
  An array of all user notifications delivered to the notification center.
- [func removeDeliveredNotification(NSUserNotification)](./removedeliverednotification%28_%29.md)
  Remove a delivered user notification from the user notification center.
- [func removeAllDeliveredNotifications()](./removealldeliverednotifications%28%29.md)
  Remove all delivered user notifications from the user notification center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotificationcenter/deliver(_:))*