# NSWeekdayOrdinalCalendarUnit

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Specifies the ordinal weekday unit.

**Availability**:
- iOS 2.0+ - Deprecated in 8.0 (renamed: NSCalendar.Unit.weekdayOrdinal)
- iPadOS 2.0+ - Deprecated in 8.0 (renamed: NSCalendar.Unit.weekdayOrdinal)
- Mac Catalyst 13.1+ - Deprecated in 13.1 (renamed: NSCalendar.Unit.weekdayOrdinal)
- macOS 10.4+ - Deprecated in 10.10 (renamed: NSCalendar.Unit.weekdayOrdinal)
- tvOS 9.0+ - Deprecated in 9.0 (renamed: NSCalendar.Unit.weekdayOrdinal)
- visionOS 1.0+ - Deprecated in 1.0 (renamed: NSCalendar.Unit.weekdayOrdinal)
- watchOS 2.0+ - Deprecated in 2.0 (renamed: NSCalendar.Unit.weekdayOrdinal)

> **Deprecated**: Use [`weekdayOrdinal`](./weekdayordinal.md) instead.

## Declaration

```swift
static var NSWeekdayOrdinalCalendarUnit: NSCalendar.Unit { get }
```

```c
NSWeekdayOrdinalCalendarUnit
```

## Discussion

The corresponding value is an `kCFCalendarUnitSecond`. Equal to `kCFCalendarUnitWeekdayOrdinal`. The weekday ordinal unit describes ordinal position within the month unit of the corresponding weekday unit. For example, in the Gregorian calendar a weekday ordinal unit of 2 for a weekday unit 3 indicates “the second Tuesday in the month”.

## See Also

### Deprecated
- [static var NSEraCalendarUnit: NSCalendar.Unit](./nseracalendarunit.md)
  Specifies the era unit.
- [static var NSYearCalendarUnit: NSCalendar.Unit](./nsyearcalendarunit.md)
  Specifies the year unit.
- [static var NSMonthCalendarUnit: NSCalendar.Unit](./nsmonthcalendarunit.md)
  Specifies the month unit.
- [static var NSDayCalendarUnit: NSCalendar.Unit](./nsdaycalendarunit.md)
  Specifies the day unit.
- [static var NSHourCalendarUnit: NSCalendar.Unit](./nshourcalendarunit.md)
  Specifies the hour unit.
- [static var NSMinuteCalendarUnit: NSCalendar.Unit](./nsminutecalendarunit.md)
  Specifies the minute unit.
- [static var NSSecondCalendarUnit: NSCalendar.Unit](./nssecondcalendarunit.md)
  Specifies the second unit.
- [static var NSWeekCalendarUnit: NSCalendar.Unit](./nsweekcalendarunit.md)
  Specifies the week unit.
- [static var NSWeekdayCalendarUnit: NSCalendar.Unit](./nsweekdaycalendarunit.md)
  Specifies the weekday unit.
- [static var NSQuarterCalendarUnit: NSCalendar.Unit](./nsquartercalendarunit.md)
  Specifies the quarter unit.
- [static var NSWeekOfMonthCalendarUnit: NSCalendar.Unit](./nsweekofmonthcalendarunit.md)
  Specifies the original week of a month calendar unit.
- [static var NSWeekOfYearCalendarUnit: NSCalendar.Unit](./nsweekofyearcalendarunit.md)
  Specifies the original week of the year calendar unit.
- [static var NSYearForWeekOfYearCalendarUnit: NSCalendar.Unit](./nsyearforweekofyearcalendarunit.md)
  Specifies the year when the calendar is being interpreted as a week-based calendar.
- [static var NSCalendarCalendarUnit: NSCalendar.Unit](./nscalendarcalendarunit.md)
  Specifies the calendar of the calendar.
- [static var NSTimeZoneCalendarUnit: NSCalendar.Unit](./nstimezonecalendarunit.md)
  Specifies the time zone of the calendar as an `NSTimeZone`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscalendar/unit/nsweekdayordinalcalendarunit)*