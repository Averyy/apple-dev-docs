# Locale.MeasurementSystem

**Framework**: Foundation  
**Kind**: struct

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
- [init(String)](locale/measurementsystem-swift.struct/init(_:).md)
  Creates a measurement system instance from a BCP 47 identifier.
### Inspecting measurement system properties
- [var identifier: String](locale/measurementsystem-swift.struct/identifier.md)
  The measurement system’s BCP 47 identifier.
### Using common measurement systems
- [static var measurementSystems: [Locale.MeasurementSystem]](locale/measurementsystem-swift.struct/measurementsystems.md)
  An array of the measurement systems defined by the Unicode Common Locale Data Repository (CLDR).
- [static let metric: Locale.MeasurementSystem](locale/measurementsystem-swift.struct/metric.md)
  The metric measurement system.
- [static let uk: Locale.MeasurementSystem](locale/measurementsystem-swift.struct/uk.md)
  The United Kingdom measurement system.
- [static let us: Locale.MeasurementSystem](locale/measurementsystem-swift.struct/us.md)
  The United States measurement system.

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
- [Locale.Currency](locale/currency-swift.struct.md)
  A type that represents the currency system used by a locale, like dollars or euros.
- [var measurementSystem: Locale.MeasurementSystem](locale/measurementsystem-swift.property.md)
  The measurement system used by the locale, like metric or the US system.
- [var numberingSystem: Locale.NumberingSystem](locale/numberingsystem-swift.property.md)
  The numbering system used by the locale.
- [var availableNumberingSystems: [Locale.NumberingSystem]](locale/availablenumberingsystems.md)
  An array containing all the valid numbering systems for the locale.
- [Locale.NumberingSystem](locale/numberingsystem-swift.struct.md)
  A type that represents the numbering system used in a locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/measurementsystem-swift.struct)*