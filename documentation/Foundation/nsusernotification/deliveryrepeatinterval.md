# deliveryRepeatInterval

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Specifies the date components that control how often a user notification is repeated.

**Availability**:
- macOS 10.8+ - Deprecated in 11.0

> **Deprecated**: All NSUserNotifications API should be replaced with UserNotifications.frameworks API

## Declaration

```swift
var deliveryRepeatInterval: DateComponents? { get set }
```

```objc
@property (copy, nullable) NSDateComponents * deliveryRepeatInterval;
```

## Discussion

This value may be `nil` if the notification should not repeat.

The date component values are relative to the date the notification was delivered.

If the calendar value of the `deliveryRepeatInterval` is `nil`, the current calendar is used to calculate the repeat interval. For example, if a notification should repeat every hour, set the `hour` property of the `deliveryRepeatInterval` to `1`.

This value is ignored unless the user notification is scheduled with the [`NSUserNotificationCenter`](../nsusernotificationcenter.md) object.

## See Also

### Delivery Timing
- [var deliveryDate: Date?](./deliverydate.md)
  Specifies when the notification should be delivered.
- [var actualDeliveryDate: Date?](./actualdeliverydate.md)
  The date this notification was actually delivered.
- [var deliveryTimeZone: TimeZone?](./deliverytimezone.md)
  Specify the time zone to interpret the delivery date in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotification/deliveryrepeatinterval)*