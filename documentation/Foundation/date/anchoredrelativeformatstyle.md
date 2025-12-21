# Date.AnchoredRelativeFormatStyle

**Framework**: Foundation  
**Kind**: struct

A relative format style that is detached from the system time, and instead formats an anchor date relative to the format input.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
struct AnchoredRelativeFormatStyle
```

## Topics

### Initializers
- [init(anchor: Date, allowedFields: Set<Date.AnchoredRelativeFormatStyle.Field>, presentation: Date.AnchoredRelativeFormatStyle.Presentation, unitsStyle: Date.AnchoredRelativeFormatStyle.UnitsStyle, locale: Locale, calendar: Calendar, capitalizationContext: FormatStyleCapitalizationContext)](date/anchoredrelativeformatstyle/init(anchor:allowedfields:presentation:unitsstyle:locale:calendar:capitalizationcontext:).md)
  Create a relative format style that is detached from the system time, and instead formats an anchor date relative to the format input.
- [init(anchor: Date, presentation: Date.AnchoredRelativeFormatStyle.Presentation, unitsStyle: Date.AnchoredRelativeFormatStyle.UnitsStyle, locale: Locale, calendar: Calendar, capitalizationContext: FormatStyleCapitalizationContext)](date/anchoredrelativeformatstyle/init(anchor:presentation:unitsstyle:locale:calendar:capitalizationcontext:).md)
  Create a relative format style that is detached from the system time, and instead formats an anchor date relative to the format input.
### Instance Properties
- [var allowedFields: Set<Date.AnchoredRelativeFormatStyle.Field>](date/anchoredrelativeformatstyle/allowedfields.md)
  The fields that can be used in the formatted output.
- [var anchor: Date](date/anchoredrelativeformatstyle/anchor.md)
  The date the formatted output refers to from the perspective of the input values.
- [var calendar: Calendar](date/anchoredrelativeformatstyle/calendar.md)
- [var capitalizationContext: FormatStyleCapitalizationContext](date/anchoredrelativeformatstyle/capitalizationcontext.md)
- [var locale: Locale](date/anchoredrelativeformatstyle/locale.md)
- [var presentation: Date.AnchoredRelativeFormatStyle.Presentation](date/anchoredrelativeformatstyle/presentation-swift.property.md)
- [var unitsStyle: Date.AnchoredRelativeFormatStyle.UnitsStyle](date/anchoredrelativeformatstyle/unitsstyle-swift.property.md)
### Type Aliases
- [Date.AnchoredRelativeFormatStyle.Field](date/anchoredrelativeformatstyle/field.md)
- [Date.AnchoredRelativeFormatStyle.Presentation](date/anchoredrelativeformatstyle/presentation-swift.typealias.md)
- [Date.AnchoredRelativeFormatStyle.UnitsStyle](date/anchoredrelativeformatstyle/unitsstyle-swift.typealias.md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/anchoredrelativeformatstyle)*