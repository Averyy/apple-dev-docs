# deliveryTimeZone

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Specify the time zone to interpret the delivery date in.

**Availability**:
- macOS 10.8+ - Deprecated in 11.0

> **Deprecated**: All NSUserNotifications API should be replaced with UserNotifications.frameworks API

## Declaration

```swift
var deliveryTimeZone: TimeZone? { get set }
```

```objc
@property (copy, nullable) NSTimeZone * deliveryTimeZone;
```

## Discussion

If this value is `nil` and the user switches time zones, the notification center will adjust the time of presentation to account for the time zone change.

If a notification should be delivered at a time in a specific time zone (regardless of whether the user switches time zones), set this value to the specific time zone, for example the current time zone.

## See Also

### Delivery Timing
- [var deliveryDate: Date?](./deliverydate.md)
  Specifies when the notification should be delivered.
- [var actualDeliveryDate: Date?](./actualdeliverydate.md)
  The date this notification was actually delivered.
- [var deliveryRepeatInterval: DateComponents?](./deliveryrepeatinterval.md)
  Specifies the date components that control how often a user notification is repeated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotification/deliverytimezone)*