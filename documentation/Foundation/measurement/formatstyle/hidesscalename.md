# hidesScaleName

**Framework**: Foundation  
**Kind**: property

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

#### Discussion

Set `hidesScaleName` to `true` to exclude the unit name from a formatted temperature string. For example, `90°` rather than `90°F` or `90°C` with the [`narrow`](measurement/formatstyle/unitwidth/narrow.md) unit width, or `90 degrees` rather than `90 degrees Celcius` or `90 degrees Fahrenheit` with the [`wide`](measurement/formatstyle/unitwidth/wide.md) width.

Hiding the unit name only affects the presentation of the measurement. Unless you specify `asProvided` as the `usage`, the system converts the temperature to the unit that the locale uses.

## See Also

- [var width: Measurement<UnitType>.FormatStyle.UnitWidth](measurement/formatstyle/width.md)
  The width of the measurement unit.
- [Measurement.FormatStyle.UnitWidth](measurement/formatstyle/unitwidth.md)
  Specifies the width of the unit, determining the textual representation.
- [var numberFormatStyle: FloatingPointFormatStyle<Double>?](measurement/formatstyle/numberformatstyle.md)
  The formatting of the measurement value.
- [var usage: MeasurementFormatUnitUsage<UnitType>?](measurement/formatstyle/usage.md)
  The intended purpose of the formatted measurement.
- [var locale: Locale](measurement/formatstyle/locale.md)
  The locale of the format style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurement/formatstyle/hidesscalename)*