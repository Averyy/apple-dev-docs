# updateTimeZone(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Updates the trigger’s time zone.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func updateTimeZone(_ timeZone: TimeZone?) async throws
```

#### Discussion

See [`timeZone`](hmtimertrigger/timezone.md) for a description of how the time zone is interpreted.

## Parameters

- `timeZone`: The new time zone; may be  .
- `completion`: The block executed after the request is processed.

## See Also

- [init(name: String, fireDate: Date, timeZone: TimeZone?, recurrence: DateComponents?, recurrenceCalendar: Calendar?)](hmtimertrigger/init(name:firedate:timezone:recurrence:recurrencecalendar:).md)
  Initializes a timer trigger with specified timing information.
- [var timeZone: TimeZone?](hmtimertrigger/timezone.md)
  The timezone in which to evaluate the fire time.
- [var recurrenceCalendar: Calendar?](hmtimertrigger/recurrencecalendar.md)
  The calendar in which the recurrence value is evaluated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmtimertrigger/updatetimezone(_:completionhandler:))*