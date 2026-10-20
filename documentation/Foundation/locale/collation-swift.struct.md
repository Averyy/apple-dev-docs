# Locale.Collation

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

A type that represents the string sort order used by the locale.

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
struct Collation
```

## Topics

### Creating a collation
- [init(String)](./collation-swift.struct/init%28_%29.md)
  Creates a collation from a BCP 47 identifier.
- [init(stringLiteral: String)](./collation-swift.struct/init%28stringliteral%29.md)
  Creates a collation from a BCP 47 identifier as a string literal.
### Examining collation properties
- [var identifier: String](./collation-swift.struct/identifier.md)
  The collation’s BCP 47 identifier.
### Using special-purpose collations
- [static let standard: Locale.Collation](./collation-swift.struct/standard.md)
  A collation that provides the default ordering for each language.
- [static let searchRules: Locale.Collation](./collation-swift.struct/searchrules.md)
  A collation used for string search.
### Type Properties
- [static var availableCollations: [Locale.Collation]](./collation-swift.struct/availablecollations.md)
  A list of available collations on the system.
### Type Methods
- [static func availableCollations(for: Locale.Language) -> [Locale.Collation]](./collation-swift.struct/availablecollations%28for%29.md)
  A list of available collations for the specified `language` in the order that it is most likely to make a difference.

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

### Getting ordering components
- [var collation: Locale.Collation](./collation-swift.property.md)
  The string sort order of the locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/collation-swift.struct)*