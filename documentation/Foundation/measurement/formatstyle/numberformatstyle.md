# numberFormatStyle

**Framework**: Foundation  
**Kind**: property

The formatting of the measurement value.

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
var numberFormatStyle: FloatingPointFormatStyle<Double>?
```

#### Discussion

The `numberFormat` property specifies the formatting of the measurement value. You can customize the precision, grouping, and rounding mode of the measurement by creating a numeric number format style.

The following example shows a customized measurement format style that includes two decimal numbers and excludes separators:

```swift
let volume = Measurement<UnitVolume>(value: 2300, unit: .milliliters)
volume.formatted(.measurement(width: .abbreviated,
                              usage: .asProvided,
                              numberFormatStyle: .number
                                  .precision(.fractionLength(2))
                                  .grouping(.never))) // "2300.00 mL"
```

## See Also

- [var width: Measurement<UnitType>.FormatStyle.UnitWidth](measurement/formatstyle/width.md)
  The width of the measurement unit.
- [Measurement.FormatStyle.UnitWidth](measurement/formatstyle/unitwidth.md)
  Specifies the width of the unit, determining the textual representation.
- [var usage: MeasurementFormatUnitUsage<UnitType>?](measurement/formatstyle/usage.md)
  The intended purpose of the formatted measurement.
- [var hidesScaleName: Bool](measurement/formatstyle/hidesscalename.md)
  The visibility of the unit name of a temperature.
- [var locale: Locale](measurement/formatstyle/locale.md)
  The locale of the format style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurement/formatstyle/numberformatstyle)*