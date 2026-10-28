# CLKDateTextProvider

**Framework**: ClockKit  
**Kind**: class  
**Role**: Class

A formatted string that conveys a date without any time information.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) to create complications for watchOS 10 or later. For more information, see Migrating to WidgetKit.

## Declaration

```swift
class CLKDateTextProvider
```

```objc
@interface CLKDateTextProvider : CLKTextProvider
```

## Mentions

- [Creating a timeline entry](./creating-a-timeline-entry.md)

## Overview

Use a date provider for strings that contain day, month, and year information. The text provider formats the date information consistently and in a way that makes the best use of the available space. It also takes into account the user’s region and locale settings.

When creating the formatted string, the date text provider creates the longest string that fits in the given space. It includes as many of the requested date elements as it can, but may truncate elements or use abbreviations as needed.

### Date Format Options

When creating a `CLKDateTextProvider` object, you must specify which calendar units you want included in the resulting date. Only the following calendar units are supported:

- [`NSDayCalendarUnit`](../Foundation/nscalendar/unit/nsdaycalendarunit.md)
- [`NSMonthCalendarUnit`](../Foundation/nscalendar/unit/nsmonthcalendarunit.md)
- [`NSWeekdayCalendarUnit`](../Foundation/nscalendar/unit/nsweekdaycalendarunit.md)
- [`NSYearCalendarUnit`](../Foundation/nscalendar/unit/nsyearcalendarunit.md)

All other calendar units are ignored.

When formatting the date, the date text provider drops units starting at the end of the preceding list and working up. In other words, it drops the year first, followed by the weekday information, followed by the month. For example, a text provider configured to display all units for the date December 28, 2014 in the English-US locale would remove elements as follows until it encountered a string that fit the available space:

- `Saturday, December 28, 2015`
- `Saturday, December 28`
- `Saturday, Dec 28`
- `Sat, Dec 28`
- `Dec 28`
- `28`

## Topics

### Creating a Text Provider
- [convenience init(date: Date, units: NSCalendar.Unit)](./clkdatetextprovider/init%28date,units%29.md)
  Creates and returns a text provider with the specified date and the default time zone.
- [convenience init(date: Date, units: NSCalendar.Unit, timeZone: TimeZone?)](./clkdatetextprovider/init%28date,units,timezone%29.md)
  Creates and returns a text provider with the specified date and time zone.
- [- initWithDate:units:](./clkdatetextprovider/initwithdate_units_.md)
  Creates and returns a text provider with the specified date and the default time zone.
- [- initWithDate:units:timeZone:](./clkdatetextprovider/initwithdate_units_timezone_.md)
  Creates and returns a text provider with the specified date and time zone.
### Getting the Date Information
- [var date: Date](./clkdatetextprovider/date.md)
  The date to display.
- [var timeZone: TimeZone?](./clkdatetextprovider/timezone.md)
  The time zone used in the formatted string.
- [var calendarUnits: NSCalendar.Unit](./clkdatetextprovider/calendarunits.md)
  The calendar units to include in the formatted string.
- [var uppercase: Bool](./clkdatetextprovider/uppercase.md)
  A Boolean value that determines whether the date string displays in uppercase.

## Relationships

### Inherits From
- [CLKTextProvider](./clktextprovider.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Text providers
- [class CLKSimpleTextProvider](./clksimpletextprovider.md)
  A single line of text to display in your complication interface.
- [class CLKRelativeDateTextProvider](./clkrelativedatetextprovider.md)
  A formatted string that conveys the difference in time between the current date and a date that you specify.
- [class CLKTimeIntervalTextProvider](./clktimeintervaltextprovider.md)
  A formatted time range.
- [class CLKTimeTextProvider](./clktimetextprovider.md)
  A formatted time value.
- [class CLKTextProvider](./clktextprovider.md)
  The common behavior for displaying text-based data in a complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkdatetextprovider)*