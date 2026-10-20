# removeScheduledNotification(_:)

**Framework**: Foundation  
**Kind**: method

Removes the specified user notification for the scheduled notifications.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func removeScheduledNotification(_ notification: NSUserNotification)
```

#### Discussion

If the user notification’s [`deliveryDate`](nsusernotification/deliverydate.md) occurs before the cancellation finishes, the notification may still be delivered.

If the notification is not in the scheduled list, nothing happens.

## Parameters

- `notification`: The user notification.

## See Also

- [func scheduleNotification(NSUserNotification)](nsusernotificationcenter/schedulenotification(_:).md)
  Schedules the specified user notification.
- [var scheduledNotifications: [NSUserNotification]](nsusernotificationcenter/schedulednotifications.md)
  Specifies an array of scheduled user notifications that have not yet been delivered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotificationcenter/removeschedulednotification(_:))*