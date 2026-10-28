# timeZone

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The time zone of the notification’s fire date.

**Availability**:
- iOS 4.0+ - Deprecated in 10.0
- iPadOS 4.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- watchOS 2.0+ - Deprecated in 3.0

> **Deprecated**: For more information, see [`UILocalNotification`](../uilocalnotification.md).

## Declaration

```swift
var timeZone: TimeZone? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSTimeZone * timeZone;
```

## Discussion

The date specified in [`fireDate`](./firedate.md) is interpreted according to the value of this property. If you specify `nil` (the default), the fire date is interpreted as an absolute GMT time, which is suitable for cases such as countdown timers. If you assign a valid [`NSTimeZone`](../../Foundation/nstimezone.md) object to this property, the fire date is interpreted as a wall-clock time that is automatically adjusted when there are changes in time zones; an example suitable for this case is an an alarm clock.

## See Also

### Scheduling a local notification
- [var fireDate: Date?](./firedate.md)
  The date and time when the system should deliver the notification.
- [var repeatInterval: NSCalendar.Unit](./repeatinterval.md)
  The calendar interval at which to reschedule the notification.
- [var repeatCalendar: Calendar?](./repeatcalendar.md)
  The calendar the system should refer to when it reschedules a repeating notification.
- [var region: CLRegion?](./region.md)
  The geographic region that triggers the notification.
- [var regionTriggersOnce: Bool](./regiontriggersonce.md)
  A Boolean value indicating whether crossing a geographic region boundary delivers only one notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilocalnotification/timezone)*