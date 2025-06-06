# regionTriggersOnce

**Framework**: UIKit  
**Kind**: property

A Boolean value indicating whether crossing a geographic region boundary delivers only one notification.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- watchOS 2.0+

## Declaration

```swift
@MainActor
var regionTriggersOnce: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the user is notified only upon the first crossing the boundary of the target [`region`](uilocalnotification/region.md). After the first crossing, the local notification is unscheduled. When the value of this property is [`false`](https://developer.apple.com/documentation/swift/false), notifications are delivered with each boundary crossing. The default value of this property is [`true`](https://developer.apple.com/documentation/swift/true).

The region object itself defines whether the notification is triggered when the user enters or exits the region.

## See Also

- [var fireDate: Date?](uilocalnotification/firedate.md)
  The date and time when the system should deliver the notification.
- [var timeZone: TimeZone?](uilocalnotification/timezone.md)
  The time zone of the notification’s fire date.
- [var repeatInterval: NSCalendar.Unit](uilocalnotification/repeatinterval.md)
  The calendar interval at which to reschedule the notification.
- [var repeatCalendar: Calendar?](uilocalnotification/repeatcalendar.md)
  The calendar the system should refer to when it reschedules a repeating notification.
- [var region: CLRegion?](uilocalnotification/region.md)
  The geographic region that triggers the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilocalnotification/regiontriggersonce)*