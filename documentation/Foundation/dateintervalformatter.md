# DateIntervalFormatter

**Framework**: Foundation  
**Kind**: class

A formatter that creates string representations of time intervals.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class DateIntervalFormatter
```

#### Overview

A [`DateIntervalFormatter`](dateintervalformatter.md) object creates user-readable strings from pairs of dates. Use a date interval formatter to create user-readable strings of the form  `-`  for your app’s interface, where  and  are date values that you supply. The formatter uses locale and language information, along with custom formatting options, to define the content of the resulting string. You can specify different styles for the date and time information in each date value.

To use this class, create an instance, configure its properties, and call the [`string(from:to:)`](dateintervalformatter/string(from:to:).md) method to generate a string. The properties of this class let you configure the calendar and specify the style to apply to date and time values. Given a current date of January 16, 2015, Configuring the Formatter Options shows how to configure a formatter object and generate the string “1/16/15 - 1/17/15”.

Configuring a formatter object

> **Note**:  Always set to the [`dateStyle`](dateintervalformatter/datestyle.md) and [`timeStyle`](dateintervalformatter/timestyle.md) properties to appropriate values before generating any strings.

 Always set to the [`dateStyle`](dateintervalformatter/datestyle.md) and [`timeStyle`](dateintervalformatter/timestyle.md) properties to appropriate values before generating any strings.

The [`string(from:to:)`](dateintervalformatter/string(from:to:).md) method may be called safely from any thread of your app. It is also safe to share a single instance of this class from multiple threads, with the caveat that you should not change the configuration of the object while another thread is using it to generate a string.

> 💡 **Tip**:  In Swift, you can use [`Date.IntervalFormatStyle`](date/intervalformatstyle.md) rather than [`DateIntervalFormatter`](dateintervalformatter.md). The [`FormatStyle`](formatstyle.md) API offers a declarative idiom for customizing the formatting of various types. Also, Foundation caches identical [`FormatStyle`](formatstyle.md) instances, so you don’t need to pass them around your app, or risk wasting memory with duplicate formatters.

 In Swift, you can use [`Date.IntervalFormatStyle`](date/intervalformatstyle.md) rather than [`DateIntervalFormatter`](dateintervalformatter.md). The [`FormatStyle`](formatstyle.md) API offers a declarative idiom for customizing the formatting of various types. Also, Foundation caches identical [`FormatStyle`](formatstyle.md) instances, so you don’t need to pass them around your app, or risk wasting memory with duplicate formatters.

## Topics

### Formatting a String
- [func string(from: Date, to: Date) -> String](dateintervalformatter/string(from:to:).md)
  Returns a formatted string based on the specified start and end dates.
### Configuring the Formatter Options
- [var dateStyle: DateIntervalFormatter.Style](dateintervalformatter/datestyle.md)
  The style to use when formatting day, month, and year information.
- [var timeStyle: DateIntervalFormatter.Style](dateintervalformatter/timestyle.md)
  The style to use when formatting hour, minute, and second information.
- [var dateTemplate: String!](dateintervalformatter/datetemplate.md)
  The template for formatting one date and time value.
- [var calendar: Calendar!](dateintervalformatter/calendar.md)
  The calendar to use for date values.
- [var locale: Locale!](dateintervalformatter/locale.md)
  The locale to use when formatting date and time values.
- [var timeZone: TimeZone!](dateintervalformatter/timezone.md)
  The time zone with which to specify time values.
### Constants
- [DateIntervalFormatter.Style](dateintervalformatter/style.md)
  Formatting styles for individual date and time values.
### Instance Methods
- [func string(from: DateInterval) -> String?](dateintervalformatter/string(from:).md)

## Relationships

### Inherits From
- [Formatter](formatter.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class DateFormatter](dateformatter.md)
  A formatter that converts between dates and their textual representations.
- [class DateComponentsFormatter](datecomponentsformatter.md)
  A formatter that creates string representations of quantities of time.
- [class RelativeDateTimeFormatter](relativedatetimeformatter.md)
  A formatter that creates locale-aware string representations of a relative date or time.
- [class ISO8601DateFormatter](iso8601dateformatter.md)
  A formatter that converts between dates and their ISO 8601 string representations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dateintervalformatter)*