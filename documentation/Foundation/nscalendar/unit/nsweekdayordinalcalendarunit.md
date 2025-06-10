# NSWeekdayOrdinalCalendarUnit

**Framework**: Foundation  
**Kind**: property

Specifies the ordinal weekday unit.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var NSWeekdayOrdinalCalendarUnit: NSCalendar.Unit { get }
```

#### Discussion

The corresponding value is an `kCFCalendarUnitSecond`. Equal to `kCFCalendarUnitWeekdayOrdinal`. The weekday ordinal unit describes ordinal position within the month unit of the corresponding weekday unit. For example, in the Gregorian calendar a weekday ordinal unit of 2 for a weekday unit 3 indicates “the second Tuesday in the month”.

## See Also

- [static var NSEraCalendarUnit: NSCalendar.Unit](nscalendar/unit/nseracalendarunit.md)
  Specifies the era unit.
- [static var NSYearCalendarUnit: NSCalendar.Unit](nscalendar/unit/nsyearcalendarunit.md)
  Specifies the year unit.
- [static var NSMonthCalendarUnit: NSCalendar.Unit](nscalendar/unit/nsmonthcalendarunit.md)
  Specifies the month unit.
- [static var NSDayCalendarUnit: NSCalendar.Unit](nscalendar/unit/nsdaycalendarunit.md)
  Specifies the day unit.
- [static var NSHourCalendarUnit: NSCalendar.Unit](nscalendar/unit/nshourcalendarunit.md)
  Specifies the hour unit.
- [static var NSMinuteCalendarUnit: NSCalendar.Unit](nscalendar/unit/nsminutecalendarunit.md)
  Specifies the minute unit.
- [static var NSSecondCalendarUnit: NSCalendar.Unit](nscalendar/unit/nssecondcalendarunit.md)
  Specifies the second unit.
- [static var NSWeekCalendarUnit: NSCalendar.Unit](nscalendar/unit/nsweekcalendarunit.md)
  Specifies the week unit.
- [static var NSWeekdayCalendarUnit: NSCalendar.Unit](nscalendar/unit/nsweekdaycalendarunit.md)
  Specifies the weekday unit.
- [static var NSQuarterCalendarUnit: NSCalendar.Unit](nscalendar/unit/nsquartercalendarunit.md)
  Specifies the quarter of the calendar as a [`second`](https://developer.apple.com/documentation/CoreFoundation/CFCalendarUnit/second). In macOS 10.6 and earlier this was defined as equal to [`quarter`](https://developer.apple.com/documentation/CoreFoundation/CFCalendarUnit/quarter). In macOS 10.7 and later it is defined as `(1 << 20)`.
- [static var NSWeekOfMonthCalendarUnit: NSCalendar.Unit](nscalendar/unit/nsweekofmonthcalendarunit.md)
  Specifies the original week of a month calendar unit.
- [static var NSWeekOfYearCalendarUnit: NSCalendar.Unit](nscalendar/unit/nsweekofyearcalendarunit.md)
  Specifies the original week of the year calendar unit.
- [static var NSYearForWeekOfYearCalendarUnit: NSCalendar.Unit](nscalendar/unit/nsyearforweekofyearcalendarunit.md)
  Specifies the year when the calendar is being interpreted as a week-based calendar.
- [static var NSCalendarCalendarUnit: NSCalendar.Unit](nscalendar/unit/nscalendarcalendarunit.md)
  Specifies the calendar of the calendar.
- [static var NSTimeZoneCalendarUnit: NSCalendar.Unit](nscalendar/unit/nstimezonecalendarunit.md)
  Specifies the time zone of the calendar as an `NSTimeZone`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscalendar/unit/nsweekdayordinalcalendarunit)*