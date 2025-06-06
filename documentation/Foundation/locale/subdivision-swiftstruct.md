# Locale.Subdivision

**Framework**: Foundation  
**Kind**: struct

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
- [init(String)](locale/subdivision-swift.struct/init(_:).md)
  Creates a sudivision from a Unicode identifier.
- [static func subdivision(for: Locale.Region) -> Locale.Subdivision](locale/subdivision-swift.struct/subdivision(for:).md)
  Returns the subdivision representing the given region as a whole.
### Examining subdivision properties
- [var identifier: String](locale/subdivision-swift.struct/identifier.md)
  The subdivision’s Unicode identifier.

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

## See Also

- [var region: Locale.Region?](locale/region-swift.property.md)
  The region used by the locale.
- [Locale.Region](locale/region-swift.struct.md)
  A type that represents a geographic region, for use in specifying a locale or language.
- [var subdivision: Locale.Subdivision?](locale/subdivision-swift.property.md)
  The optional subdivision of the region used by this locale.
- [var variant: Locale.Variant?](locale/variant-swift.property.md)
  An optional variant used by the locale.
- [Locale.Variant](locale/variant-swift.struct.md)
  A type that represents a locale’s languate variant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/subdivision-swift.struct)*