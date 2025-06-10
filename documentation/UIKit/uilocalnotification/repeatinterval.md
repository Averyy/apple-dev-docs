# repeatInterval

**Framework**: UIKit  
**Kind**: property

The calendar interval at which to reschedule the notification.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- watchOS 2.0+

## Declaration

```swift
@MainActor
var repeatInterval: NSCalendar.Unit { get set }
```

#### Discussion

If you assign a calendar unit such as weekly ([`weekOfYear`](https://developer.apple.com/documentation/Foundation/NSCalendar/Unit/weekOfYear)) or yearly ([`year`](https://developer.apple.com/documentation/Foundation/NSCalendar/Unit/year)), the system reschedules the notification for delivery at the specified interval. Note that intervals of less than one minute are not supported. The default value is 0, which means that the system fires the notification once and then discards it.

## See Also

- [var fireDate: Date?](uilocalnotification/firedate.md)
  The date and time when the system should deliver the notification.
- [var timeZone: TimeZone?](uilocalnotification/timezone.md)
  The time zone of the notification’s fire date.
- [var repeatCalendar: Calendar?](uilocalnotification/repeatcalendar.md)
  The calendar the system should refer to when it reschedules a repeating notification.
- [var region: CLRegion?](uilocalnotification/region.md)
  The geographic region that triggers the notification.
- [var regionTriggersOnce: Bool](uilocalnotification/regiontriggersonce.md)
  A Boolean value indicating whether crossing a geographic region boundary delivers only one notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilocalnotification/repeatinterval)*