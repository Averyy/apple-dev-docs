# repeatCalendar

**Framework**: UIKit  
**Kind**: property

The calendar the system should refer to when it reschedules a repeating notification.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- watchOS 2.0+

## Declaration

```swift
@MainActor
var repeatCalendar: Calendar? { get set }
```

#### Discussion

The default value is `nil`, which indicates that the current user calendar is used. (The current user calendar is returned by the [`current`](https://developer.apple.com/documentation/Foundation/NSCalendar/current) class method of `NSCalendar`.)

## See Also

- [var fireDate: Date?](uilocalnotification/firedate.md)
  The date and time when the system should deliver the notification.
- [var timeZone: TimeZone?](uilocalnotification/timezone.md)
  The time zone of the notification’s fire date.
- [var repeatInterval: NSCalendar.Unit](uilocalnotification/repeatinterval.md)
  The calendar interval at which to reschedule the notification.
- [var region: CLRegion?](uilocalnotification/region.md)
  The geographic region that triggers the notification.
- [var regionTriggersOnce: Bool](uilocalnotification/regiontriggersonce.md)
  A Boolean value indicating whether crossing a geographic region boundary delivers only one notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilocalnotification/repeatcalendar)*