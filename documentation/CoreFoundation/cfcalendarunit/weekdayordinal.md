# weekdayOrdinal

**Framework**: Core Foundation  
**Kind**: property  
**Role**: Type Property

Specifies the ordinal weekday unit.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
static var weekdayOrdinal: CFCalendarUnit { get }
```

```c
kCFCalendarUnitWeekdayOrdinal
```

#### Discussion

The weekday ordinal unit describes ordinal position within the month unit of the corresponding weekday unit. For example, in the Gregorian calendar a weekday ordinal unit of `2` for a weekday unit `3` indicates “the second Tuesday in the month”.

## See Also

### Constants
- [static var era: CFCalendarUnit](./era.md)
  Specifies the era unit.
- [static var year: CFCalendarUnit](./year.md)
  Specifies the year unit.
- [static var month: CFCalendarUnit](./month.md)
  Specifies the month unit.
- [static var day: CFCalendarUnit](./day.md)
  Specifies the day unit.
- [static var hour: CFCalendarUnit](./hour.md)
  Specifies the hour unit.
- [static var minute: CFCalendarUnit](./minute.md)
  Specifies the minute unit.
- [static var second: CFCalendarUnit](./second.md)
  Specifies the second unit.
- [static var week: CFCalendarUnit](./week.md)
  Specifies the week unit.
- [static var weekday: CFCalendarUnit](./weekday.md)
  Specifies the weekday unit.
- [static var quarter: CFCalendarUnit](./quarter.md)
  Specifies the quarter-year unit.
- [static var weekOfMonth: CFCalendarUnit](./weekofmonth.md)
  Specifies the original week of a month calendar unit.
- [static var weekOfYear: CFCalendarUnit](./weekofyear.md)
  Specifies the original week of the year calendar unit.
- [static var yearForWeekOfYear: CFCalendarUnit](./yearforweekofyear.md)
  Specifies the relative year for a week within a year calendar unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcalendarunit/weekdayordinal)*