# timeZone

**Framework**: HomeKit  
**Kind**: property

The timezone in which to evaluate the fire time.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var timeZone: TimeZone? { get }
```

#### Discussion

If this value is `nil`, the trigger’s fire time will stay at the same relative time if the user changes timezones. If this value is set to a specific value, the trigger’s fire time will always be the same absolute time as evaluated in that time zone. A common value to set this to is the time zone where the accessories are physically located. This will result in the trigger firing at a specific time of day in that location, regardless of where the iOS device is located.

## See Also

- [init(name: String, fireDate: Date, timeZone: TimeZone?, recurrence: DateComponents?, recurrenceCalendar: Calendar?)](hmtimertrigger/init(name:firedate:timezone:recurrence:recurrencecalendar:).md)
  Initializes a timer trigger with specified timing information.
- [func updateTimeZone(TimeZone?, completionHandler: ((any Error)?) -> Void)](hmtimertrigger/updatetimezone(_:completionhandler:).md)
  Updates the trigger’s time zone.
- [var recurrenceCalendar: Calendar?](hmtimertrigger/recurrencecalendar.md)
  The calendar in which the recurrence value is evaluated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmtimertrigger/timezone)*