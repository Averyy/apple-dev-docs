# removeDeliveredNotification(_:)

**Framework**: Foundation  
**Kind**: method

Remove a delivered user notification from the user notification center.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func removeDeliveredNotification(_ notification: NSUserNotification)
```

#### Discussion

If the user notification is not in [`deliveredNotifications`](nsusernotificationcenter/deliverednotifications.md), nothing happens.

## Parameters

- `notification`: The user notification.

## See Also

- [func deliver(NSUserNotification)](nsusernotificationcenter/deliver(_:).md)
  Deliver the specified user notification.
- [var deliveredNotifications: [NSUserNotification]](nsusernotificationcenter/deliverednotifications.md)
  An array of all user notifications delivered to the notification center.
- [func removeAllDeliveredNotifications()](nsusernotificationcenter/removealldeliverednotifications.md)
  Remove all delivered user notifications from the user notification center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotificationcenter/removedeliverednotification(_:))*