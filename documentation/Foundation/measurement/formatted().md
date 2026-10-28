# formatted()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Generates a locale-aware string representation of a measurement using the default measurement format style.

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
func formatted() -> String
```

Available when `UnitType` inherits `Dimension`.

## Return Value

A string, formatted according to the default style.

## Discussion

Use the [`formatted()`](./formatted%28%29.md) method to apply the default format style to a measurement, such as in the following example:

```swift
let string = Measurement<UnitTemperature>(value: 38, unit: .celsius).formatted()
// For locale: en_US: 100.4°F
```

The default measurement format style uses an [`abbreviated`](./formatstyle/unitwidth/abbreviated.md) unit width, the general usage type, and the default number format style. To customize the formatted measurement string, use the [`formatted(_:)`](./formatted%28_%29.md) method and include a [`Measurement.FormatStyle`](./formatstyle.md).

## See Also

### Formatting a Measurement
- [func formatted<S>(S) -> S.FormatOutput](./formatted%28_%29.md)
  Generates a locale-aware string representation of a measurement using the provided measurement format style.
- [Measurement.FormatStyle](./formatstyle.md)
  A type that provides localized representations of measurements.
- [Measurement.AttributedStyle](./attributedstyle.md)
  A type that provides localized representations of measurements with an attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurement/formatted())*