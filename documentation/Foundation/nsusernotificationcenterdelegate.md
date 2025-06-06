# NSUserNotificationCenterDelegate

**Framework**: Foundation  
**Kind**: protocol

An interface that enables customizing the behavior of the default notification center.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
protocol NSUserNotificationCenterDelegate : NSObjectProtocol
```

## Topics

### User Notification Delivery Information
- [func userNotificationCenter(NSUserNotificationCenter, didDeliver: NSUserNotification)](nsusernotificationcenterdelegate/usernotificationcenter(_:diddeliver:).md)
  Sent to the delegate when a notification delivery date has arrived.
- [func userNotificationCenter(NSUserNotificationCenter, didActivate: NSUserNotification)](nsusernotificationcenterdelegate/usernotificationcenter(_:didactivate:).md)
  Sent to the delegate when a user clicks on a user notification presented by the user notification center.
### User Notification Display Override
- [func userNotificationCenter(NSUserNotificationCenter, shouldPresent: NSUserNotification) -> Bool](nsusernotificationcenterdelegate/usernotificationcenter(_:shouldpresent:).md)
  Sent to the delegate when the user notification center has decided not to present your notification.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSUserNotification](nsusernotification.md)
  A notification that can be scheduled for display in the notification center.
- [class NSUserNotificationAction](nsusernotificationaction.md)
  An action that the user can take in response to receiving a notification.
- [class NSUserNotificationCenter](nsusernotificationcenter.md)
  An object that delivers notifications from apps to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotificationcenterdelegate)*