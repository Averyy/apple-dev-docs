# isDate(_:inSameDayAs:)

**Framework**: Foundation  
**Kind**: method

Returns a Boolean value indicating whether a date is within the same day as another date.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func isDate(_ date1: Date, inSameDayAs date2: Date) -> Bool
```

#### Return Value

`true` if `date1` and `date2` are in the same day, as defined by the calendar and calendar’s locale; otherwise, `false`.

## Parameters

- `date1`: A date to check for containment.
- `date2`: A date to check for containment.

## See Also

- [func compare(Date, to: Date, toGranularity: Calendar.Component) -> ComparisonResult](calendar/compare(_:to:togranularity:).md)
  Compares two dates down to the specified component.
- [func isDate(Date, equalTo: Date, toGranularity: Calendar.Component) -> Bool](calendar/isdate(_:equalto:togranularity:).md)
  Returns a Boolean value indicating whether two dates are equal down to the specified component.
- [func isDateInToday(Date) -> Bool](calendar/isdateintoday(_:).md)
  Returns a Boolean value indicating whether the given date is within today.
- [func isDateInTomorrow(Date) -> Bool](calendar/isdateintomorrow(_:).md)
  Returns a Boolean value indicating whether the given date is within tomorrow.
- [func isDateInYesterday(Date) -> Bool](calendar/isdateinyesterday(_:).md)
  Returns a Boolean value indicating whether the given date is within yesterday.
- [func isDateInWeekend(Date) -> Bool](calendar/isdateinweekend(_:).md)
  Returns a Boolean value indicating whether the given date is within a weekend period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/isdate(_:insamedayas:))*