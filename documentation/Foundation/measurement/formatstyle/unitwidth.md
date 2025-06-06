# Measurement.FormatStyle.UnitWidth

**Framework**: Foundation  
**Kind**: struct

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
- [static var wide: Measurement<UnitType>.FormatStyle.UnitWidth](measurement/formatstyle/unitwidth/wide.md)
  A unit width that shows the full unit name.
- [static var abbreviated: Measurement<UnitType>.FormatStyle.UnitWidth](measurement/formatstyle/unitwidth/abbreviated.md)
  An abbreviated unit width.
- [static var narrow: Measurement<UnitType>.FormatStyle.UnitWidth](measurement/formatstyle/unitwidth/narrow.md)
  The shortest unit width.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var width: Measurement<UnitType>.FormatStyle.UnitWidth](measurement/formatstyle/width.md)
  The width of the measurement unit.
- [var numberFormatStyle: FloatingPointFormatStyle<Double>?](measurement/formatstyle/numberformatstyle.md)
  The formatting of the measurement value.
- [var usage: MeasurementFormatUnitUsage<UnitType>?](measurement/formatstyle/usage.md)
  The intended purpose of the formatted measurement.
- [var hidesScaleName: Bool](measurement/formatstyle/hidesscalename.md)
  The visibility of the unit name of a temperature.
- [var locale: Locale](measurement/formatstyle/locale.md)
  The locale of the format style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurement/formatstyle/unitwidth)*