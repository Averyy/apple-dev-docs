# Date.ComponentsFormatStyle

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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
- [Date.ComponentsFormatStyle.Field](./componentsformatstyle/field.md)
- [Date.ComponentsFormatStyle.Style](./componentsformatstyle/style-swift.struct.md)
### Initializers
- [init(style: Date.ComponentsFormatStyle.Style, locale: Locale, calendar: Calendar, fields: Set<Date.ComponentsFormatStyle.Field>?)](./componentsformatstyle/init%28style,locale,calendar,fields%29.md)
  Shows the date interval with the specified style and the specified date and time fields.
### Instance Properties
- [var calendar: Calendar](./componentsformatstyle/calendar.md)
- [var fields: Set<Date.ComponentsFormatStyle.Field>?](./componentsformatstyle/fields.md)
- [var isPositive: Bool](./componentsformatstyle/ispositive.md)
  Controls whether the format input is formatted as a positive or negative range.
- [var locale: Locale](./componentsformatstyle/locale.md)
- [var style: Date.ComponentsFormatStyle.Style](./componentsformatstyle/style-swift.property.md)
### Instance Methods
- [func calendar(Calendar) -> Date.ComponentsFormatStyle](./componentsformatstyle/calendar%28_%29.md)
### Default Implementations
- [DiscreteFormatStyle Implementations](./componentsformatstyle/discreteformatstyle-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Decodable](../../Swift/decodable.md)
- [DiscreteFormatStyle](../discreteformatstyle.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [FormatStyle](../formatstyle.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Applying date and time styles
- [static var dateTime: Date.FormatStyle](../formatstyle/datetime.md)
  A style for formatting a date and time.
- [struct FormatStyle](./formatstyle.md)
  A structure that creates a locale-appropriate string representation of a date instance and converts strings of dates and times into date instances.
- [struct ISO8601FormatStyle](./iso8601formatstyle.md)
  A type that converts between dates and their ISO-8601 string representations.
- [static func verbatim(Date.FormatString, locale: Locale?, timeZone: TimeZone, calendar: Calendar) -> Date.VerbatimFormatStyle](../formatstyle/verbatim%28_,locale,timezone,calendar%29.md)
  Returns a style for formatting a date with an explicitly-specified style.
- [struct VerbatimFormatStyle](./verbatimformatstyle.md)
  A style that formats a date with an explicitly-specified style.
- [static var interval: Date.IntervalFormatStyle](../formatstyle/interval.md)
  A style for formatting a date interval.
- [struct IntervalFormatStyle](./intervalformatstyle.md)
  A format style that creates string representations of date intervals.
- [static func relative(presentation: Date.RelativeFormatStyle.Presentation, unitsStyle: Date.RelativeFormatStyle.UnitsStyle) -> Self](../formatstyle/relative%28presentation,unitsstyle%29.md)
  Returns a style for formatting a date as relative to the current date.
- [struct RelativeFormatStyle](./relativeformatstyle.md)
  A format style that forms locale-aware string representations of a relative date or time.
- [static func components(style: Date.ComponentsFormatStyle.Style, fields: Set<Date.ComponentsFormatStyle.Field>?) -> Self](../formatstyle/components%28style,fields%29.md)
  Returns a style for formatting a date interval in terms of specific date components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/componentsformatstyle)*