# usage

**Framework**: Foundation  
**Kind**: property

The intended purpose of the formatted measurement.

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
var usage: MeasurementFormatUnitUsage<UnitType>?
```

#### Discussion

You can use the `usage` property to specify the intended purpose of the formatted measurement. The default option, `general`, formats the measurement with the default unit for the current locale. The `asProvided` option formats the measurement using the specified unit, ignoring the unit that the locale uses.

The following example shows a formatted temperature using the default unit for the `en_US` locale and using a provided Celsius unit:

```swift
let temperature = Measurement<UnitTemperature>(value: 36.8, unit: .celsius)
temperature.formatted()
// 98°F

temperature.formatted(.measurement(width: .abbreviated, usage: .asProvided))
// 36.8°C
```

All unit types have `general` and `asProvided` options. Some subclasses have additional options, such as the following:

[`UnitTemperature`](unittemperature.md)

- `person`
- `weather`

[`UnitLength`](unitlength.md)

- `person`
- `personHeight`
- `road`

[`UnitEnergy`](unitenergy.md)

- `food`
- `workout`

[`UnitMass`](unitmass.md)

- `personWeight`

## See Also

- [var width: Measurement<UnitType>.FormatStyle.UnitWidth](measurement/formatstyle/width.md)
  The width of the measurement unit.
- [Measurement.FormatStyle.UnitWidth](measurement/formatstyle/unitwidth.md)
  Specifies the width of the unit, determining the textual representation.
- [var numberFormatStyle: FloatingPointFormatStyle<Double>?](measurement/formatstyle/numberformatstyle.md)
  The formatting of the measurement value.
- [var hidesScaleName: Bool](measurement/formatstyle/hidesscalename.md)
  The visibility of the unit name of a temperature.
- [var locale: Locale](measurement/formatstyle/locale.md)
  The locale of the format style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurement/formatstyle/usage)*