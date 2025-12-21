# Date.ComponentsFormatStyle

**Framework**: Foundation  
**Kind**: struct

A style for formatting a date interval in terms of specific date components.

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
struct ComponentsFormatStyle
```

## Topics

### Structures
- [Date.ComponentsFormatStyle.Field](date/componentsformatstyle/field.md)
- [Date.ComponentsFormatStyle.Style](date/componentsformatstyle/style-swift.struct.md)
### Initializers
- [init(style: Date.ComponentsFormatStyle.Style, locale: Locale, calendar: Calendar, fields: Set<Date.ComponentsFormatStyle.Field>?)](date/componentsformatstyle/init(style:locale:calendar:fields:).md)
  Shows the date interval with the specified style and the specified date and time fields.
### Instance Properties
- [var calendar: Calendar](date/componentsformatstyle/calendar.md)
- [var fields: Set<Date.ComponentsFormatStyle.Field>?](date/componentsformatstyle/fields.md)
- [var isPositive: Bool](date/componentsformatstyle/ispositive.md)
  Controls whether the format input is formatted as a positive or negative range.
- [var locale: Locale](date/componentsformatstyle/locale.md)
- [var style: Date.ComponentsFormatStyle.Style](date/componentsformatstyle/style-swift.property.md)
### Instance Methods
- [func calendar(Calendar) -> Date.ComponentsFormatStyle](date/componentsformatstyle/calendar(_:).md)
### Default Implementations
- [DiscreteFormatStyle Implementations](date/componentsformatstyle/discreteformatstyle-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [DiscreteFormatStyle](discreteformatstyle.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [FormatStyle](formatstyle.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static var dateTime: Date.FormatStyle](formatstyle/datetime.md)
  A style for formatting a date and time.
- [struct FormatStyle](date/formatstyle.md)
  A structure that creates a locale-appropriate string representation of a date instance and converts strings of dates and times into date instances.
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
- [static func components(style: Date.ComponentsFormatStyle.Style, fields: Set<Date.ComponentsFormatStyle.Field>?) -> Self](formatstyle/components(style:fields:).md)
  Returns a style for formatting a date interval in terms of specific date components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/componentsformatstyle)*