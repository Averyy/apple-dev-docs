# MusicItemID

**Framework**: MusicKit  
**Kind**: struct

An object that represents a unique identifier for a music item.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@frozen
struct MusicItemID
```

## Topics

### Initializers
- [init(String)](musicitemid/init(_:).md)
  Creates a music item identifier with a string.
- [init(rawValue: String)](musicitemid/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
- [init(stringLiteral: String)](musicitemid/init(stringliteral:).md)
  Creates an instance initialized to the given string value.
### Instance Properties
- [let rawValue: String](musicitemid/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [MusicItemID.ExtendedGraphemeClusterLiteralType](musicitemid/extendedgraphemeclusterliteraltype.md)
  A type that represents an extended grapheme cluster literal.
- [MusicItemID.RawValue](musicitemid/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
- [MusicItemID.StringLiteralType](musicitemid/stringliteraltype.md)
  A type that represents a string literal.
- [MusicItemID.UnicodeScalarLiteralType](musicitemid/unicodescalarliteraltype.md)
  A type that represents a Unicode scalar literal.
### Default Implementations
- [CustomStringConvertible Implementations](musicitemid/customstringconvertible-implementations.md)
- [Decodable Implementations](musicitemid/decodable-implementations.md)
- [Encodable Implementations](musicitemid/encodable-implementations.md)
- [Equatable Implementations](musicitemid/equatable-implementations.md)
- [ExpressibleByExtendedGraphemeClusterLiteral Implementations](musicitemid/expressiblebyextendedgraphemeclusterliteral-implementations.md)
- [ExpressibleByStringLiteral Implementations](musicitemid/expressiblebystringliteral-implementations.md)
- [RawRepresentable Implementations](musicitemid/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/ExpressibleByExtendedGraphemeClusterLiteral.md)
- [ExpressibleByStringLiteral](../Swift/ExpressibleByStringLiteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/ExpressibleByUnicodeScalarLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [MusicLibraryRequestFilterValueEquatable](musiclibraryrequestfiltervalueequatable.md)
- [MusicLibraryRequestFilterValueMembershipComparable](musiclibraryrequestfiltervaluemembershipcomparable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol MusicItem](musicitem.md)
  A protocol with basic requirements for music items.
- [struct MusicItemCollection](musicitemcollection.md)
  A collection of music items.
- [protocol MusicPropertyContainer](musicpropertycontainer.md)
  A protocol for music items that allow loading additional properties that you can fetch asynchronously.
- [class MusicRelationshipProperty](musicrelationshipproperty.md)
  An identifier for a music item relationship property from a specific root type to a specific value type for the element of the resulting collection.
- [class MusicExtendedAttributeProperty](musicextendedattributeproperty.md)
  An identifier for a music item extended attribute property from a specific root type to a specific resulting value type.
- [class MusicAttributeProperty](musicattributeproperty.md)
  An identifier for a music item attribute property from a specific root type to a specific resulting value type.
- [class PartialMusicAsyncProperty](partialmusicasyncproperty.md)
  A partially type-erased identifier for a music item property that you can fetch asynchronously from a concrete root type to any resulting value type.
- [class PartialMusicProperty](partialmusicproperty.md)
  A partially type-erased identifier for a music item property from a concrete root type to any resulting value type.
- [class AnyMusicProperty](anymusicproperty.md)
  A type-erased identifier for a music item property, from any root type to any resulting value type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicitemid)*