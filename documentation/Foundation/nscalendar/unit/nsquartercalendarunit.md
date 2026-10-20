# NSQuarterCalendarUnit

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Specifies the quarter unit.

**Availability**:
- iOS 4.0+ - Deprecated in 8.0 (renamed: NSCalendar.Unit.quarter)
- iPadOS 4.0+ - Deprecated in 8.0 (renamed: NSCalendar.Unit.quarter)
- Mac Catalyst 13.1+ - Deprecated in 13.1 (renamed: NSCalendar.Unit.quarter)
- macOS 10.6+ - Deprecated in 10.10 (renamed: NSCalendar.Unit.quarter)
- tvOS 9.0+ - Deprecated in 9.0 (renamed: NSCalendar.Unit.quarter)
- visionOS 1.0+ - Deprecated in 1.0 (renamed: NSCalendar.Unit.quarter)
- watchOS 2.0+ - Deprecated in 2.0 (renamed: NSCalendar.Unit.quarter)

> **Deprecated**: Use [`quarter`](./quarter.md) instead.

## Declaration

```swift
static var NSQuarterCalendarUnit: NSCalendar.Unit { get }
```

```c
NSQuarterCalendarUnit
```

#### Discussion

In macOS 10.6 and earlier this was defined as equal to [`quarter`](../../../CoreFoundation/cfcalendarunit/quarter.md). In macOS 10.7 and later it is defined as `(1 << 20)`.

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
- [static var NSWeekdayOrdinalCalendarUnit: NSCalendar.Unit](./nsweekdayordinalcalendarunit.md)
  Specifies the ordinal weekday unit.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscalendar/unit/nsquartercalendarunit)*