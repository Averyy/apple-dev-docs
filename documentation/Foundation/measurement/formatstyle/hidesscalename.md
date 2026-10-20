# hidesScaleName

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The visibility of the unit name of a temperature.

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
var hidesScaleName: Bool { get set }
```

Available when `UnitType` is `UnitTemperature`.

#### Discussion

Set `hidesScaleName` to `true` to exclude the unit name from a formatted temperature string. For example, `90°` rather than `90°F` or `90°C` with the [`narrow`](./unitwidth/narrow.md) unit width, or `90 degrees` rather than `90 degrees Celcius` or `90 degrees Fahrenheit` with the [`wide`](./unitwidth/wide.md) width.

Hiding the unit name only affects the presentation of the measurement. Unless you specify `asProvided` as the `usage`, the system converts the temperature to the unit that the locale uses.

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
- [var locale: Locale](./locale.md)
  The locale of the format style.
- [func locale(Locale) -> Measurement<UnitType>.FormatStyle](./locale%28_%29.md)
  Modifies the measurement format style to use the specified locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurement/formatstyle/hidesscalename)*