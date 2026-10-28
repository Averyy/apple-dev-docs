# recurrenceCalendar

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

The calendar in which the recurrence value is evaluated.

**Availability**:
- iOS 8.0+ - Deprecated in 16.4
- iPadOS 8.0+ - Deprecated in 16.4
- Mac Catalyst 8.0+ - Deprecated in 16.4
- tvOS 10.0+ - Deprecated in 16.4
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 9.4

> **Deprecated**: This property is no longer supported.

## Declaration

```swift
var recurrenceCalendar: Calendar? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSCalendar * recurrenceCalendar;
```

## Discussion

See [`recurrence`](./recurrence.md) for a discussion of how the recurrence value and recurrence calendar are used.

## See Also

### Deprecated symbols
- [init(name: String, fireDate: Date, timeZone: TimeZone?, recurrence: DateComponents?, recurrenceCalendar: Calendar?)](./init%28name,firedate,timezone,recurrence,recurrencecalendar%29.md)
  Initializes a timer trigger with specified timing information.
- [var timeZone: TimeZone?](./timezone.md)
  The timezone in which to evaluate the fire time.
- [func updateTimeZone(TimeZone?, completionHandler: ((any Error)?) -> Void)](./updatetimezone%28_,completionhandler%29.md)
  Updates the trigger’s time zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmtimertrigger/recurrencecalendar)*