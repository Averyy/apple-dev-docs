# actualDeliveryDate

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The date this notification was actually delivered.

**Availability**:
- macOS 10.8+ - Deprecated in 11.0

> **Deprecated**: All NSUserNotifications API should be replaced with UserNotifications.frameworks API

## Declaration

```swift
var actualDeliveryDate: Date? { get }
```

```objc
@property (copy, readonly, nullable) NSDate * actualDeliveryDate;
```

## Discussion

The notification center will set this value if a notification is put in the scheduled list and the delivery time arrives.

If the notification is delivered directly using the [`deliver(_:)`](../nsusernotificationcenter/deliver%28_%29.md) method of the [`NSUserNotificationCenter`](../nsusernotificationcenter.md) class, this value is set to the [`deliveryDate`](./deliverydate.md) value. If the [`deliveryDate`](./deliverydate.md) value `nil`  this value is set to the current date.

This value is used to sort the list of notifications in the user interface.

## See Also

### Delivery Timing
- [var deliveryDate: Date?](./deliverydate.md)
  Specifies when the notification should be delivered.
- [var deliveryRepeatInterval: DateComponents?](./deliveryrepeatinterval.md)
  Specifies the date components that control how often a user notification is repeated.
- [var deliveryTimeZone: TimeZone?](./deliverytimezone.md)
  Specify the time zone to interpret the delivery date in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotification/actualdeliverydate)*