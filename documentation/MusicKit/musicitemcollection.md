# MusicItemCollection

**Framework**: MusicKit  
**Kind**: struct

A collection of music items.

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
struct MusicItemCollection<MusicItemType> where MusicItemType : MusicItem
```

## Topics

### Operators
- [static func += (inout MusicItemCollection<MusicItemType>, MusicItemCollection<MusicItemType>)](musicitemcollection/+=(_:_:).md)
  Appends contents of a collection representing a next batch, in the right hand side, to the existing collection on the left hand side.
### Initializers
- [init<S>(S)](musicitemcollection/init(_:).md)
### Instance Properties
- [var hasNextBatch: Bool](musicitemcollection/hasnextbatch.md)
  A Boolean value that indicates whether the collection has information that allows it to fetch a subsequent batch of items.
- [var title: String?](musicitemcollection/title.md)
  An optional title for the collection.
### Instance Methods
- [func nextBatch(limit: Int?) async throws -> MusicItemCollection<MusicItemType>?](musicitemcollection/nextbatch(limit:)-432i0.md)
  Fetches the next batch of items asynchronously.
- [func nextBatch(limit: Int?) async throws -> MusicItemCollection<MusicItemType>?](musicitemcollection/nextbatch(limit:)-ywue.md)
  Fetches the next batch of items asynchronously.
### Default Implementations
- [BidirectionalCollection Implementations](musicitemcollection/bidirectionalcollection-implementations.md)
- [Collection Implementations](musicitemcollection/collection-implementations.md)
- [CustomDebugStringConvertible Implementations](musicitemcollection/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](musicitemcollection/customstringconvertible-implementations.md)
- [Decodable Implementations](musicitemcollection/decodable-implementations.md)
- [Encodable Implementations](musicitemcollection/encodable-implementations.md)
- [Equatable Implementations](musicitemcollection/equatable-implementations.md)
- [ExpressibleByArrayLiteral Implementations](musicitemcollection/expressiblebyarrayliteral-implementations.md)
- [Hashable Implementations](musicitemcollection/hashable-implementations.md)
- [RandomAccessCollection Implementations](musicitemcollection/randomaccesscollection-implementations.md)
- [Sequence Implementations](musicitemcollection/sequence-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [RandomAccessCollection](../Swift/RandomAccessCollection.md)
- [Sendable](../Swift/Sendable.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [protocol MusicItem](musicitem.md)
  A protocol with basic requirements for music items.
- [struct MusicItemID](musicitemid.md)
  An object that represents a unique identifier for a music item.
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

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicitemcollection)*