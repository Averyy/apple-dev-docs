# Locale.Subdivision

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

A type that represents a subdivision of a region, such as a state in the US or a province in Canada.

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
struct Subdivision
```

## Topics

### Creating a subdivision
- [init(String)](./subdivision-swift.struct/init%28_%29.md)
  Creates a sudivision from a Unicode identifier.
- [static func subdivision(for: Locale.Region) -> Locale.Subdivision](./subdivision-swift.struct/subdivision%28for%29.md)
  Returns the subdivision representing the given region as a whole.
- [init(stringLiteral: String)](./subdivision-swift.struct/init%28stringliteral%29.md)
  Creates a sudivision from a Unicode identifier as a string literal.
### Examining subdivision properties
- [var identifier: String](./subdivision-swift.struct/identifier.md)
  The subdivision’s Unicode identifier.

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

### Getting region components
- [var region: Locale.Region?](./region-swift.property.md)
  The region used by the locale.
- [Locale.Region](./region-swift.struct.md)
  A type that represents a geographic region, for use in specifying a locale or language.
- [var subdivision: Locale.Subdivision?](./subdivision-swift.property.md)
  The optional subdivision of the region used by this locale.
- [var variant: Locale.Variant?](./variant-swift.property.md)
  An optional variant used by the locale.
- [Locale.Variant](./variant-swift.struct.md)
  A type that represents a locale’s language variant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/subdivision-swift.struct)*