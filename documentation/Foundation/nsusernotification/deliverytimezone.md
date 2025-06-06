# deliveryTimeZone

**Framework**: Foundation  
**Kind**: property

Specify the time zone to interpret the delivery date in.

**Availability**:
- macOS 10.8+

## Declaration

```swift
var deliveryTimeZone: TimeZone? { get set }
```

#### Discussion

If this value is `nil` and the user switches time zones, the notification center will adjust the time of presentation to account for the time zone change.

If a notification should be delivered at a time in a specific time zone (regardless of whether the user switches time zones), set this value to the specific time zone, for example the current time zone.

## See Also

- [var deliveryDate: Date?](nsusernotification/deliverydate.md)
  Specifies when the notification should be delivered.
- [var actualDeliveryDate: Date?](nsusernotification/actualdeliverydate.md)
  The date this notification was actually delivered.
- [var deliveryRepeatInterval: DateComponents?](nsusernotification/deliveryrepeatinterval.md)
  Specifies the date components that control how often a user notification is repeated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotification/deliverytimezone)*