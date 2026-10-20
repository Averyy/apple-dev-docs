# Locale.NumberingSystem

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

A type that represents the numbering system used in a locale.

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
struct NumberingSystem
```

## Topics

### Creating a numbering system instance
- [init(String)](./numberingsystem-swift.struct/init%28_%29.md)
  Creates a numbering system instance from a BCP 47 identifier.
- [init(stringLiteral: String)](./numberingsystem-swift.struct/init%28stringliteral%29.md)
  Creates a numbering system instance from a BCP 47 identifier as a string literal.
### Examining numbering system properties
- [var identifier: String](./numberingsystem-swift.struct/identifier.md)
  The numbering system’s BCP 47 identifier.
### Type Properties
- [static var availableNumberingSystems: [Locale.NumberingSystem]](./numberingsystem-swift.struct/availablenumberingsystems.md)
  A list of available numbering systems on the system.

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
- [Locale.Currency](./currency-swift.struct.md)
  A type that represents the currency system used by a locale, like dollars or euros.
- [var measurementSystem: Locale.MeasurementSystem](./measurementsystem-swift.property.md)
  The measurement system used by the locale, like metric or the US system.
- [Locale.MeasurementSystem](./measurementsystem-swift.struct.md)
  A type that represents the measurement system used by a locale, like metric or the US system.
- [var numberingSystem: Locale.NumberingSystem](./numberingsystem-swift.property.md)
  The numbering system used by the locale.
- [var availableNumberingSystems: [Locale.NumberingSystem]](./availablenumberingsystems.md)
  An array containing all the valid numbering systems for the locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/numberingsystem-swift.struct)*