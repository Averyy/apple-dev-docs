# Date.ISO8601FormatStyle

**Framework**: Foundation  
**Kind**: struct

A type that converts between dates and their ISO-8601 string representations.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct ISO8601FormatStyle
```

#### Overview

The [`Date.ISO8601FormatStyle`](date/iso8601formatstyle.md) type generates and parses string representations of dates following the [`ISO-8601`](https://developer.apple.comhttps://www.iso.org/iso-8601-date-and-time-format.html) standard, like `2024-04-01T12:34:56.789Z`. Use this type to create ISO-8601 representations of dates and create dates from text strings in ISO 8601 format. For other formatting conventions, like human-readable, localized date formats, use [`Date.FormatStyle`](date/formatstyle.md).

Instance modifier methods applied to an ISO-8601 format style customize the formatted output, as the following example illustrates.

```swift
let now = Date()
print(now.formatted(Date.ISO8601FormatStyle().dateSeparator(.dash)))
// 2021-06-21T211015Z
```

Use the static factory property `FormatStyle/iso8601` to create an instance of [`Date.ISO8601FormatStyle`](date/iso8601formatstyle.md). Then apply instance modifier methods to customize the format, as in the example below.

```swift
let meetNow = Date()
let formatted = meetNow.formatted(.iso8601
    .year()
    .month()
    .day()
    .timeZone(separator: .omitted)
    .time(includingFractionalSeconds: true)
    .timeSeparator(.colon)
) // "2022-06-10T12:34:56.789Z"

```

## Topics

### Creating an ISO 8601 Format Style
- [init(dateSeparator: Date.ISO8601FormatStyle.DateSeparator, dateTimeSeparator: Date.ISO8601FormatStyle.DateTimeSeparator, timeZone: TimeZone)](date/iso8601formatstyle/init(dateseparator:datetimeseparator:timezone:).md)
  Creates an instance using the provided date separator, date and time components separator, and time zone.
### Modifying an ISO 8601 Format Style
- [var dateSeparator: Date.ISO8601FormatStyle.DateSeparator](date/iso8601formatstyle/dateseparator-swift.property.md)
  The character used to separate the components of a date.
- [var dateTimeSeparator: Date.ISO8601FormatStyle.DateTimeSeparator](date/iso8601formatstyle/datetimeseparator-swift.property.md)
  The character used to separate the date and time components of an ISO 8601 string representation of a date.
- [var timeZone: TimeZone](date/iso8601formatstyle/timezone.md)
  The time zone used to create and parse date representations.
- [func dateTimeSeparator(Date.ISO8601FormatStyle.DateTimeSeparator) -> Date.ISO8601FormatStyle](date/iso8601formatstyle/datetimeseparator(_:).md)
  Sets the character that specifies the date and time components.
### Modifying Dates in an ISO 8601 Format Style
- [func dateSeparator(Date.ISO8601FormatStyle.DateSeparator) -> Date.ISO8601FormatStyle](date/iso8601formatstyle/dateseparator(_:).md)
  Modifies the ISO 8601 date format style to use the specified date separator.
- [func year() -> Date.ISO8601FormatStyle](date/iso8601formatstyle/year.md)
  Modifies the ISO 8601 date format style to include the year in the formatted output.
- [func month() -> Date.ISO8601FormatStyle](date/iso8601formatstyle/month.md)
  Modifies the ISO 8601 date format style to include the month in the formatted output.
- [func weekOfYear() -> Date.ISO8601FormatStyle](date/iso8601formatstyle/weekofyear.md)
  Modifies the ISO 8601 date format style to include the week of the year in the formatted output.
- [func day() -> Date.ISO8601FormatStyle](date/iso8601formatstyle/day.md)
  Modifies the ISO 8601 date format style to include the day in the formatted output.
### Modifying Times in an ISO 8601 Format Style
- [func time(includingFractionalSeconds: Bool) -> Date.ISO8601FormatStyle](date/iso8601formatstyle/time(includingfractionalseconds:).md)
  Modifies the ISO 8601 date format style to include the time in the formatted output.
- [func timeSeparator(Date.ISO8601FormatStyle.TimeSeparator) -> Date.ISO8601FormatStyle](date/iso8601formatstyle/timeseparator(_:).md)
  Modifies the ISO 8601 date format style to use the specified time separator.
- [func timeZone(separator: Date.ISO8601FormatStyle.TimeZoneSeparator) -> Date.ISO8601FormatStyle](date/iso8601formatstyle/timezone(separator:).md)
  Modifies the ISO 8601 date format style to include the time zone in the formatted output.
- [func timeZoneSeparator(Date.ISO8601FormatStyle.TimeZoneSeparator) -> Date.ISO8601FormatStyle](date/iso8601formatstyle/timezoneseparator(_:).md)
  Modifies the ISO 8601 date format style to use the specified time zone separator.
### Comparing ISO 8601 Format Styles
- [static func != (Self, Self) -> Bool](date/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [static func == (Date, Date) -> Bool](date/==(_:_:).md)
  Returns true if the two `Date` values represent the same point in time.
### Supporting Types
- [Date.ISO8601FormatStyle.DateSeparator](date/iso8601formatstyle/dateseparator-swift.enum.md)
  A type describing the character separating year, month, and day components of a date in an ISO 8601 date format.
- [Date.ISO8601FormatStyle.DateTimeSeparator](date/iso8601formatstyle/datetimeseparator-swift.enum.md)
  Type describing the character separating the date and time components of a date in an ISO 8601 date format.
- [Date.ISO8601FormatStyle.TimeSeparator](date/iso8601formatstyle/timeseparator-swift.enum.md)
  Type describing the character separating the time components of a date in an ISO 8601 date format.
- [Date.ISO8601FormatStyle.TimeZoneSeparator](date/iso8601formatstyle/timezoneseparator-swift.enum.md)
  A type describing the character separating the time and time zone of a date in an ISO 8601 date format.
### Initializers
- [init(dateSeparator: Date.ISO8601FormatStyle.DateSeparator, dateTimeSeparator: Date.ISO8601FormatStyle.DateTimeSeparator, timeSeparator: Date.ISO8601FormatStyle.TimeSeparator, timeZoneSeparator: Date.ISO8601FormatStyle.TimeZoneSeparator, includingFractionalSeconds: Bool, timeZone: TimeZone)](date/iso8601formatstyle/init(dateseparator:datetimeseparator:timeseparator:timezoneseparator:includingfractionalseconds:timezone:).md)
### Instance Properties
- [var includingFractionalSeconds: Bool](date/iso8601formatstyle/includingfractionalseconds.md)
- [var timeSeparator: Date.ISO8601FormatStyle.TimeSeparator](date/iso8601formatstyle/timeseparator-swift.property.md)
- [var timeZoneSeparator: Date.ISO8601FormatStyle.TimeZoneSeparator](date/iso8601formatstyle/timezoneseparator-swift.property.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomConsumingRegexComponent](../Swift/CustomConsumingRegexComponent.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [FormatStyle](formatstyle.md)
- [Hashable](../Swift/Hashable.md)
- [ParseStrategy](parsestrategy.md)
- [ParseableFormatStyle](parseableformatstyle.md)
- [RegexComponent](../Swift/RegexComponent.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static var dateTime: Date.FormatStyle](formatstyle/datetime.md)
  A style for formatting a date and time.
- [struct FormatStyle](date/formatstyle.md)
  A structure that creates a locale-appropriate string representation of a date instance and converts strings of dates and times into date instances.
- [static func verbatim(Date.FormatString, locale: Locale?, timeZone: TimeZone, calendar: Calendar) -> Date.VerbatimFormatStyle](formatstyle/verbatim(_:locale:timezone:calendar:).md)
  Returns a style for formatting a date with an explicitly-specified style.
- [struct VerbatimFormatStyle](date/verbatimformatstyle.md)
  A style that formats a date with an explicitly-specified style.
- [static var interval: Date.IntervalFormatStyle](formatstyle/interval.md)
  A style for formatting a date interval.
- [struct IntervalFormatStyle](date/intervalformatstyle.md)
  A format style that creates string representations of date intervals.
- [static func relative(presentation: Date.RelativeFormatStyle.Presentation, unitsStyle: Date.RelativeFormatStyle.UnitsStyle) -> Self](formatstyle/relative(presentation:unitsstyle:).md)
  Returns a style for formatting a date as relative to the current date.
- [struct RelativeFormatStyle](date/relativeformatstyle.md)
  A format style that forms locale-aware string representations of a relative date or time.
- [static func components(style: Date.ComponentsFormatStyle.Style, fields: Set<Date.ComponentsFormatStyle.Field>?) -> Self](formatstyle/components(style:fields:).md)
  Returns a style for formatting a date interval in terms of specific date components.
- [struct ComponentsFormatStyle](date/componentsformatstyle.md)
  A style for formatting a date interval in terms of specific date components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/iso8601formatstyle)*