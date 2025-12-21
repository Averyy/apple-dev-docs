# weekday

**Framework**: Foundation  
**Kind**: property

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

#### Discussion

The corresponding value is an `NSInteger`. Equal to `kCFCalendarUnitWeekday`. The weekday units are the numbers `1` through `N` (where for the Gregorian calendar `N`=`7` and `1` is Sunday).

## See Also

- [static var weekOfYear: NSCalendar.Unit](nscalendar/unit/weekofyear.md)
  Identifier for the week of the year calendar unit.
- [static var weekOfMonth: NSCalendar.Unit](nscalendar/unit/weekofmonth.md)
  Identifier for the week of the month calendar unit.
- [static var weekdayOrdinal: NSCalendar.Unit](nscalendar/unit/weekdayordinal.md)
  Identifier for the ordinal weekday unit.
- [static var day: NSCalendar.Unit](nscalendar/unit/day.md)
  Identifier for the day unit.
- [static var dayOfYear: NSCalendar.Unit](nscalendar/unit/dayofyear.md)
- [static var isRepeatedDay: NSCalendar.Unit](nscalendar/unit/isrepeatedday.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscalendar/unit/weekday)*