# Locale.Currency

**Framework**: Foundation  
**Kind**: struct

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
- [init(String)](locale/currency-swift.struct/init(_:).md)
  Creates a currency instance from a BCP 47 identifier.
### Examining currency properties
- [var identifier: String](locale/currency-swift.struct/identifier.md)
  The currency’s identifier.
- [var isISOCurrency: Bool](locale/currency-swift.struct/isisocurrency.md)
  A Boolean value that indicates whether the currency is in the list of ISO-defined currencies.
### Using common currencies
- [static var isoCurrencies: [Locale.Currency]](locale/currency-swift.struct/isocurrencies.md)
  An array containing currencies defined by the currency codes in ISO-4217.
- [static let unknown: Locale.Currency](locale/currency-swift.struct/unknown.md)
  A representation of an “unknown” currency, for use with transactions that don’t involve any currency.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/ExpressibleByExtendedGraphemeClusterLiteral.md)
- [ExpressibleByStringLiteral](../Swift/ExpressibleByStringLiteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/ExpressibleByUnicodeScalarLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var currency: Locale.Currency?](locale/currency-swift.property.md)
  The currency used by the locale.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/currency-swift.struct)*