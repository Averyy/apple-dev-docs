# deliveredNotifications

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

An array of all user notifications delivered to the notification center.

**Availability**:
- macOS 10.8+ - Deprecated in 11.0

> **Deprecated**: All NSUserNotifications API should be replaced with UserNotifications.frameworks API

## Declaration

```swift
var deliveredNotifications: [NSUserNotification] { get }
```

```objc
@property (copy, readonly) NSArray<NSUserNotification *> * deliveredNotifications;
```

## Discussion

The number of notifications the user actually sees in the user interface may be less than the size of this array.

Note that these may or may not have been actually presented to the user. See the [`isPresented`](../nsusernotification/ispresented.md) property in the [`NSUserNotification`](../nsusernotification.md) class.

> **Note**:  A scheduled user notification that specifies a [`deliveryRepeatInterval`](../nsusernotification/deliveryrepeatinterval.md) remains in the [`scheduledNotifications`](./schedulednotifications.md) list, even though it has been delivered.  The item that goes into the `deliveredNotifications` list is a copy of the user notification item.

## See Also

### Managing the Delivered Notifications
- [func deliver(NSUserNotification)](./deliver%28_%29.md)
  Deliver the specified user notification.
- [func removeDeliveredNotification(NSUserNotification)](./removedeliverednotification%28_%29.md)
  Remove a delivered user notification from the user notification center.
- [func removeAllDeliveredNotifications()](./removealldeliverednotifications%28%29.md)
  Remove all delivered user notifications from the user notification center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotificationcenter/deliverednotifications)*