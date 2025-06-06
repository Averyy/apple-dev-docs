# scheduleNotification(_:)

**Framework**: Foundation  
**Kind**: method

Schedules the specified user notification.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func scheduleNotification(_ notification: NSUserNotification)
```

#### Discussion

Scheduled notifications are added to the end of the notification queue.

## Parameters

- `notification`: The user notification.

## See Also

- [func deliver(NSUserNotification)](nsusernotificationcenter/deliver(_:).md)
  Deliver the specified user notification.
- [var scheduledNotifications: [NSUserNotification]](nsusernotificationcenter/schedulednotifications.md)
  Specifies an array of scheduled user notifications that have not yet been delivered.
- [func removeScheduledNotification(NSUserNotification)](nsusernotificationcenter/removeschedulednotification(_:).md)
  Removes the specified user notification for the scheduled notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotificationcenter/schedulenotification(_:))*