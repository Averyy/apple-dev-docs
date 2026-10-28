# NSCalendar.Unit

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

```c
enum NSCalendarUnit : NSUInteger;
```

## Overview

Calendar units may be used as a bit mask to specify a combination of units. Values in this enumeration are equal to the corresponding constants in `CFCalendarUnit`.

## Topics

### Initializers
- [init(rawValue: UInt)](./unit/init%28rawvalue%29.md)
  Creates a new calendar unit from the raw value.
### Specifying Years and Months
- [static var era: NSCalendar.Unit](./unit/era.md)
  Identifier for the era unit.
- [static var year: NSCalendar.Unit](./unit/year.md)
  Identifier for the year unit.
- [static var yearForWeekOfYear: NSCalendar.Unit](./unit/yearforweekofyear.md)
  Identifier for the week-counting year unit.
- [static var quarter: NSCalendar.Unit](./unit/quarter.md)
  Identifier for the quarter of the calendar.
- [static var month: NSCalendar.Unit](./unit/month.md)
  Identifier for the month unit.
- [static var isLeapMonth: NSCalendar.Unit](./unit/isleapmonth.md)
  Identifier for the time zone of a date components object.
### Specifying Weeks and Days
- [static var weekOfYear: NSCalendar.Unit](./unit/weekofyear.md)
  Identifier for the week of the year calendar unit.
- [static var weekOfMonth: NSCalendar.Unit](./unit/weekofmonth.md)
  Identifier for the week of the month calendar unit.
- [static var weekday: NSCalendar.Unit](./unit/weekday.md)
  Identifier for the weekday unit.
- [static var weekdayOrdinal: NSCalendar.Unit](./unit/weekdayordinal.md)
  Identifier for the ordinal weekday unit.
- [static var day: NSCalendar.Unit](./unit/day.md)
  Identifier for the day unit.
- [static var dayOfYear: NSCalendar.Unit](./unit/dayofyear.md)
  Identifier for the nanosecond unit.
- [static var isRepeatedDay: NSCalendar.Unit](./unit/isrepeatedday.md)
  Identifier for the time zone of a date components object.
### Specifying Hours, Minutes, and Seconds
- [static var hour: NSCalendar.Unit](./unit/hour.md)
  Identifier for the hour unit.
- [static var minute: NSCalendar.Unit](./unit/minute.md)
  Identifier for the minute unit.
- [static var second: NSCalendar.Unit](./unit/second.md)
  Identifier for the second unit.
- [static var nanosecond: NSCalendar.Unit](./unit/nanosecond.md)
  Identifier for the nanosecond unit.
### Specifying Calendars and Time Zones
- [static var calendar: NSCalendar.Unit](./unit/calendar.md)
  Identifier for the calendar of a date components object.
- [static var timeZone: NSCalendar.Unit](./unit/timezone.md)
  Identifier for the time zone of a date components object.
### Deprecated
- [static var NSEraCalendarUnit: NSCalendar.Unit](./unit/nseracalendarunit.md)
  Specifies the era unit.
- [static var NSYearCalendarUnit: NSCalendar.Unit](./unit/nsyearcalendarunit.md)
  Specifies the year unit.
- [static var NSMonthCalendarUnit: NSCalendar.Unit](./unit/nsmonthcalendarunit.md)
  Specifies the month unit.
- [static var NSDayCalendarUnit: NSCalendar.Unit](./unit/nsdaycalendarunit.md)
  Specifies the day unit.
- [static var NSHourCalendarUnit: NSCalendar.Unit](./unit/nshourcalendarunit.md)
  Specifies the hour unit.
- [static var NSMinuteCalendarUnit: NSCalendar.Unit](./unit/nsminutecalendarunit.md)
  Specifies the minute unit.
- [static var NSSecondCalendarUnit: NSCalendar.Unit](./unit/nssecondcalendarunit.md)
  Specifies the second unit.
- [static var NSWeekCalendarUnit: NSCalendar.Unit](./unit/nsweekcalendarunit.md)
  Specifies the week unit.
- [static var NSWeekdayCalendarUnit: NSCalendar.Unit](./unit/nsweekdaycalendarunit.md)
  Specifies the weekday unit.
- [static var NSWeekdayOrdinalCalendarUnit: NSCalendar.Unit](./unit/nsweekdayordinalcalendarunit.md)
  Specifies the ordinal weekday unit.
- [static var NSQuarterCalendarUnit: NSCalendar.Unit](./unit/nsquartercalendarunit.md)
  Specifies the quarter unit.
- [static var NSWeekOfMonthCalendarUnit: NSCalendar.Unit](./unit/nsweekofmonthcalendarunit.md)
  Specifies the original week of a month calendar unit.
- [static var NSWeekOfYearCalendarUnit: NSCalendar.Unit](./unit/nsweekofyearcalendarunit.md)
  Specifies the original week of the year calendar unit.
- [static var NSYearForWeekOfYearCalendarUnit: NSCalendar.Unit](./unit/nsyearforweekofyearcalendarunit.md)
  Specifies the year when the calendar is being interpreted as a week-based calendar.
- [static var NSCalendarCalendarUnit: NSCalendar.Unit](./unit/nscalendarcalendarunit.md)
  Specifies the calendar of the calendar.
- [static var NSTimeZoneCalendarUnit: NSCalendar.Unit](./unit/nstimezonecalendarunit.md)
  Specifies the time zone of the calendar as an `NSTimeZone`.
- [static var NSEraCalendarUnit: NSCalendar.Unit](./unit/nseracalendarunit.md)
  Specifies the era unit.
- [static var NSYearCalendarUnit: NSCalendar.Unit](./unit/nsyearcalendarunit.md)
  Specifies the year unit.
- [static var NSMonthCalendarUnit: NSCalendar.Unit](./unit/nsmonthcalendarunit.md)
  Specifies the month unit.
- [static var NSDayCalendarUnit: NSCalendar.Unit](./unit/nsdaycalendarunit.md)
  Specifies the day unit.
- [static var NSHourCalendarUnit: NSCalendar.Unit](./unit/nshourcalendarunit.md)
  Specifies the hour unit.
- [static var NSMinuteCalendarUnit: NSCalendar.Unit](./unit/nsminutecalendarunit.md)
  Specifies the minute unit.
- [static var NSSecondCalendarUnit: NSCalendar.Unit](./unit/nssecondcalendarunit.md)
  Specifies the second unit.
- [static var NSWeekCalendarUnit: NSCalendar.Unit](./unit/nsweekcalendarunit.md)
  Specifies the week unit.
- [static var NSWeekdayCalendarUnit: NSCalendar.Unit](./unit/nsweekdaycalendarunit.md)
  Specifies the weekday unit.
- [static var NSWeekdayOrdinalCalendarUnit: NSCalendar.Unit](./unit/nsweekdayordinalcalendarunit.md)
  Specifies the ordinal weekday unit.
- [static var NSQuarterCalendarUnit: NSCalendar.Unit](./unit/nsquartercalendarunit.md)
  Specifies the quarter unit.
- [static var NSWeekOfMonthCalendarUnit: NSCalendar.Unit](./unit/nsweekofmonthcalendarunit.md)
  Specifies the original week of a month calendar unit.
- [static var NSWeekOfYearCalendarUnit: NSCalendar.Unit](./unit/nsweekofyearcalendarunit.md)
  Specifies the original week of the year calendar unit.
- [static var NSYearForWeekOfYearCalendarUnit: NSCalendar.Unit](./unit/nsyearforweekofyearcalendarunit.md)
  Specifies the year when the calendar is being interpreted as a week-based calendar.
- [static var NSCalendarCalendarUnit: NSCalendar.Unit](./unit/nscalendarcalendarunit.md)
  Specifies the calendar of the calendar.
- [static var NSTimeZoneCalendarUnit: NSCalendar.Unit](./unit/nstimezonecalendarunit.md)
  Specifies the time zone of the calendar as an `NSTimeZone`.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Getting Calendar Information
- [var calendarIdentifier: NSCalendar.Identifier](./calendaridentifier.md)
  An identifier for the calendar.
- [var firstWeekday: Int](./firstweekday.md)
  The index of the first weekday of the receiver.
- [var locale: Locale?](./locale.md)
  The locale of the receiver.
- [var timeZone: TimeZone](./timezone.md)
  The time zone for the calendar.
- [func maximumRange(of: NSCalendar.Unit) -> NSRange](./maximumrange%28of%29.md)
  Returns the maximum range limits of the values that a given unit can take on.
- [func minimumRange(of: NSCalendar.Unit) -> NSRange](./minimumrange%28of%29.md)
  Returns the minimum range limits of the values that a given unit can take on.
- [var minimumDaysInFirstWeek: Int](./minimumdaysinfirstweek.md)
  The minimum number of days in the first week of the receiver.
- [func ordinality(of: NSCalendar.Unit, in: NSCalendar.Unit, for: Date) -> Int](./ordinality%28of,in,for%29.md)
  Returns, for a given absolute time, the ordinal number of a smaller calendar unit (such as a day) within a specified larger calendar unit (such as a week).
- [func range(of: NSCalendar.Unit, in: NSCalendar.Unit, for: Date) -> NSRange](./range%28of,in,for%29.md)
  Returns the range of absolute time values that a smaller calendar unit (such as a day) can take on in a larger calendar unit (such as a month) that includes a specified absolute time.
- [func range(of: NSCalendar.Unit, start: AutoreleasingUnsafeMutablePointer<NSDate?>?, interval: UnsafeMutablePointer<TimeInterval>?, for: Date) -> Bool](./range%28of,start,interval,for%29.md)
  Returns by reference the starting time and duration of a given calendar unit that contains a given date.
- [func range(ofWeekendStart: AutoreleasingUnsafeMutablePointer<NSDate?>?, interval: UnsafeMutablePointer<TimeInterval>?, containing: Date) -> Bool](./range%28ofweekendstart,interval,containing%29.md)
  Returns whether a given date falls within a weekend period, and if so, returns by reference the start date and time interval of the weekend range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscalendar/unit)*