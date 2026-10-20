# locale

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The locale of the format style.

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
var locale: Locale
```

#### Discussion

By default, the format style displays a measurement in the unit that `locale` specifies. The default value is [`autoupdatingCurrent`](../../locale/autoupdatingcurrent.md).

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
- [func locale(Locale) -> Measurement<UnitType>.FormatStyle](./locale%28_%29.md)
  Modifies the measurement format style to use the specified locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurement/formatstyle/locale)*