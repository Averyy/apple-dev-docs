# compare(_:to:toUnitGranularity:)

**Framework**: Foundation  
**Kind**: method

Indicates the ordering of two given dates based on their components down to a given unit granularity.

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
func compare(_ date1: Date, to date2: Date, toUnitGranularity unit: NSCalendar.Unit) -> ComparisonResult
```

#### Return Value

`NSOrderedSame` if the dates are the same down to the given granularity, otherwise `NSOrderedAscending` or `NSOrderedDescending`.

## Parameters

- `date1`: The first date to compare.
- `date2`: The second date to compare.
- `unit`: The smallest unit that must, along with all larger units, be equal for the given dates to be considered the same. For possible values, see  .

## See Also

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
- [func isDateInYesterday(Date) -> Bool](nscalendar/isdateinyesterday(_:).md)
  Indicates whether the given date is in “yesterday.”


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscalendar/compare(_:to:tounitgranularity:))*