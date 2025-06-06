# MusicPersonalRecommendation.Item

**Framework**: MusicKit  
**Kind**: enum

An item that represents an album, a playlist, or a station for a personal recommendation.

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
enum Item
```

## Topics

### Operators
- [static func == (MusicPersonalRecommendation.Item, MusicPersonalRecommendation.Item) -> Bool](musicpersonalrecommendation/item/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [MusicPersonalRecommendation.Item.album(_:)](musicpersonalrecommendation/item/album(_:).md)
  An item that corresponds to an album.
- [MusicPersonalRecommendation.Item.playlist(_:)](musicpersonalrecommendation/item/playlist(_:).md)
  An item that corresponds to a playlist.
- [MusicPersonalRecommendation.Item.station(_:)](musicpersonalrecommendation/item/station(_:).md)
  An item that corresponds to a station.
### Instance Properties
- [var artwork: Artwork?](musicpersonalrecommendation/item/artwork.md)
  The artwork of this item.
- [var hashValue: Int](musicpersonalrecommendation/item/hashvalue.md)
  The hash value.
- [var id: MusicItemID](musicpersonalrecommendation/item/id-swift.property.md)
  The unique identifier of this item.
- [var subtitle: String?](musicpersonalrecommendation/item/subtitle.md)
  The subtitle of this item.
- [var title: String](musicpersonalrecommendation/item/title.md)
  The title of this item.
### Instance Methods
- [func hash(into: inout Hasher)](musicpersonalrecommendation/item/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [MusicPersonalRecommendation.Item.ID](musicpersonalrecommendation/item/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.
### Default Implementations
- [CustomDebugStringConvertible Implementations](musicpersonalrecommendation/item/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](musicpersonalrecommendation/item/customstringconvertible-implementations.md)
- [Decodable Implementations](musicpersonalrecommendation/item/decodable-implementations.md)
- [Encodable Implementations](musicpersonalrecommendation/item/encodable-implementations.md)
- [Equatable Implementations](musicpersonalrecommendation/item/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [MusicItem](musicitem.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicpersonalrecommendation/item)*