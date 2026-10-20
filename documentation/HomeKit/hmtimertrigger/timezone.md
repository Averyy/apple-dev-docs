# timeZone

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

The timezone in which to evaluate the fire time.

**Availability**:
- iOS 8.0+ - Deprecated in 16.4
- iPadOS 8.0+ - Deprecated in 16.4
- Mac Catalyst 8.0+ - Deprecated in 16.4
- tvOS 10.0+ - Deprecated in 16.4
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 9.4

> **Deprecated**: Use [`HMEventTrigger`](../hmeventtrigger.md) with [`HMCalendarEvent`](../hmcalendarevent.md) for triggers based on a time-zone-relative time of day.

## Declaration

```swift
var timeZone: TimeZone? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSTimeZone * timeZone;
```

#### Discussion

If this value is `nil`, the trigger’s fire time will stay at the same relative time if the user changes timezones. If this value is set to a specific value, the trigger’s fire time will always be the same absolute time as evaluated in that time zone. A common value to set this to is the time zone where the accessories are physically located. This will result in the trigger firing at a specific time of day in that location, regardless of where the iOS device is located.

## See Also

### Deprecated symbols
- [init(name: String, fireDate: Date, timeZone: TimeZone?, recurrence: DateComponents?, recurrenceCalendar: Calendar?)](./init%28name,firedate,timezone,recurrence,recurrencecalendar%29.md)
  Initializes a timer trigger with specified timing information.
- [func updateTimeZone(TimeZone?, completionHandler: ((any Error)?) -> Void)](./updatetimezone%28_,completionhandler%29.md)
  Updates the trigger’s time zone.
- [var recurrenceCalendar: Calendar?](./recurrencecalendar.md)
  The calendar in which the recurrence value is evaluated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmtimertrigger/timezone)*