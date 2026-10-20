# isDateInTomorrow(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value indicating whether the given date is within tomorrow.

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
func isDateInTomorrow(_ date: Date) -> Bool
```

#### Return Value

`true` if the given date is within tomorrow, as defined by the calendar and calendar’s locale; otherwise, `false`.

## Parameters

- `date`: The specified date.

## See Also

### Comparing Dates
- [func compare(Date, to: Date, toGranularity: Calendar.Component) -> ComparisonResult](./compare%28_,to,togranularity%29.md)
  Compares two dates down to the specified component.
- [func isDate(Date, equalTo: Date, toGranularity: Calendar.Component) -> Bool](./isdate%28_,equalto,togranularity%29.md)
  Returns a Boolean value indicating whether two dates are equal down to the specified component.
- [func isDate(Date, inSameDayAs: Date) -> Bool](./isdate%28_,insamedayas%29.md)
  Returns a Boolean value indicating whether a date is within the same day as another date.
- [func isDateInToday(Date) -> Bool](./isdateintoday%28_%29.md)
  Returns a Boolean value indicating whether the given date is within today.
- [func isDateInYesterday(Date) -> Bool](./isdateinyesterday%28_%29.md)
  Returns a Boolean value indicating whether the given date is within yesterday.
- [func isDateInWeekend(Date) -> Bool](./isdateinweekend%28_%29.md)
  Returns a Boolean value indicating whether the given date is within a weekend period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/isdateintomorrow(_:))*