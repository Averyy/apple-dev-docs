# deliveryDate

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Specifies when the notification should be delivered.

**Availability**:
- macOS 10.8+ - Deprecated in 11.0

> **Deprecated**: All NSUserNotifications API should be replaced with UserNotifications.frameworks API

## Declaration

```swift
var deliveryDate: Date? { get set }
```

```objc
@property (copy, nullable) NSDate * deliveryDate;
```

#### Discussion

The delivery date is specified in an absolute time.

After a notification is delivered, it may be presented to the user.

## See Also

### Delivery Timing
- [var actualDeliveryDate: Date?](./actualdeliverydate.md)
  The date this notification was actually delivered.
- [var deliveryRepeatInterval: DateComponents?](./deliveryrepeatinterval.md)
  Specifies the date components that control how often a user notification is repeated.
- [var deliveryTimeZone: TimeZone?](./deliverytimezone.md)
  Specify the time zone to interpret the delivery date in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotification/deliverydate)*