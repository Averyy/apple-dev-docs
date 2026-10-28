# weekdayOrdinal

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Identifier for the ordinal weekday unit.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var weekdayOrdinal: NSCalendar.Unit { get }
```

```c
NSCalendarUnitWeekdayOrdinal
```

## Discussion

The corresponding value is an `NSInteger`. Equal to `kCFCalendarUnitWeekdayOrdinal`. The weekday ordinal unit describes ordinal position within the month unit of the corresponding weekday unit. For example, in the Gregorian calendar a weekday ordinal unit of `2` for a weekday unit `3` indicates “the second Tuesday in the month”.

## See Also

### Specifying Weeks and Days
- [static var weekOfYear: NSCalendar.Unit](./weekofyear.md)
  Identifier for the week of the year calendar unit.
- [static var weekOfMonth: NSCalendar.Unit](./weekofmonth.md)
  Identifier for the week of the month calendar unit.
- [static var weekday: NSCalendar.Unit](./weekday.md)
  Identifier for the weekday unit.
- [static var day: NSCalendar.Unit](./day.md)
  Identifier for the day unit.
- [static var dayOfYear: NSCalendar.Unit](./dayofyear.md)
  Identifier for the nanosecond unit.
- [static var isRepeatedDay: NSCalendar.Unit](./isrepeatedday.md)
  Identifier for the time zone of a date components object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscalendar/unit/weekdayordinal)*