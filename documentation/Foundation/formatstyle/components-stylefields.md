# components(style:fields:)

**Framework**: Foundation  
**Kind**: method

Returns a style for formatting a date interval in terms of specific date components.

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
static func components(style: Date.ComponentsFormatStyle.Style, fields: Set<Date.ComponentsFormatStyle.Field>? = nil) -> Self
```

#### Return Value

A date format style that uses the specified style and fields.

#### Discussion

Use this type method when the call point allows the use of [`Date.ComponentsFormatStyle`](date/componentsformatstyle.md). You typically do this when calling the [`formatted(_:)`](https://developer.apple.com/documentation/Swift/Range/formatted(_:)) method of a `Range<Date>`.

The following example creates a 120-day date range, and then uses a [`Date.ComponentsFormatStyle`](date/componentsformatstyle.md) to express this as a count of weeks and days:

```swift
let date = Date()
let futureDate = Calendar.current.date(byAdding: .day, value: 120, to: date)!
let interval = (date..<futureDate)
let formatted = interval.formatted(
    .components(style: .wide,
                fields: [.week, .day])) // 17 weeks, 1 day
```

## Parameters

- `style`: The style to use for the fields, such as   or  .
- `fields`: A set of date component fields to include in the formatted output.

## See Also

- [static var dateTime: Date.FormatStyle](formatstyle/datetime.md)
  A style for formatting a date and time.
- [struct FormatStyle](date/formatstyle.md)
  A structure that creates a locale-appropriate string representation of a date instance and converts strings of dates and times into date instances.
- [static var iso8601: Date.ISO8601FormatStyle](formatstyle/iso8601.md)
  A style for formatting a date in accordance with the ISO-8601 standard.
- [struct ISO8601FormatStyle](date/iso8601formatstyle.md)
  A type that converts between dates and their ISO-8601 string representations.
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
- [struct ComponentsFormatStyle](date/componentsformatstyle.md)
  A style for formatting a date interval in terms of specific date components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/formatstyle/components(style:fields:))*