# fireDate

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The date and time when the system should deliver the notification.

**Availability**:
- iOS 4.0+ - Deprecated in 10.0
- iPadOS 4.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- watchOS 2.0+ - Deprecated in 3.0

> **Deprecated**: For more information, see [`UILocalNotification`](../uilocalnotification.md).

## Declaration

```swift
var fireDate: Date? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSDate * fireDate;
```

#### Discussion

The fire date is interpreted according to the value specified in the [`timeZone`](./timezone.md) property. If the specified value is `nil` or is a date in the past, the notification is delivered immediately.

You may specify a value for this property or the [`region`](./region.md) property but not both. Attempting to schedule a local notification that contains both a region and fire date raises an exception.

## See Also

### Scheduling a local notification
- [var timeZone: TimeZone?](./timezone.md)
  The time zone of the notification’s fire date.
- [var repeatInterval: NSCalendar.Unit](./repeatinterval.md)
  The calendar interval at which to reschedule the notification.
- [var repeatCalendar: Calendar?](./repeatcalendar.md)
  The calendar the system should refer to when it reschedules a repeating notification.
- [var region: CLRegion?](./region.md)
  The geographic region that triggers the notification.
- [var regionTriggersOnce: Bool](./regiontriggersonce.md)
  A Boolean value indicating whether crossing a geographic region boundary delivers only one notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilocalnotification/firedate)*