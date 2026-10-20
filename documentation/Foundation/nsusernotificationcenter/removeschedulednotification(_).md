# removeScheduledNotification(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Removes the specified user notification for the scheduled notifications.

**Availability**:
- macOS 10.8+ - Deprecated in 11.0

> **Deprecated**: All NSUserNotifications API should be replaced with UserNotifications.frameworks API

## Declaration

```swift
func removeScheduledNotification(_ notification: NSUserNotification)
```

```objc
- (void) removeScheduledNotification:(NSUserNotification *) notification;
```

#### Discussion

If the user notification’s [`deliveryDate`](../nsusernotification/deliverydate.md) occurs before the cancellation finishes, the notification may still be delivered.

If the notification is not in the scheduled list, nothing happens.

## Parameters

- `notification`: The user notification.

## See Also

### Managing the Scheduled Notification Queue
- [func scheduleNotification(NSUserNotification)](./schedulenotification%28_%29.md)
  Schedules the specified user notification.
- [var scheduledNotifications: [NSUserNotification]](./schedulednotifications.md)
  Specifies an array of scheduled user notifications that have not yet been delivered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotificationcenter/removeschedulednotification(_:))*