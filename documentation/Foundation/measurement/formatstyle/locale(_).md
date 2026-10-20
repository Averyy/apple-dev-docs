# locale(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Modifies the measurement format style to use the specified locale.

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
func locale(_ locale: Locale) -> Measurement<UnitType>.FormatStyle
```

#### Return Value

A measurement format style with the specified locale.

## Parameters

- `locale`: The locale to use when formatting a measurement.

## See Also

### Modifying a measurement format style
- [var width: Measurement<UnitType>.FormatStyle.UnitWidth](./width.md)
  The width of the measurement unit.
- [Measurement.FormatStyle.UnitWidth](./unitwidth.md)
  Specifies the width of the unit, determining the textual representation.
- [var numberFormatStyle: FloatingPointFormatStyle<Double>?](./numberformatstyle.md)
  The formatting of the measurement value.
- [var usage: MeasurementFormatUnitUsage<UnitType>?](./usage.md)
  The intended purpose of the formatted measurement.
- [var hidesScaleName: Bool](./hidesscalename.md)
  The visibility of the unit name of a temperature.
- [var locale: Locale](./locale.md)
  The locale of the format style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurement/formatstyle/locale(_:))*