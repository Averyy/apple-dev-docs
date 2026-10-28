# scheduledNotifications

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Specifies an array of scheduled user notifications that have not yet been delivered.

**Availability**:
- macOS 10.8+ - Deprecated in 11.0

> **Deprecated**: All NSUserNotifications API should be replaced with UserNotifications.frameworks API

## Declaration

```swift
var scheduledNotifications: [NSUserNotification] { get set }
```

```objc
@property (copy) NSArray<NSUserNotification *> * scheduledNotifications;
```

## Discussion

Newly scheduled notifications are added to the end of the array. You may also bulk-schedule notifications by setting this array. Bulk setting new scheduled notifications unschedules existing notifications.

> **Note**:  The scheduled user notification could be changing to a delivered notification at the time you are calling this method. and if that case the user notification will still be delivered.

## See Also

### Managing the Scheduled Notification Queue
- [func scheduleNotification(NSUserNotification)](./schedulenotification%28_%29.md)
  Schedules the specified user notification.
- [func removeScheduledNotification(NSUserNotification)](./removeschedulednotification%28_%29.md)
  Removes the specified user notification for the scheduled notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotificationcenter/schedulednotifications)*