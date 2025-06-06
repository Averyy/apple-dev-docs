# actualDeliveryDate

**Framework**: Foundation  
**Kind**: property

The date this notification was actually delivered.

**Availability**:
- macOS 10.8+

## Declaration

```swift
var actualDeliveryDate: Date? { get }
```

#### Discussion

The notification center will set this value if a notification is put in the scheduled list and the delivery time arrives.

If the notification is delivered directly using the [`deliver(_:)`](nsusernotificationcenter/deliver(_:).md) method of the [`NSUserNotificationCenter`](nsusernotificationcenter.md) class, this value is set to the [`deliveryDate`](nsusernotification/deliverydate.md) value. If the [`deliveryDate`](nsusernotification/deliverydate.md) value `nil`  this value is set to the current date.

This value is used to sort the list of notifications in the user interface.

## See Also

- [var deliveryDate: Date?](nsusernotification/deliverydate.md)
  Specifies when the notification should be delivered.
- [var deliveryRepeatInterval: DateComponents?](nsusernotification/deliveryrepeatinterval.md)
  Specifies the date components that control how often a user notification is repeated.
- [var deliveryTimeZone: TimeZone?](nsusernotification/deliverytimezone.md)
  Specify the time zone to interpret the delivery date in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotification/actualdeliverydate)*