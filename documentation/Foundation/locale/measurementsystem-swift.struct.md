# Locale.MeasurementSystem

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

A type that represents the measurement system used by a locale, like metric or the US system.

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
struct MeasurementSystem
```

## Topics

### Creating a measurement system instance
- [init(String)](./measurementsystem-swift.struct/init%28_%29.md)
  Creates a measurement system instance from a BCP 47 identifier.
- [init(stringLiteral: String)](./measurementsystem-swift.struct/init%28stringliteral%29.md)
  Creates a measurement system instance from a BCP 47 identifier as a string literal.
### Inspecting measurement system properties
- [var identifier: String](./measurementsystem-swift.struct/identifier.md)
  The measurement system’s BCP 47 identifier.
### Using common measurement systems
- [static var measurementSystems: [Locale.MeasurementSystem]](./measurementsystem-swift.struct/measurementsystems.md)
  An array of the measurement systems defined by the Unicode Common Locale Data Repository (CLDR).
- [static let metric: Locale.MeasurementSystem](./measurementsystem-swift.struct/metric.md)
  The metric measurement system.
- [static let uk: Locale.MeasurementSystem](./measurementsystem-swift.struct/uk.md)
  The United Kingdom measurement system.
- [static let us: Locale.MeasurementSystem](./measurementsystem-swift.struct/us.md)
  The United States measurement system.

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
- [var numberingSystem: Locale.NumberingSystem](./numberingsystem-swift.property.md)
  The numbering system used by the locale.
- [var availableNumberingSystems: [Locale.NumberingSystem]](./availablenumberingsystems.md)
  An array containing all the valid numbering systems for the locale.
- [Locale.NumberingSystem](./numberingsystem-swift.struct.md)
  A type that represents the numbering system used in a locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/measurementsystem-swift.struct)*