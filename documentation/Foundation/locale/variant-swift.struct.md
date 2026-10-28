# Locale.Variant

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

A type that represents a locale’s language variant.

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
struct Variant
```

## Overview

This type corresponds to the Unicode variant subtag, such as `posix`.

## Topics

### Creating a variant
- [init(String)](./variant-swift.struct/init%28_%29.md)
  Creates a variant from a BCP 47 identifier.
- [init(stringLiteral: String)](./variant-swift.struct/init%28stringliteral%29.md)
  Creates a variant from a BCP 47 identifier as a string literal.
### Examining variant properties
- [var identifier: String](./variant-swift.struct/identifier.md)
  The variant’s BCP 47 identifier.
### Using defined variants
- [static let posix: Locale.Variant](./variant-swift.struct/posix.md)

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
- [Locale.Subdivision](./subdivision-swift.struct.md)
  A type that represents a subdivision of a region, such as a state in the US or a province in Canada.
- [var variant: Locale.Variant?](./variant-swift.property.md)
  An optional variant used by the locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/variant-swift.struct)*