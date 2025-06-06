# recurrenceCalendar

**Framework**: HomeKit  
**Kind**: property

The calendar in which the recurrence value is evaluated.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var recurrenceCalendar: Calendar? { get }
```

#### Discussion

See [`recurrence`](hmtimertrigger/recurrence.md) for a discussion of how the recurrence value and recurrence calendar are used.

## See Also

- [init(name: String, fireDate: Date, timeZone: TimeZone?, recurrence: DateComponents?, recurrenceCalendar: Calendar?)](hmtimertrigger/init(name:firedate:timezone:recurrence:recurrencecalendar:).md)
  Initializes a timer trigger with specified timing information.
- [var timeZone: TimeZone?](hmtimertrigger/timezone.md)
  The timezone in which to evaluate the fire time.
- [func updateTimeZone(TimeZone?, completionHandler: ((any Error)?) -> Void)](hmtimertrigger/updatetimezone(_:completionhandler:).md)
  Updates the trigger’s time zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmtimertrigger/recurrencecalendar)*