# width

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The width of the measurement unit.

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
var width: Measurement<UnitType>.FormatStyle.UnitWidth
```

## Discussion

The `width` property specifies the display of the measurement unit. The possible values are [`abbreviated`](./unitwidth/abbreviated.md), [`narrow`](./unitwidth/narrow.md), and [`wide`](./unitwidth/wide.md). The format style represents the unit in the shortest notation available.

The following example shows *100 degrees Fahrenheit* in each width for the `en_US` locale.

```swift
let temperatureMeasurement = Measurement<UnitTemperature>(value: 100, unit: .fahrenheit)
temperatureMeasurement.formatted(.measurement(width: .wide)) // 100 degrees Fahrenheit
temperatureMeasurement.formatted(.measurement(width: .abbreviated)) // 100°F
temperatureMeasurement.formatted(.measurement(width: .narrow)) // 100°
```

## See Also

### Modifying a measurement format style
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
- [func locale(Locale) -> Measurement<UnitType>.FormatStyle](./locale%28_%29.md)
  Modifies the measurement format style to use the specified locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurement/formatstyle/width)*