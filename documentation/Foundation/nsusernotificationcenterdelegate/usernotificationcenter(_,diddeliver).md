# userNotificationCenter(_:didDeliver:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sent to the delegate when a notification delivery date has arrived.

**Availability**:
- macOS 10.8+ - Deprecated in 11.0

> **Deprecated**: All NSUserNotifications API should be replaced with UserNotifications.frameworks API

## Declaration

```swift
optional func userNotificationCenter(_ center: NSUserNotificationCenter, didDeliver notification: NSUserNotification)
```

```objc
- (void) userNotificationCenter:(NSUserNotificationCenter *) center didDeliverNotification:(NSUserNotification *) notification;
```

#### Discussion

This method is always called, regardless of your application state and even if you deliver the user notification yourself using [`deliver(_:)`](../nsusernotificationcenter/deliver%28_%29.md).

This delegate method is invoked before the [`userNotificationCenter(_:shouldPresent:)`](./usernotificationcenter%28_,shouldpresent%29.md) delegate method.

## Parameters

- `center`: The user notification center.
- `notification`: The user notification object.

## See Also

### User Notification Delivery Information
- [func userNotificationCenter(NSUserNotificationCenter, didActivate: NSUserNotification)](./usernotificationcenter%28_,didactivate%29.md)
  Sent to the delegate when a user clicks on a user notification presented by the user notification center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotificationcenterdelegate/usernotificationcenter(_:diddeliver:))*