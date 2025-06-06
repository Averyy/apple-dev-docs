# isDateInToday(_:)

**Framework**: Foundation  
**Kind**: method

Returns a Boolean value indicating whether the given date is within today.

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
func isDateInToday(_ date: Date) -> Bool
```

#### Return Value

`true` if the given date is within today, as defined by the calendar and calendar’s locale; otherwise, `false`.

## Parameters

- `date`: The specified date.

## See Also

- [func compare(Date, to: Date, toGranularity: Calendar.Component) -> ComparisonResult](calendar/compare(_:to:togranularity:).md)
  Compares two dates down to the specified component.
- [func isDate(Date, equalTo: Date, toGranularity: Calendar.Component) -> Bool](calendar/isdate(_:equalto:togranularity:).md)
  Returns a Boolean value indicating whether two dates are equal down to the specified component.
- [func isDate(Date, inSameDayAs: Date) -> Bool](calendar/isdate(_:insamedayas:).md)
  Returns a Boolean value indicating whether a date is within the same day as another date.
- [func isDateInTomorrow(Date) -> Bool](calendar/isdateintomorrow(_:).md)
  Returns a Boolean value indicating whether the given date is within tomorrow.
- [func isDateInYesterday(Date) -> Bool](calendar/isdateinyesterday(_:).md)
  Returns a Boolean value indicating whether the given date is within yesterday.
- [func isDateInWeekend(Date) -> Bool](calendar/isdateinweekend(_:).md)
  Returns a Boolean value indicating whether the given date is within a weekend period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/isdateintoday(_:))*