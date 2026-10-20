# Date.VerbatimFormatStyle

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

A style that formats a date with an explicitly-specified style.

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
struct VerbatimFormatStyle
```

## Topics

### Structures
- [Date.VerbatimFormatStyle.Attributed](./verbatimformatstyle/attributed-swift.struct.md)
  The type preserving attributed variant of this style.
### Initializers
- [init(format: Date.FormatString, locale: Locale?, timeZone: TimeZone, calendar: Calendar)](./verbatimformatstyle/init%28format,locale,timezone,calendar%29.md)
### Instance Properties
- [var attributed: Date.AttributedStyle](./verbatimformatstyle/attributed-swift.property.md)
  Returns a type erased attributed variant of this style.
- [var attributedStyle: Date.VerbatimFormatStyle.Attributed](./verbatimformatstyle/attributedstyle.md)
  Return the type preserving attributed variant of this style.
- [var calendar: Calendar](./verbatimformatstyle/calendar.md)
- [var locale: Locale?](./verbatimformatstyle/locale.md)
  Use system locale if nil or unspecified.
- [var timeZone: TimeZone](./verbatimformatstyle/timezone.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomConsumingRegexComponent](../../Swift/customconsumingregexcomponent.md)
- [Decodable](../../Swift/decodable.md)
- [DiscreteFormatStyle](../discreteformatstyle.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [FormatStyle](../formatstyle.md)
- [Hashable](../../Swift/hashable.md)
- [ParseableFormatStyle](../parseableformatstyle.md)
- [RegexComponent](../../Swift/regexcomponent.md)
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
- [struct ComponentsFormatStyle](./componentsformatstyle.md)
  A style for formatting a date interval in terms of specific date components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/verbatimformatstyle)*