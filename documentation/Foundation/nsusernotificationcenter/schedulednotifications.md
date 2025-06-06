# scheduledNotifications

**Framework**: Foundation  
**Kind**: property

Specifies an array of scheduled user notifications that have not yet been delivered.

**Availability**:
- macOS 10.8+

## Declaration

```swift
var scheduledNotifications: [NSUserNotification] { get set }
```

#### Discussion

Newly scheduled notifications are added to the end of the array. You may also bulk-schedule notifications by setting this array. Bulk setting new scheduled notifications unschedules existing notifications.

> **Note**:  The scheduled user notification could be changing to a delivered notification at the time you are calling this method. and if that case the user notification will still be delivered.

## See Also

- [func scheduleNotification(NSUserNotification)](nsusernotificationcenter/schedulenotification(_:).md)
  Schedules the specified user notification.
- [func removeScheduledNotification(NSUserNotification)](nsusernotificationcenter/removeschedulednotification(_:).md)
  Removes the specified user notification for the scheduled notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotificationcenter/schedulednotifications)*