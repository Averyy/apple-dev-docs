# isDateInWeekend(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Indicates whether a given date falls within a weekend period, as defined by the calendar and the calendar’s locale.

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
func isDateInWeekend(_ date: Date) -> Bool
```

```objc
- (BOOL) isDateInWeekend:(NSDate *) date;
```

## Return Value

[`true`](../../Swift/true.md) if the given date is within a weekend period, otherwise [`false`](../../Swift/false.md).

## Discussion

If the date does fall within a weekend, you can use the [`range(ofWeekendStart:interval:containing:)`](./range%28ofweekendstart,interval,containing%29.md) method to determine the start date of that weekend period. Otherwise, you can use the [`nextWeekendStart(_:interval:options:after:)`](./nextweekendstart%28_,interval,options,after%29.md) method to determine the start date of the next or previous weekend.

## Parameters

- `date`: The date for which to perform the calculation.

## See Also

### Comparing Dates
- [func compare(Date, to: Date, toUnitGranularity: NSCalendar.Unit) -> ComparisonResult](./compare%28_,to,tounitgranularity%29.md)
  Indicates the ordering of two given dates based on their components down to a given unit granularity.
- [func isDate(Date, equalTo: Date, toUnitGranularity: NSCalendar.Unit) -> Bool](./isdate%28_,equalto,tounitgranularity%29.md)
  Indicates whether two dates are equal to a given unit of granularity.
- [func isDate(Date, inSameDayAs: Date) -> Bool](./isdate%28_,insamedayas%29.md)
  Indicates whether two dates are in the same day.
- [func isDateInToday(Date) -> Bool](./isdateintoday%28_%29.md)
  Indicates whether the given date is in “today.”
- [func isDateInTomorrow(Date) -> Bool](./isdateintomorrow%28_%29.md)
  Indicates whether the given date is in “tomorrow.”
- [func isDateInYesterday(Date) -> Bool](./isdateinyesterday%28_%29.md)
  Indicates whether the given date is in “yesterday.”


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscalendar/isdateinweekend(_:))*