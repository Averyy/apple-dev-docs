# deliveryRepeatInterval

**Framework**: Foundation  
**Kind**: property

Specifies the date components that control how often a user notification is repeated.

**Availability**:
- macOS 10.8+

## Declaration

```swift
var deliveryRepeatInterval: DateComponents? { get set }
```

#### Discussion

This value may be `nil` if the notification should not repeat.

The date component values are relative to the date the notification was delivered.

If the calendar value of the `deliveryRepeatInterval` is `nil`, the current calendar is used to calculate the repeat interval. For example, if a notification should repeat every hour, set the `hour` property of the `deliveryRepeatInterval` to `1`.

This value is ignored unless the user notification is scheduled with the [`NSUserNotificationCenter`](nsusernotificationcenter.md) object.

## See Also

- [var deliveryDate: Date?](nsusernotification/deliverydate.md)
  Specifies when the notification should be delivered.
- [var actualDeliveryDate: Date?](nsusernotification/actualdeliverydate.md)
  The date this notification was actually delivered.
- [var deliveryTimeZone: TimeZone?](nsusernotification/deliverytimezone.md)
  Specify the time zone to interpret the delivery date in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotification/deliveryrepeatinterval)*