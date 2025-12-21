# isDateInYesterday(_:)

**Framework**: Foundation  
**Kind**: method

Indicates whether the given date is in “yesterday.”

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func isDateInYesterday(_ date: Date) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the given date is in “yesterday,” otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `date`: The date for which to perform the calculation.

## See Also

- [func compare(Date, to: Date, toUnitGranularity: NSCalendar.Unit) -> ComparisonResult](nscalendar/compare(_:to:tounitgranularity:).md)
  Indicates the ordering of two given dates based on their components down to a given unit granularity.
- [func isDate(Date, equalTo: Date, toUnitGranularity: NSCalendar.Unit) -> Bool](nscalendar/isdate(_:equalto:tounitgranularity:).md)
  Indicates whether two dates are equal to a given unit of granularity.
- [func isDate(Date, inSameDayAs: Date) -> Bool](nscalendar/isdate(_:insamedayas:).md)
  Indicates whether two dates are in the same day.
- [func isDateInToday(Date) -> Bool](nscalendar/isdateintoday(_:).md)
  Indicates whether the given date is in “today.”
- [func isDateInTomorrow(Date) -> Bool](nscalendar/isdateintomorrow(_:).md)
  Indicates whether the given date is in “tomorrow.”
- [func isDateInWeekend(Date) -> Bool](nscalendar/isdateinweekend(_:).md)
  Indicates whether a given date falls within a weekend period, as defined by the calendar and the calendar’s locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscalendar/isdateinyesterday(_:))*