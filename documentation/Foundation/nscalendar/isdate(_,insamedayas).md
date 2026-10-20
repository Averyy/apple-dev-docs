# isDate(_:inSameDayAs:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Indicates whether two dates are in the same day.

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
func isDate(_ date1: Date, inSameDayAs date2: Date) -> Bool
```

```objc
- (BOOL) isDate:(NSDate *) date1 inSameDayAsDate:(NSDate *) date2;
```

#### Return Value

[`true`](../../Swift/true.md) if both dates are within the same day, otherwise [`false`](../../Swift/false.md).

## Parameters

- `date1`: The first date to compare.
- `date2`: The second date to compare.

## See Also

### Comparing Dates
- [func compare(Date, to: Date, toUnitGranularity: NSCalendar.Unit) -> ComparisonResult](./compare%28_,to,tounitgranularity%29.md)
  Indicates the ordering of two given dates based on their components down to a given unit granularity.
- [func isDate(Date, equalTo: Date, toUnitGranularity: NSCalendar.Unit) -> Bool](./isdate%28_,equalto,tounitgranularity%29.md)
  Indicates whether two dates are equal to a given unit of granularity.
- [func isDateInToday(Date) -> Bool](./isdateintoday%28_%29.md)
  Indicates whether the given date is in “today.”
- [func isDateInTomorrow(Date) -> Bool](./isdateintomorrow%28_%29.md)
  Indicates whether the given date is in “tomorrow.”
- [func isDateInWeekend(Date) -> Bool](./isdateinweekend%28_%29.md)
  Indicates whether a given date falls within a weekend period, as defined by the calendar and the calendar’s locale.
- [func isDateInYesterday(Date) -> Bool](./isdateinyesterday%28_%29.md)
  Indicates whether the given date is in “yesterday.”


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscalendar/isdate(_:insamedayas:))*