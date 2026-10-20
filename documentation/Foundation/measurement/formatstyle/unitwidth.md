# Measurement.FormatStyle.UnitWidth

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

Specifies the width of the unit, determining the textual representation.

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
struct UnitWidth
```

## Topics

### Unit widths
- [static var wide: Measurement<UnitType>.FormatStyle.UnitWidth](./unitwidth/wide.md)
  A unit width that shows the full unit name.
- [static var abbreviated: Measurement<UnitType>.FormatStyle.UnitWidth](./unitwidth/abbreviated.md)
  An abbreviated unit width.
- [static var narrow: Measurement<UnitType>.FormatStyle.UnitWidth](./unitwidth/narrow.md)
  The shortest unit width.

## Relationships

### Conforms To
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Modifying a measurement format style
- [var width: Measurement<UnitType>.FormatStyle.UnitWidth](./width.md)
  The width of the measurement unit.
- [var numberFormatStyle: FloatingPointFormatStyle<Double>?](./numberformatstyle.md)
  The formatting of the measurement value.
- [var usage: MeasurementFormatUnitUsage<UnitType>?](./usage.md)
  The intended purpose of the formatted measurement.
- [var hidesScaleName: Bool](./hidesscalename.md)
  The visibility of the unit name of a temperature.
- [var locale: Locale](./locale.md)
  The locale of the format style.
- [func locale(Locale) -> Measurement<UnitType>.FormatStyle](./locale%28_%29.md)
  Modifies the measurement format style to use the specified locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurement/formatstyle/unitwidth)*