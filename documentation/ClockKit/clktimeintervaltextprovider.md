# CLKTimeIntervalTextProvider

**Framework**: ClockKit  
**Kind**: class

A formatted time range.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class CLKTimeIntervalTextProvider
```

## Mentions

- [Creating a timeline entry](creating-a-timeline-entry.md)

#### Overview

This provider creates strings like “10:15–11:15AM” where the time range may span hours, days, or some larger time interval. The text provider takes into account the user’s region and locale settings.

Time interval strings are more appropriate in complication families where there’s sufficient space to draw the full time range, such as the modular large and utilitarian large families. In families where space is more limited, the provider may display only the start date of the time range.

When formatting the time interval, the time text provider drops the morning/evening indicator of the start time when it’s the same as the end time. Time intervals that are more than 24 hours are displayed as a range of days. The following are some examples of formatted time intervals:

- `9:30AM - 3:30PM`
- `9:30 - 10:30AM`
- `Jan 1 - Jan 7`
- `1/1 - 1/7`

## Topics

### Creating the Text Provider
- [convenience init(start: Date, end: Date)](clktimeintervaltextprovider/init(start:end:).md)
  Creates and returns a text provider with the specified start and end dates.
- [convenience init(start: Date, end: Date, timeZone: TimeZone?)](clktimeintervaltextprovider/init(start:end:timezone:).md)
  Creates and returns a text provider with the specified dates and time zone information.
### Getting the Time Information
- [var startDate: Date](clktimeintervaltextprovider/startdate.md)
  The start date for the time interval.
- [var endDate: Date](clktimeintervaltextprovider/enddate.md)
  The end date for the time interval.
- [var timeZone: TimeZone?](clktimeintervaltextprovider/timezone.md)
  The time zone used to format time values.

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
- [class CLKRelativeDateTextProvider](clkrelativedatetextprovider.md)
  A formatted string that conveys the difference in time between the current date and a date that you specify.
- [class CLKTimeTextProvider](clktimetextprovider.md)
  A formatted time value.
- [class CLKTextProvider](clktextprovider.md)
  The common behavior for displaying text-based data in a complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clktimeintervaltextprovider)*