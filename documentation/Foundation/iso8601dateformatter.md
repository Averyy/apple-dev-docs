# ISO8601DateFormatter

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

A formatter that converts between dates and their ISO 8601 string representations.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class ISO8601DateFormatter
```

```objc
@interface NSISO8601DateFormatter : NSFormatter
```

#### Overview

The [`ISO8601DateFormatter`](./iso8601dateformatter.md) class generates and parses string representations of dates following the [ISO 8601](http://www.iso.org/iso/home/standards/iso8601) standard. Use this class to create ISO 8601 representations of dates and create dates from text strings in ISO 8601 format.

> 💡 **Tip**:  In Swift, you can use [`Date.ISO8601FormatStyle`](./date/iso8601formatstyle.md) rather than [`ISO8601DateFormatter`](./iso8601dateformatter.md). The [`FormatStyle`](./formatstyle.md) API offers a declarative idiom for customizing the formatting of various types. Also, Foundation caches identical [`FormatStyle`](./formatstyle.md) instances, so you don’t need to pass them around your app, or risk wasting memory with duplicate formatters.

## Topics

### Configuring the Formatter
- [var formatOptions: ISO8601DateFormatter.Options](./iso8601dateformatter/formatoptions.md)
  Options for generating and parsing ISO 8601 date representations. See [`ISO8601DateFormatter.Options`](./iso8601dateformatter/options.md) for possible values.
- [var timeZone: TimeZone!](./iso8601dateformatter/timezone.md)
  The time zone used to create and parse date representations. When unspecified, GMT is used.
### Creating ISO 8601 Date Formatters
- [init()](./iso8601dateformatter/init%28%29.md)
  Initializes an ISO 8601 date formatter with default format, time zone, and options.
### Converting ISO 8601 Dates
- [func string(from: Date) -> String](./iso8601dateformatter/string%28from%29.md)
  Creates and returns an ISO 8601 formatted string representation of the specified date.
- [func date(from: String) -> Date?](./iso8601dateformatter/date%28from%29.md)
  Creates and returns a date object from the specified ISO 8601 formatted string representation.
- [class func string(from: Date, timeZone: TimeZone, formatOptions: ISO8601DateFormatter.Options) -> String](./iso8601dateformatter/string%28from,timezone,formatoptions%29.md)
  Creates a representation of the specified date with a given time zone and format options.
### Constants
- [ISO8601DateFormatter.Options](./iso8601dateformatter/options.md)
  Options used to generate and parse ISO 8601 date representations.

## Relationships

### Inherits From
- [Formatter](./formatter.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](./nscoding.md)
- [NSCopying](./nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](./nssecurecoding.md)

## See Also

### Dates and times
- [class DateFormatter](./dateformatter.md)
  A formatter that converts between dates and their textual representations.
- [class DateComponentsFormatter](./datecomponentsformatter.md)
  A formatter that creates string representations of quantities of time.
- [class RelativeDateTimeFormatter](./relativedatetimeformatter.md)
  A formatter that creates locale-aware string representations of a relative date or time.
- [class DateIntervalFormatter](./dateintervalformatter.md)
  A formatter that creates string representations of time intervals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/iso8601dateformatter)*