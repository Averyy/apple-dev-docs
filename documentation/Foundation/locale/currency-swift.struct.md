# Locale.Currency

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

A type that represents the currency system used by a locale, like dollars or euros.

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
struct Currency
```

## Topics

### Creating a currency instance
- [init(String)](./currency-swift.struct/init%28_%29.md)
  Creates a currency instance from a BCP 47 identifier.
- [init(stringLiteral: String)](./currency-swift.struct/init%28stringliteral%29.md)
  Creates a currency instance from a BCP 47 identifier as a string literal.
### Examining currency properties
- [var identifier: String](./currency-swift.struct/identifier.md)
  The currency’s identifier.
- [var isISOCurrency: Bool](./currency-swift.struct/isisocurrency.md)
  A Boolean value that indicates whether the currency is in the list of ISO-defined currencies.
### Using common currencies
- [static var isoCurrencies: [Locale.Currency]](./currency-swift.struct/isocurrencies.md)
  An array containing currencies defined by the currency codes in ISO-4217.
- [static let unknown: Locale.Currency](./currency-swift.struct/unknown.md)
  A representation of an “unknown” currency, for use with transactions that don’t involve any currency.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../../Swift/expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByStringLiteral](../../Swift/expressiblebystringliteral.md)
- [ExpressibleByUnicodeScalarLiteral](../../Swift/expressiblebyunicodescalarliteral.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting measurement and counting components
- [var currency: Locale.Currency?](./currency-swift.property.md)
  The currency used by the locale.
- [var measurementSystem: Locale.MeasurementSystem](./measurementsystem-swift.property.md)
  The measurement system used by the locale, like metric or the US system.
- [Locale.MeasurementSystem](./measurementsystem-swift.struct.md)
  A type that represents the measurement system used by a locale, like metric or the US system.
- [var numberingSystem: Locale.NumberingSystem](./numberingsystem-swift.property.md)
  The numbering system used by the locale.
- [var availableNumberingSystems: [Locale.NumberingSystem]](./availablenumberingsystems.md)
  An array containing all the valid numbering systems for the locale.
- [Locale.NumberingSystem](./numberingsystem-swift.struct.md)
  A type that represents the numbering system used in a locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/currency-swift.struct)*