# timeZone

**Framework**: Foundation  
**Kind**: property

A time zone.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var timeZone: TimeZone? { get set }
```

#### Discussion

> **Note**:  This value is interpreted in the context of the calendar in which it is used.

## See Also

- [init(calendar: Calendar?, timeZone: TimeZone?, era: Int?, year: Int?, month: Int?, day: Int?, hour: Int?, minute: Int?, second: Int?, nanosecond: Int?, weekday: Int?, weekdayOrdinal: Int?, quarter: Int?, weekOfMonth: Int?, weekOfYear: Int?, yearForWeekOfYear: Int?)](datecomponents/init(calendar:timezone:era:year:month:day:hour:minute:second:nanosecond:weekday:weekdayordinal:quarter:weekofmonth:weekofyear:yearforweekofyear:).md)
  Initializes a date components value, optionally specifying values for its fields.
- [var calendar: Calendar?](datecomponents/calendar.md)
  The calendar used to interpret the other values in this structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/datecomponents/timezone)*