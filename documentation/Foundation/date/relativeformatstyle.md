# Date.RelativeFormatStyle

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

A format style that forms locale-aware string representations of a relative date or time.

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
struct RelativeFormatStyle
```

#### Overview

Use the strings that the format style produces, such as “1 hour ago”, “in 2 weeks”, “yesterday”, and “tomorrow” as standalone strings. Embedding them in other strings may not be grammatically correct.

Express relative date formats in either [`numeric`](./relativeformatstyle/presentation-swift.struct/numeric.md) or [`named`](./relativeformatstyle/presentation-swift.struct/named.md) styles. For example:

```swift
if let past = Calendar.current.date(byAdding: .day, value: -7, to: Date()) {
    var formatStyle = Date.RelativeFormatStyle()
    
    formatStyle.presentation = .numeric
    past.formatted(formatStyle) // "1 week ago"
    
    formatStyle.presentation = .named
    past.formatted(formatStyle) // "last week"
}
```

Use the convenient static factory method [`relative(presentation:unitsStyle:)`](../formatstyle/relative%28presentation,unitsstyle%29.md) to shorten the syntax when applying presentation and units style modifiers to customize the format. For example:

```swift
if let past = Calendar.current.date(byAdding: .day, value: 7, to: Date()) {

    past.formatted(.relative(presentation: .numeric)) // "in 1 week"
    past.formatted(.relative(presentation: .named)) // "next week"

    past.formatted(.relative(presentation: .named, unitsStyle: .wide)) // "next week"
    past.formatted(.relative(presentation: .named, unitsStyle: .narrow)) // "next wk."
    past.formatted(.relative(presentation: .named, unitsStyle: .abbreviated)) // "next wk."
    past.formatted(.relative(presentation: .named, unitsStyle: .spellOut)) // "next week"
    past.formatted(.relative(presentation: .numeric, unitsStyle: .wide)) // "in 1 week"
    past.formatted(.relative(presentation: .numeric, unitsStyle: .narrow)) // "in 1 wk."
    past.formatted(.relative(presentation: .numeric, unitsStyle: .abbreviated)) // "in 1 wk."
    past.formatted(.relative(presentation: .numeric, unitsStyle: .spellOut)) // "in one week"
}
```

The [`format(_:)`](./formatstyle/format%28_%29.md) instance method generates a string from the provided relative date. Once you create a style, you can use it to format relative dates multiple times.

The following example applies a format style repeatedly to produce string representations of relative dates:

```swift
if let pastWeek = Calendar.current.date(byAdding: .day, value: -7, to: Date()), 
  let pastDay = Calendar.current.date(byAdding: .day, value: -1, to: Date()) {

    let formatStyle = Date.RelativeFormatStyle(
        presentation: .named,
        unitsStyle: .spellOut,
        locale: Locale(identifier: "en_GB"),
        calendar: Calendar.current,
        capitalizationContext: .beginningOfSentence)
        
    formatStyle.format(pastDay) // "Yesterday"
    formatStyle.format(pastWeek) // "Last week"
}
```

## Topics

### Creating a Relative Date Format Style
- [init(presentation: Date.RelativeFormatStyle.Presentation, unitsStyle: Date.RelativeFormatStyle.UnitsStyle, locale: Locale, calendar: Calendar, capitalizationContext: FormatStyleCapitalizationContext)](./relativeformatstyle/init%28presentation,unitsstyle,locale,calendar,capitalizationcontext%29.md)
  Creates a relative date format style with the specified presentation, units, locale, calendar, and capitalization context.
### Modifying a Relative Date Format Style
- [var presentation: Date.RelativeFormatStyle.Presentation](./relativeformatstyle/presentation-swift.property.md)
  Specifies the style to use when describing a relative date, such as “1 day ago” or “yesterday”.
- [var unitsStyle: Date.RelativeFormatStyle.UnitsStyle](./relativeformatstyle/unitsstyle-swift.property.md)
  The style to use when formatting the quantity or the name of the unit, such as “1 day ago” or “one day ago”.
- [var calendar: Calendar](./relativeformatstyle/calendar.md)
  The calendar to use when formatting relative dates.
- [var capitalizationContext: FormatStyleCapitalizationContext](./relativeformatstyle/capitalizationcontext.md)
  The capitalization context to use when formatting the relative dates.
- [var locale: Locale](./relativeformatstyle/locale.md)
  The locale to use when formatting the relative date.
- [func locale(Locale) -> Date.RelativeFormatStyle](./relativeformatstyle/locale%28_%29.md)
  Modifies the relative date format style to use the specified locale.
### Formatting a Relative Date
- [func format(Date) -> String](./relativeformatstyle/format%28_%29.md)
  Creates a locale-aware string representation from a relative date value.
### Comparing Relative Date Format Styles
- [static func == (Date, Date) -> Bool](./eqeq%28_,_%29.md)
  Returns true if the two `Date` values represent the same point in time.
### Supporting Types
- [Date.RelativeFormatStyle.Presentation](./relativeformatstyle/presentation-swift.struct.md)
  A type that represents the style to use when formatting relative dates, such as “1 week ago” or “last week”.
- [Date.RelativeFormatStyle.UnitsStyle](./relativeformatstyle/unitsstyle-swift.struct.md)
  A type that represents the style to use when formatting the units of relative dates.
### Initializers
- [init(allowedFields: Set<Date.RelativeFormatStyle.Field>, presentation: Date.RelativeFormatStyle.Presentation, unitsStyle: Date.RelativeFormatStyle.UnitsStyle, locale: Locale, calendar: Calendar, capitalizationContext: FormatStyleCapitalizationContext)](./relativeformatstyle/init%28allowedfields,presentation,unitsstyle,locale,calendar,capitalizationcontext%29.md)
### Instance Properties
- [var allowedFields: Set<Date.RelativeFormatStyle.Field>](./relativeformatstyle/allowedfields.md)
  The fields that can be used in the formatted output.
### Type Aliases
- [Date.RelativeFormatStyle.Field](./relativeformatstyle/field.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Decodable](../../Swift/decodable.md)
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
- [static func components(style: Date.ComponentsFormatStyle.Style, fields: Set<Date.ComponentsFormatStyle.Field>?) -> Self](../formatstyle/components%28style,fields%29.md)
  Returns a style for formatting a date interval in terms of specific date components.
- [struct ComponentsFormatStyle](./componentsformatstyle.md)
  A style for formatting a date interval in terms of specific date components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/relativeformatstyle)*