# isDate(_:equalTo:toUnitGranularity:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Indicates whether two dates are equal to a given unit of granularity.

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
func isDate(_ date1: Date, equalTo date2: Date, toUnitGranularity unit: NSCalendar.Unit) -> Bool
```

```objc
- (BOOL) isDate:(NSDate *) date1 equalToDate:(NSDate *) date2 toUnitGranularity:(NSCalendarUnit) unit;
```

## Return Value

[`true`](../../Swift/true.md) if both dates have equal date component for all units greater than or equal to the given unit, otherwise [`false`](../../Swift/false.md).

## Parameters

- `date1`: The first date to compare.
- `date2`: The second date to compare.
- `unit`: The smallest unit that must, along with all larger units, be equal in the given dates. For possible values, see [`NSCalendar.Unit`](./unit.md).

## See Also

### Comparing Dates
- [func compare(Date, to: Date, toUnitGranularity: NSCalendar.Unit) -> ComparisonResult](./compare%28_,to,tounitgranularity%29.md)
  Indicates the ordering of two given dates based on their components down to a given unit granularity.
- [func isDate(Date, inSameDayAs: Date) -> Bool](./isdate%28_,insamedayas%29.md)
  Indicates whether two dates are in the same day.
- [func isDateInToday(Date) -> Bool](./isdateintoday%28_%29.md)
  Indicates whether the given date is in “today.”
- [func isDateInTomorrow(Date) -> Bool](./isdateintomorrow%28_%29.md)
  Indicates whether the given date is in “tomorrow.”
- [func isDateInWeekend(Date) -> Bool](./isdateinweekend%28_%29.md)
  Indicates whether a given date falls within a weekend period, as defined by the calendar and the calendar’s locale.
- [func isDateInYesterday(Date) -> Bool](./isdateinyesterday%28_%29.md)
  Indicates whether the given date is in “yesterday.”


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscalendar/isdate(_:equalto:tounitgranularity:))*