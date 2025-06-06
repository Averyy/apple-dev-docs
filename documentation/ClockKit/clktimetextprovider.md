# CLKTimeTextProvider

**Framework**: ClockKit  
**Kind**: class

A formatted time value.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class CLKTimeTextProvider
```

## Mentions

- [Creating a timeline entry](creating-a-timeline-entry.md)

#### Overview

This provider supports time values in either the 24-hour or 12-hour format and takes into account the user’s region and locale settings. As needed, the provider automatically shortens the string to fit the available space.

When formatting the time, the time text provider drops the morning/evening indicator if it can’t fit the entire time value. For example, a provider configured to display the time 10:09AM in the English-US locale would remove elements as follows until it encountered a string that fit the available space:

- `10:09AM`
- `10:09`

## Topics

### Creating a Text Provider
- [convenience init(date: Date)](clktimetextprovider/init(date:).md)
  Creates and returns a text provider for displaying the specified time.
- [convenience init(date: Date, timeZone: TimeZone?)](clktimetextprovider/init(date:timezone:).md)
  Creates and returns a text provider for displaying the specified time.
### Getting the Time Information
- [var date: Date](clktimetextprovider/date.md)
  The date object containing the time value.
- [var timeZone: TimeZone?](clktimetextprovider/timezone.md)
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
- [class CLKTimeIntervalTextProvider](clktimeintervaltextprovider.md)
  A formatted time range.
- [class CLKTextProvider](clktextprovider.md)
  The common behavior for displaying text-based data in a complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clktimetextprovider)*