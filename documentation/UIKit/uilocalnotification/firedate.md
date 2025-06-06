# fireDate

**Framework**: UIKit  
**Kind**: property

The date and time when the system should deliver the notification.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- watchOS 2.0+

## Declaration

```swift
@MainActor
var fireDate: Date? { get set }
```

#### Discussion

The fire date is interpreted according to the value specified in the [`timeZone`](uilocalnotification/timezone.md) property. If the specified value is `nil` or is a date in the past, the notification is delivered immediately.

You may specify a value for this property or the [`region`](uilocalnotification/region.md) property but not both. Attempting to schedule a local notification that contains both a region and fire date raises an exception.

## See Also

- [var timeZone: TimeZone?](uilocalnotification/timezone.md)
  The time zone of the notification’s fire date.
- [var repeatInterval: NSCalendar.Unit](uilocalnotification/repeatinterval.md)
  The calendar interval at which to reschedule the notification.
- [var repeatCalendar: Calendar?](uilocalnotification/repeatcalendar.md)
  The calendar the system should refer to when it reschedules a repeating notification.
- [var region: CLRegion?](uilocalnotification/region.md)
  The geographic region that triggers the notification.
- [var regionTriggersOnce: Bool](uilocalnotification/regiontriggersonce.md)
  A Boolean value indicating whether crossing a geographic region boundary delivers only one notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilocalnotification/firedate)*