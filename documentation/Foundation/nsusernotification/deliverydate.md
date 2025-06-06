# deliveryDate

**Framework**: Foundation  
**Kind**: property

Specifies when the notification should be delivered.

**Availability**:
- macOS 10.8+

## Declaration

```swift
var deliveryDate: Date? { get set }
```

#### Discussion

The delivery date is specified in an absolute time.

After a notification is delivered, it may be presented to the user.

## See Also

- [var actualDeliveryDate: Date?](nsusernotification/actualdeliverydate.md)
  The date this notification was actually delivered.
- [var deliveryRepeatInterval: DateComponents?](nsusernotification/deliveryrepeatinterval.md)
  Specifies the date components that control how often a user notification is repeated.
- [var deliveryTimeZone: TimeZone?](nsusernotification/deliverytimezone.md)
  Specify the time zone to interpret the delivery date in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotification/deliverydate)*