# Date.AnchoredRelativeFormatStyle

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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
- [init(anchor: Date, allowedFields: Set<Date.AnchoredRelativeFormatStyle.Field>, presentation: Date.AnchoredRelativeFormatStyle.Presentation, unitsStyle: Date.AnchoredRelativeFormatStyle.UnitsStyle, locale: Locale, calendar: Calendar, capitalizationContext: FormatStyleCapitalizationContext)](./anchoredrelativeformatstyle/init%28anchor,allowedfields,presentation,unitsstyle,locale,calendar,capitalizationcontext%29.md)
  Create a relative format style that is detached from the system time, and instead formats an anchor date relative to the format input.
- [init(anchor: Date, presentation: Date.AnchoredRelativeFormatStyle.Presentation, unitsStyle: Date.AnchoredRelativeFormatStyle.UnitsStyle, locale: Locale, calendar: Calendar, capitalizationContext: FormatStyleCapitalizationContext)](./anchoredrelativeformatstyle/init%28anchor,presentation,unitsstyle,locale,calendar,capitalizationcontext%29.md)
  Create a relative format style that is detached from the system time, and instead formats an anchor date relative to the format input.
### Instance Properties
- [var allowedFields: Set<Date.AnchoredRelativeFormatStyle.Field>](./anchoredrelativeformatstyle/allowedfields.md)
  The fields that can be used in the formatted output.
- [var anchor: Date](./anchoredrelativeformatstyle/anchor.md)
  The date the formatted output refers to from the perspective of the input values.
- [var calendar: Calendar](./anchoredrelativeformatstyle/calendar.md)
- [var capitalizationContext: FormatStyleCapitalizationContext](./anchoredrelativeformatstyle/capitalizationcontext.md)
- [var locale: Locale](./anchoredrelativeformatstyle/locale.md)
- [var presentation: Date.AnchoredRelativeFormatStyle.Presentation](./anchoredrelativeformatstyle/presentation-swift.property.md)
- [var unitsStyle: Date.AnchoredRelativeFormatStyle.UnitsStyle](./anchoredrelativeformatstyle/unitsstyle-swift.property.md)
### Type Aliases
- [Date.AnchoredRelativeFormatStyle.Field](./anchoredrelativeformatstyle/field.md)
- [Date.AnchoredRelativeFormatStyle.Presentation](./anchoredrelativeformatstyle/presentation-swift.typealias.md)
- [Date.AnchoredRelativeFormatStyle.UnitsStyle](./anchoredrelativeformatstyle/unitsstyle-swift.typealias.md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/anchoredrelativeformatstyle)*