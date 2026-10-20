# scheduleNotification(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Schedules the specified user notification.

**Availability**:
- macOS 10.8+ - Deprecated in 11.0

> **Deprecated**: All NSUserNotifications API should be replaced with UserNotifications.frameworks API

## Declaration

```swift
func scheduleNotification(_ notification: NSUserNotification)
```

```objc
- (void) scheduleNotification:(NSUserNotification *) notification;
```

#### Discussion

Scheduled notifications are added to the end of the notification queue.

## Parameters

- `notification`: The user notification.

## See Also

### Related Documentation
- [func deliver(NSUserNotification)](./deliver%28_%29.md)
  Deliver the specified user notification.
### Managing the Scheduled Notification Queue
- [var scheduledNotifications: [NSUserNotification]](./schedulednotifications.md)
  Specifies an array of scheduled user notifications that have not yet been delivered.
- [func removeScheduledNotification(NSUserNotification)](./removeschedulednotification%28_%29.md)
  Removes the specified user notification for the scheduled notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotificationcenter/schedulenotification(_:))*