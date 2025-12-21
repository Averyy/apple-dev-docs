# deliver(_:)

**Framework**: Foundation  
**Kind**: method

Deliver the specified user notification.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func deliver(_ notification: NSUserNotification)
```

#### Discussion

The notification will be presented to the user (subject to the user’s preferences). The [`isPresented`](nsusernotification/ispresented.md) property of the [`NSUserNotification`](nsusernotification.md) object will always be set to [`true`](https://developer.apple.com/documentation/Swift/true) if a notification is delivered using this method.

## Parameters

- `notification`: The user notification.

## See Also

- [func removeScheduledNotification(NSUserNotification)](nsusernotificationcenter/removeschedulednotification(_:).md)
  Removes the specified user notification for the scheduled notifications.
- [var deliveredNotifications: [NSUserNotification]](nsusernotificationcenter/deliverednotifications.md)
  An array of all user notifications delivered to the notification center.
- [func removeDeliveredNotification(NSUserNotification)](nsusernotificationcenter/removedeliverednotification(_:).md)
  Remove a delivered user notification from the user notification center.
- [func removeAllDeliveredNotifications()](nsusernotificationcenter/removealldeliverednotifications.md)
  Remove all delivered user notifications from the user notification center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotificationcenter/deliver(_:))*