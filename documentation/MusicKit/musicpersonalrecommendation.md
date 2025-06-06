# MusicPersonalRecommendation

**Framework**: MusicKit  
**Kind**: struct

An object that contains recommended items based on the user’s library and listening history.

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
struct MusicPersonalRecommendation
```

## Topics

### Operators
- [static func == (MusicPersonalRecommendation, MusicPersonalRecommendation) -> Bool](musicpersonalrecommendation/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var albums: MusicItemCollection<Album>](musicpersonalrecommendation/albums.md)
  The albums for the personal recommendation.
- [var hashValue: Int](musicpersonalrecommendation/hashvalue.md)
  The hash value.
- [let id: MusicItemID](musicpersonalrecommendation/id-swift.property.md)
  The unique identifier for the personal recommendation.
- [var items: MusicItemCollection<MusicPersonalRecommendation.Item>](musicpersonalrecommendation/items.md)
  The items for the personal recommendation.
- [let nextRefreshDate: Date?](musicpersonalrecommendation/nextrefreshdate.md)
  The next date for refreshing the personal recommendation.
- [var playlists: MusicItemCollection<Playlist>](musicpersonalrecommendation/playlists.md)
  The playlists for the personal recommendation.
- [let reason: String?](musicpersonalrecommendation/reason.md)
  The reason for the personal recommendation.
- [var stations: MusicItemCollection<Station>](musicpersonalrecommendation/stations.md)
  The stations for the personal recommendation.
- [let title: String?](musicpersonalrecommendation/title.md)
  The title for the personal recommendation.
- [var types: [any MusicPersonalRecommendationItem.Type]](musicpersonalrecommendation/types.md)
  The types of items in the personal recommendation.
### Instance Methods
- [func hash(into: inout Hasher)](musicpersonalrecommendation/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [MusicPersonalRecommendation.ID](musicpersonalrecommendation/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.
### Enumerations
- [MusicPersonalRecommendation.Item](musicpersonalrecommendation/item.md)
  An item that represents an album, a playlist, or a station for a personal recommendation.
### Default Implementations
- [CustomDebugStringConvertible Implementations](musicpersonalrecommendation/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](musicpersonalrecommendation/customstringconvertible-implementations.md)
- [Decodable Implementations](musicpersonalrecommendation/decodable-implementations.md)
- [Encodable Implementations](musicpersonalrecommendation/encodable-implementations.md)
- [Equatable Implementations](musicpersonalrecommendation/equatable-implementations.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicpersonalrecommendation)*