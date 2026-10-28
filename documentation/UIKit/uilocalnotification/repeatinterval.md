# repeatInterval

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The calendar interval at which to reschedule the notification.

**Availability**:
- iOS 4.0+ - Deprecated in 10.0
- iPadOS 4.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- watchOS 2.0+ - Deprecated in 3.0

> **Deprecated**: For more information, see [`UILocalNotification`](../uilocalnotification.md).

## Declaration

```swift
var repeatInterval: NSCalendar.Unit { get set }
```

```objc
@property (nonatomic) NSCalendarUnit repeatInterval;
```

## Discussion

If you assign a calendar unit such as weekly ([`weekOfYear`](../../Foundation/nscalendar/unit/weekofyear.md)) or yearly ([`year`](../../Foundation/nscalendar/unit/year.md)), the system reschedules the notification for delivery at the specified interval. Note that intervals of less than one minute are not supported. The default value is 0, which means that the system fires the notification once and then discards it.

## See Also

### Scheduling a local notification
- [var fireDate: Date?](./firedate.md)
  The date and time when the system should deliver the notification.
- [var timeZone: TimeZone?](./timezone.md)
  The time zone of the notification’s fire date.
- [var repeatCalendar: Calendar?](./repeatcalendar.md)
  The calendar the system should refer to when it reschedules a repeating notification.
- [var region: CLRegion?](./region.md)
  The geographic region that triggers the notification.
- [var regionTriggersOnce: Bool](./regiontriggersonce.md)
  A Boolean value indicating whether crossing a geographic region boundary delivers only one notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilocalnotification/repeatinterval)*