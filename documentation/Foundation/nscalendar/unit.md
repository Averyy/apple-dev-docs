# NSCalendar.Unit

**Framework**: Foundation  
**Kind**: struct

Calendrical units such as year, month, day and hour.

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
struct Unit
```

#### Overview

Calendar units may be used as a bit mask to specify a combination of units. Values in this enumeration are equal to the corresponding constants in `CFCalendarUnit`.

## Topics

### Initializers
- [init(rawValue: UInt)](nscalendar/unit/init(rawvalue:).md)
  Creates a new calendar unit from the raw value.
### Specifying Years and Months
- [static var era: NSCalendar.Unit](nscalendar/unit/era.md)
  Identifier for the era unit.
- [static var year: NSCalendar.Unit](nscalendar/unit/year.md)
  Identifier for the year unit.
- [static var yearForWeekOfYear: NSCalendar.Unit](nscalendar/unit/yearforweekofyear.md)
  Identifier for the week-counting year unit.
- [static var quarter: NSCalendar.Unit](nscalendar/unit/quarter.md)
  Identifier for the quarter of the calendar.
- [static var month: NSCalendar.Unit](nscalendar/unit/month.md)
  Identifier for the month unit.
- [static var isLeapMonth: NSCalendar.Unit](nscalendar/unit/isleapmonth.md)
### Specifying Weeks and Days
- [static var weekOfYear: NSCalendar.Unit](nscalendar/unit/weekofyear.md)
  Identifier for the week of the year calendar unit.
- [static var weekOfMonth: NSCalendar.Unit](nscalendar/unit/weekofmonth.md)
  Identifier for the week of the month calendar unit.
- [static var weekday: NSCalendar.Unit](nscalendar/unit/weekday.md)
  Identifier for the weekday unit.
- [static var weekdayOrdinal: NSCalendar.Unit](nscalendar/unit/weekdayordinal.md)
  Identifier for the ordinal weekday unit.
- [static var day: NSCalendar.Unit](nscalendar/unit/day.md)
  Identifier for the day unit.
- [static var dayOfYear: NSCalendar.Unit](nscalendar/unit/dayofyear.md)
- [static var isRepeatedDay: NSCalendar.Unit](nscalendar/unit/isrepeatedday.md)
### Specifying Hours, Minutes, and Seconds
- [static var hour: NSCalendar.Unit](nscalendar/unit/hour.md)
  Identifier for the hour unit.
- [static var minute: NSCalendar.Unit](nscalendar/unit/minute.md)
  Identifier for the minute unit.
- [static var second: NSCalendar.Unit](nscalendar/unit/second.md)
  Identifier for the second unit.
- [static var nanosecond: NSCalendar.Unit](nscalendar/unit/nanosecond.md)
  Identifier for the nanosecond unit.
### Specifying Calendars and Time Zones
- [static var calendar: NSCalendar.Unit](nscalendar/unit/calendar.md)
  Identifier for the calendar of a date components object.
- [static var timeZone: NSCalendar.Unit](nscalendar/unit/timezone.md)
  Identifier for the time zone of a date components object.
### Deprecated
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
- [static var NSWeekdayOrdinalCalendarUnit: NSCalendar.Unit](nscalendar/unit/nsweekdayordinalcalendarunit.md)
  Specifies the ordinal weekday unit.
- [static var NSQuarterCalendarUnit: NSCalendar.Unit](nscalendar/unit/nsquartercalendarunit.md)
  Specifies the quarter unit.
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
- [static var NSWeekdayOrdinalCalendarUnit: NSCalendar.Unit](nscalendar/unit/nsweekdayordinalcalendarunit.md)
  Specifies the ordinal weekday unit.
- [static var NSQuarterCalendarUnit: NSCalendar.Unit](nscalendar/unit/nsquartercalendarunit.md)
  Specifies the quarter unit.
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

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var calendarIdentifier: NSCalendar.Identifier](nscalendar/calendaridentifier.md)
  An identifier for the calendar.
- [var firstWeekday: Int](nscalendar/firstweekday.md)
  The index of the first weekday of the receiver.
- [var locale: Locale?](nscalendar/locale.md)
  The locale of the receiver.
- [var timeZone: TimeZone](nscalendar/timezone.md)
  The time zone for the calendar.
- [func maximumRange(of: NSCalendar.Unit) -> NSRange](nscalendar/maximumrange(of:).md)
  Returns the maximum range limits of the values that a given unit can take on.
- [func minimumRange(of: NSCalendar.Unit) -> NSRange](nscalendar/minimumrange(of:).md)
  Returns the minimum range limits of the values that a given unit can take on.
- [var minimumDaysInFirstWeek: Int](nscalendar/minimumdaysinfirstweek.md)
  The minimum number of days in the first week of the receiver.
- [func ordinality(of: NSCalendar.Unit, in: NSCalendar.Unit, for: Date) -> Int](nscalendar/ordinality(of:in:for:).md)
  Returns, for a given absolute time, the ordinal number of a smaller calendar unit (such as a day) within a specified larger calendar unit (such as a week).
- [func range(of: NSCalendar.Unit, in: NSCalendar.Unit, for: Date) -> NSRange](nscalendar/range(of:in:for:).md)
  Returns the range of absolute time values that a smaller calendar unit (such as a day) can take on in a larger calendar unit (such as a month) that includes a specified absolute time.
- [func range(of: NSCalendar.Unit, start: AutoreleasingUnsafeMutablePointer<NSDate?>?, interval: UnsafeMutablePointer<TimeInterval>?, for: Date) -> Bool](nscalendar/range(of:start:interval:for:).md)
  Returns by reference the starting time and duration of a given calendar unit that contains a given date.
- [func range(ofWeekendStart: AutoreleasingUnsafeMutablePointer<NSDate?>?, interval: UnsafeMutablePointer<TimeInterval>?, containing: Date) -> Bool](nscalendar/range(ofweekendstart:interval:containing:).md)
  Returns whether a given date falls within a weekend period, and if so, returns by reference the start date and time interval of the weekend range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscalendar/unit)*