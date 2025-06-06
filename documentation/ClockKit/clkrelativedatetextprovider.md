# CLKRelativeDateTextProvider

**Framework**: Clockkit  
**Kind**: class

A formatted string that conveys the difference in time between the current date and a date that you specify.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class CLKRelativeDateTextProvider
```

## Mentions

- [Creating a timeline entry](creating-a-timeline-entry.md)

#### Overview

You use a relative date text provider to implement timers or other relative time values in an efficient way. Instead of using multiple timeline entries to replicate a countdown timer, create a single timeline entry with a relative date text provider. When the user views the clock face, ClockKit automatically updates the relative time value in your complication, providing up-to-date time information.

When creating the formatted string, the relative date text provider creates the longest string that fits in the given space. It includes as many of the requested date elements as it can, but may truncate elements or use abbreviations as needed. The formatted string takes into account the user’s region and locale settings.

##### Date Format Options

When creating a `CLKRelativeDateTextProvider` object, you must specify which calendar units you want included in the resulting date. Only the following calendar units are supported:

- [`NSYearCalendarUnit`](https://developer.apple.com/documentation/foundation/nscalendar/unit/1415822-nsyearcalendarunit)
- [`NSMonthCalendarUnit`](https://developer.apple.com/documentation/foundation/nscalendar/unit/1408613-nsmonthcalendarunit)
- [`NSWeekOfMonthCalendarUnit`](https://developer.apple.com/documentation/foundation/nscalendar/unit/1411920-nsweekofmonthcalendarunit)
- [`NSDayCalendarUnit`](https://developer.apple.com/documentation/foundation/nscalendar/unit/1409435-nsdaycalendarunit)
- [`NSHourCalendarUnit`](https://developer.apple.com/documentation/foundation/nscalendar/unit/1411272-nshourcalendarunit)
- [`NSMinuteCalendarUnit`](https://developer.apple.com/documentation/foundation/nscalendar/unit/1413292-nsminutecalendarunit)
- [`NSSecondCalendarUnit`](https://developer.apple.com/documentation/foundation/nscalendar/unit/1416859-nssecondcalendarunit)

> **Note**:  When creating a relative date provider using the [`CLKRelativeDateStyle.timer`](clkrelativedatestyle/timer.md) style, only the [`NSHourCalendarUnit`](https://developer.apple.com/documentation/foundation/nscalendar/unit/1411272-nshourcalendarunit), [`NSMinuteCalendarUnit`](https://developer.apple.com/documentation/foundation/nscalendar/unit/1413292-nsminutecalendarunit), and [`NSSecondCalendarUnit`](https://developer.apple.com/documentation/foundation/nscalendar/unit/1416859-nssecondcalendarunit) units are supported.

All other calendar units are ignored.

The format of the relative time value is dependent on the date style you choose when creating the text provider. For a list of possible styles and examples of each, see [`CLKRelativeDateStyle`](clkrelativedatestyle.md).

## Topics

### Creating a Text Provider
- [convenience init(date: Date, style: CLKRelativeDateStyle, units: NSCalendar.Unit)](clkrelativedatetextprovider/init(date:style:units:).md)
  Creates a text provider that shows the difference between the current time and the specified date.
- [convenience init(date: Date, relativeTo: Date?, style: CLKRelativeDateStyle, units: NSCalendar.Unit)](clkrelativedatetextprovider/init(date:relativeto:style:units:).md)
  Creates a text provider that shows the difference in time between the provided dates.
### Getting the Date Information
- [var date: Date](clkrelativedatetextprovider/date.md)
  The target date to use for calculations.
- [var relativeToDate: Date?](clkrelativedatetextprovider/relativetodate.md)
  The end date that the text provider uses when calculating a fixed, relative date.
- [var relativeDateStyle: CLKRelativeDateStyle](clkrelativedatetextprovider/relativedatestyle.md)
  The formatting style to use for the relative time value.
- [var calendarUnits: NSCalendar.Unit](clkrelativedatetextprovider/calendarunits.md)
  The calendar units to include in the formatted string.
### Constants
- [enum CLKRelativeDateStyle](clkrelativedatestyle.md)
  Constants indicating the formatting style for the relative date values.

## Relationships

### Inherits From
- [CLKTextProvider](clktextprovider.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CLKSimpleTextProvider](clksimpletextprovider.md)
  A single line of text to display in your complication interface.
- [class CLKDateTextProvider](clkdatetextprovider.md)
  A formatted string that conveys a date without any time information.
- [class CLKTimeIntervalTextProvider](clktimeintervaltextprovider.md)
  A formatted time range.
- [class CLKTimeTextProvider](clktimetextprovider.md)
  A formatted time value.
- [class CLKTextProvider](clktextprovider.md)
  The common behavior for displaying text-based data in a complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ClockKit/clkrelativedatetextprovider)*