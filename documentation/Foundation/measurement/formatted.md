# formatted(_:)

**Framework**: Foundation  
**Kind**: method

Generates a locale-aware string representation of a measurement using the provided measurement format style.

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
func formatted<S>(_ style: S) -> S.FormatOutput where S : FormatStyle, S.FormatInput == Measurement<UnitType>
```

#### Return Value

A string, formatted according to the provided style.

#### Discussion

Use the [`formatted(_:)`](measurement/formatted(_:).md) method to create a string representation of a measurement using a custom measurement format style. You can specify the width of the unit name, the numeric formatting of the value, and the intended usage type of the measurement. You can use the [`Measurement.FormatStyle`](measurement/formatstyle.md) static factory method `measurement(width:usage:numberFormat:)` to create a custom format style as a parameter to the method, such as in the following example:

```swift
let temp = Measurement<UnitTemperature>(value: 38, unit: .celsius)
let formattedTemp = temp.formatted(.measurement(width: .wide, usage: .weather, numberFormat: .numeric(precision: .fractionLength(1))))
// For locale: en_US: 100.4 degrees Fahrenheit
```

## Parameters

- `style`: The measurement format style to apply to the measurement.

## See Also

- [func formatted() -> String](measurement/formatted.md)
  Generates a locale-aware string representation of a measurement using the default measurement format style.
- [Measurement.FormatStyle](measurement/formatstyle.md)
  A type that provides localized representations of measurements.
- [Measurement.AttributedStyle](measurement/attributedstyle.md)
  A type that provides localized representations of measurements with an attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurement/formatted(_:))*