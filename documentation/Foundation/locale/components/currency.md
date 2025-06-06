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
var currency: Locale.Currency?
```

#### Discussion

Set this property to override the locale’s default currency. To request the default currency used by the locale, use the [`Locale`](locale.md) property [`currency`](locale/currency-swift.property.md).

This property corresponds to the `cu` key of the Unicode BCP 47 extension.

## See Also

- [Locale.Currency](locale/currency-swift.struct.md)
  A type that represents the currency system used by a locale, like dollars or euros.
- [var measurementSystem: Locale.MeasurementSystem?](locale/components/measurementsystem.md)
  The measurement system used by the locale, like metric or the US system.
- [Locale.MeasurementSystem](locale/measurementsystem-swift.struct.md)
  A type that represents the measurement system used by a locale, like metric or the US system.
- [var numberingSystem: Locale.NumberingSystem?](locale/components/numberingsystem.md)
  The numbering system used by the locale.
- [Locale.NumberingSystem](locale/numberingsystem-swift.struct.md)
  A type that represents the numbering system used in a locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/components/currency)*