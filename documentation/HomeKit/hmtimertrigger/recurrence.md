# recurrence

**Framework**: HomeKit  
**Kind**: property

The interval on which to repeat firing the trigger.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var recurrence: DateComponents? { get }
```

#### Discussion

This value may be `nil` if the trigger should not repeat.

The next fire date is calculated by adding the date components to the last fire date, as evaluated in the context of the trigger’s [`recurrenceCalendar`](hmtimertrigger/recurrencecalendar.md). Depending on the calendar, some date components may result in an undefined next fire date.

The minimum recurrence interval is five minutes, and the most precision possible are whole minute values—you may not specify seconds in a recurrence interval. The maximum recurrence interval is five weeks.

## See Also

- [func updateRecurrence(DateComponents?, completionHandler: ((any Error)?) -> Void)](hmtimertrigger/updaterecurrence(_:completionhandler:).md)
  Updates the recurrence interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmtimertrigger/recurrence)*