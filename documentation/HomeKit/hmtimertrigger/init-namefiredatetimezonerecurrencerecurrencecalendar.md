# init(name:fireDate:timeZone:recurrence:recurrenceCalendar:)

**Framework**: HomeKit  
**Kind**: init

Initializes a timer trigger with specified timing information.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(name: String, fireDate: Date, timeZone: TimeZone?, recurrence: DateComponents?, recurrenceCalendar: Calendar?)
```

#### Return Value

A newly-initialized timer trigger with the specified values.

#### Discussion

A new timer trigger starts out disabled, and must be enabled using [`enable(_:completionHandler:)`](hmtrigger/enable(_:completionhandler:).md) before use.

## Parameters

- `name`: The name of the timer trigger.
- `fireDate`: The first fire date.
- `timeZone`: The time zone for the first fire date. Pass   to use the default time zone. See   for a description of how the time zone is interpreted.
- `recurrence`: The recurrence interval on which to fire the trigger.   indicates a one-time trigger.
- `recurrenceCalendar`: The calendar in which to evaluate the recurrence interval of a timer trigger. May be  , in which case the current calendar   is used.

## See Also

- [var timeZone: TimeZone?](hmtimertrigger/timezone.md)
  The timezone in which to evaluate the fire time.
- [func updateTimeZone(TimeZone?, completionHandler: ((any Error)?) -> Void)](hmtimertrigger/updatetimezone(_:completionhandler:).md)
  Updates the trigger’s time zone.
- [var recurrenceCalendar: Calendar?](hmtimertrigger/recurrencecalendar.md)
  The calendar in which the recurrence value is evaluated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmtimertrigger/init(name:firedate:timezone:recurrence:recurrencecalendar:))*