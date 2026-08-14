# Locale.Collation

**Framework**: Foundation  
**Kind**: struct

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
- [init(String)](locale/collation-swift.struct/init(_:).md)
  Creates a collation from a BCP 47 identifier.
- [init(stringLiteral: String)](locale/collation-swift.struct/init(stringliteral:).md)
  Creates a collation from a BCP 47 identifier as a string literal.
### Examining collation properties
- [var identifier: String](locale/collation-swift.struct/identifier.md)
  The collation’s BCP 47 identifier.
### Using special-purpose collations
- [static let standard: Locale.Collation](locale/collation-swift.struct/standard.md)
  A collation that provides the default ordering for each language.
- [static let searchRules: Locale.Collation](locale/collation-swift.struct/searchrules.md)
  A collation used for string search.
### Type Properties
- [static var availableCollations: [Locale.Collation]](locale/collation-swift.struct/availablecollations.md)
  A list of available collations on the system.
### Type Methods
- [static func availableCollations(for: Locale.Language) -> [Locale.Collation]](locale/collation-swift.struct/availablecollations(for:).md)
  A list of available collations for the specified `language` in the order that it is most likely to make a difference.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../swift/expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByStringLiteral](../swift/expressiblebystringliteral.md)
- [ExpressibleByUnicodeScalarLiteral](../swift/expressiblebyunicodescalarliteral.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var collation: Locale.Collation](locale/collation-swift.property.md)
  The string sort order of the locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/collation-swift.struct)*