# currency

**Framework**: Foundation  
**Kind**: property

The currency used by the locale.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var currency: Locale.Currency? { get }
```

#### Discussion

This property corresponds to the `cu` key of the Unicode BCP 47 extension.

For locale instances created with the `cu` specifier (such as `en-US@cu=cad`), or with a custom [`Locale.Components`](locale/components.md), this property represents the custom currency. Otherwise, it represents the locale’s default currency.

## See Also

- [Locale.Currency](locale/currency-swift.struct.md)
  A type that represents the currency system used by a locale, like dollars or euros.
- [var measurementSystem: Locale.MeasurementSystem](locale/measurementsystem-swift.property.md)
  The measurement system used by the locale, like metric or the US system.
- [Locale.MeasurementSystem](locale/measurementsystem-swift.struct.md)
  A type that represents the measurement system used by a locale, like metric or the US system.
- [var numberingSystem: Locale.NumberingSystem](locale/numberingsystem-swift.property.md)
  The numbering system used by the locale.
- [var availableNumberingSystems: [Locale.NumberingSystem]](locale/availablenumberingsystems.md)
  An array containing all the valid numbering systems for the locale.
- [Locale.NumberingSystem](locale/numberingsystem-swift.struct.md)
  A type that represents the numbering system used in a locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/currency-swift.property)*