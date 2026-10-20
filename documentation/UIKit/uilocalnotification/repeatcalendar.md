# repeatCalendar

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The calendar the system should refer to when it reschedules a repeating notification.

**Availability**:
- iOS 4.0+ - Deprecated in 10.0
- iPadOS 4.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- watchOS 2.0+ - Deprecated in 3.0

> **Deprecated**: For more information, see [`UILocalNotification`](../uilocalnotification.md).

## Declaration

```swift
var repeatCalendar: Calendar? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSCalendar * repeatCalendar;
```

#### Discussion

The default value is `nil`, which indicates that the current user calendar is used. (The current user calendar is returned by the [`current`](../../Foundation/nscalendar/current.md) class method of `NSCalendar`.)

## See Also

### Scheduling a local notification
- [var fireDate: Date?](./firedate.md)
  The date and time when the system should deliver the notification.
- [var timeZone: TimeZone?](./timezone.md)
  The time zone of the notification’s fire date.
- [var repeatInterval: NSCalendar.Unit](./repeatinterval.md)
  The calendar interval at which to reschedule the notification.
- [var region: CLRegion?](./region.md)
  The geographic region that triggers the notification.
- [var regionTriggersOnce: Bool](./regiontriggersonce.md)
  A Boolean value indicating whether crossing a geographic region boundary delivers only one notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilocalnotification/repeatcalendar)*