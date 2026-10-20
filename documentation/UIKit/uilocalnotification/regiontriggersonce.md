# regionTriggersOnce

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether crossing a geographic region boundary delivers only one notification.

**Availability**:
- iOS 8.0+ - Deprecated in 10.0
- iPadOS 8.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- watchOS 2.0+ - Deprecated in 3.0

## Declaration

```swift
var regionTriggersOnce: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL regionTriggersOnce;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), the user is notified only upon the first crossing the boundary of the target [`region`](./region.md). After the first crossing, the local notification is unscheduled. When the value of this property is [`false`](../../Swift/false.md), notifications are delivered with each boundary crossing. The default value of this property is [`true`](../../Swift/true.md).

The region object itself defines whether the notification is triggered when the user enters or exits the region.

## See Also

### Scheduling a local notification
- [var fireDate: Date?](./firedate.md)
  The date and time when the system should deliver the notification.
- [var timeZone: TimeZone?](./timezone.md)
  The time zone of the notification’s fire date.
- [var repeatInterval: NSCalendar.Unit](./repeatinterval.md)
  The calendar interval at which to reschedule the notification.
- [var repeatCalendar: Calendar?](./repeatcalendar.md)
  The calendar the system should refer to when it reschedules a repeating notification.
- [var region: CLRegion?](./region.md)
  The geographic region that triggers the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilocalnotification/regiontriggersonce)*