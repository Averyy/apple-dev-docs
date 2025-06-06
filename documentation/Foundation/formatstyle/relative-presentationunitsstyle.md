# relative(presentation:unitsStyle:)

**Framework**: Foundation  
**Kind**: method

Returns a style for formatting a date as relative to the current date.

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
static func relative(presentation: Date.RelativeFormatStyle.Presentation, unitsStyle: Date.RelativeFormatStyle.UnitsStyle = .wide) -> Self
```

#### Return Value

A relative date format style customized with the specified presentation and unit styles.

#### Discussion

Use this static method when the call point allows the use of [`Date.RelativeFormatStyle`](date/relativeformatstyle.md). You typically do this when calling the [`formatted(_:)`](date/formatted(_:).md) method of [`Date`](date.md).

The following example shows the [`relative(presentation:unitsStyle:)`](formatstyle/relative(presentation:unitsstyle:).md) relative format style with two different presentations.

```swift
if let past = Calendar.current.date(byAdding: .day, value: -7, to: Date()) {
    let formattedNumeric = past.formatted(
        .relative(presentation: .numeric)) // "1 week ago"
    let formattedNamed = past.formatted(
        .relative(presentation: .named)) // "last week"
}
```

## Parameters

- `presentation`: The style to use when describing a relative date; for example, “1 day ago” or “yesterday”.
- `unitsStyle`: The style to use when formatting the quantity or the name of the unit; for example, “1 day ago” or “one day ago”.

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
- [struct RelativeFormatStyle](date/relativeformatstyle.md)
  A format style that forms locale-aware string representations of a relative date or time.
- [static func components(style: Date.ComponentsFormatStyle.Style, fields: Set<Date.ComponentsFormatStyle.Field>?) -> Self](formatstyle/components(style:fields:).md)
  Returns a style for formatting a date interval in terms of specific date components.
- [struct ComponentsFormatStyle](date/componentsformatstyle.md)
  A style for formatting a date interval in terms of specific date components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/formatstyle/relative(presentation:unitsstyle:))*