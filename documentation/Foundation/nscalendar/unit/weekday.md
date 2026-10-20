# weekday

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Identifier for the weekday unit.

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
static var weekday: NSCalendar.Unit { get }
```

```c
NSCalendarUnitWeekday
```

#### Discussion

The corresponding value is an `NSInteger`. Equal to `kCFCalendarUnitWeekday`. The weekday units are the numbers `1` through `N` (where for the Gregorian calendar `N`=`7` and `1` is Sunday).

## See Also

### Specifying Weeks and Days
- [static var weekOfYear: NSCalendar.Unit](./weekofyear.md)
  Identifier for the week of the year calendar unit.
- [static var weekOfMonth: NSCalendar.Unit](./weekofmonth.md)
  Identifier for the week of the month calendar unit.
- [static var weekdayOrdinal: NSCalendar.Unit](./weekdayordinal.md)
  Identifier for the ordinal weekday unit.
- [static var day: NSCalendar.Unit](./day.md)
  Identifier for the day unit.
- [static var dayOfYear: NSCalendar.Unit](./dayofyear.md)
  Identifier for the nanosecond unit.
- [static var isRepeatedDay: NSCalendar.Unit](./isrepeatedday.md)
  Identifier for the time zone of a date components object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscalendar/unit/weekday)*