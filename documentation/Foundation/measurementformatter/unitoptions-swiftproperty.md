# unitOptions

**Framework**: Foundation  
**Kind**: property

The options for how the unit is formatted.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var unitOptions: MeasurementFormatter.UnitOptions { get set }
```

#### Discussion

You can set this property to ensure that the formatter chooses the preferred unit to format for the measurement based on the formatter’s locale. For possible values, see [`MeasurementFormatter.UnitOptions`](measurementformatter/unitoptions-swift.struct.md).

If no options are specified, the formatter localizes according to the preferences of the formatter’s [`locale`](measurementformatter/locale.md). For example, a measurement in kilocalories may be formatted as `C` instead of `kcal`, or a measurement in kilometers per hour may be formatted as `miles per hour` for US and UK locales, but `kilometers per hour` for other locales. However, if the `providedUnit` option is specified, a measurement with [`kilocalories`](unitenergy/kilocalories.md) units would be formatted as `kcal`, even if the locale prefers `C`, and a measurement with [`kilometersPerHour`](unitspeed/kilometersperhour.md) units would be formatted as `kilometers per hour` for US and UK locales, even though they prefer `miles per hour`.

> **Note**:  `NSMeasurementFormatter` handles the conversion of measurements to the preferred units in a particular locale when this option is specified. For example, if provided a measurement object in kilojoules, the formatter implicitly converts the measurement object to kilocalories and returns the formatted string as the equivalent measurement in kilocalories.

## See Also

- [MeasurementFormatter.UnitOptions](measurementformatter/unitoptions-swift.struct.md)
  Measurement formatter options.
- [var unitStyle: Formatter.UnitStyle](measurementformatter/unitstyle.md)
  The unit style.
- [var locale: Locale!](measurementformatter/locale.md)
  The locale of the formatter.
- [var numberFormatter: NumberFormatter!](measurementformatter/numberformatter.md)
  The number formatter used to format the quantity of a measurement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurementformatter/unitoptions-swift.property)*