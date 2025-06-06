# isDate(_:equalTo:toGranularity:)

**Framework**: Foundation  
**Kind**: method

Returns a Boolean value indicating whether two dates are equal down to the specified component.

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
func isDate(_ date1: Date, equalTo date2: Date, toGranularity component: Calendar.Component) -> Bool
```

#### Return Value

`true` if the two dates are equal in the given component and all larger components; otherwise, `false`.

## Parameters

- `date1`: A date to compare.
- `date2`: A date to compare.
- `component`: A granularity to compare. For example, pass   to check if two dates are in the same hour.

## See Also

- [func compare(Date, to: Date, toGranularity: Calendar.Component) -> ComparisonResult](calendar/compare(_:to:togranularity:).md)
  Compares two dates down to the specified component.
- [func isDate(Date, inSameDayAs: Date) -> Bool](calendar/isdate(_:insamedayas:).md)
  Returns a Boolean value indicating whether a date is within the same day as another date.
- [func isDateInToday(Date) -> Bool](calendar/isdateintoday(_:).md)
  Returns a Boolean value indicating whether the given date is within today.
- [func isDateInTomorrow(Date) -> Bool](calendar/isdateintomorrow(_:).md)
  Returns a Boolean value indicating whether the given date is within tomorrow.
- [func isDateInYesterday(Date) -> Bool](calendar/isdateinyesterday(_:).md)
  Returns a Boolean value indicating whether the given date is within yesterday.
- [func isDateInWeekend(Date) -> Bool](calendar/isdateinweekend(_:).md)
  Returns a Boolean value indicating whether the given date is within a weekend period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/isdate(_:equalto:togranularity:))*