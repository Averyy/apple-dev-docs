# deliveredNotifications

**Framework**: Foundation  
**Kind**: property

An array of all user notifications delivered to the notification center.

**Availability**:
- macOS 10.8+

## Declaration

```swift
var deliveredNotifications: [NSUserNotification] { get }
```

#### Discussion

The number of notifications the user actually sees in the user interface may be less than the size of this array.

Note that these may or may not have been actually presented to the user. See the [`isPresented`](nsusernotification/ispresented.md) property in the [`NSUserNotification`](nsusernotification.md) class.

> **Note**:  A scheduled user notification that specifies a [`deliveryRepeatInterval`](nsusernotification/deliveryrepeatinterval.md) remains in the [`scheduledNotifications`](nsusernotificationcenter/schedulednotifications.md) list, even though it has been delivered.  The item that goes into the `deliveredNotifications` list is a copy of the user notification item.

## See Also

- [func deliver(NSUserNotification)](nsusernotificationcenter/deliver(_:).md)
  Deliver the specified user notification.
- [func removeDeliveredNotification(NSUserNotification)](nsusernotificationcenter/removedeliverednotification(_:).md)
  Remove a delivered user notification from the user notification center.
- [func removeAllDeliveredNotifications()](nsusernotificationcenter/removealldeliverednotifications.md)
  Remove all delivered user notifications from the user notification center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotificationcenter/deliverednotifications)*