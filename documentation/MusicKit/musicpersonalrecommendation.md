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

### Instance Properties
- [var albums: MusicItemCollection<Album>](musicpersonalrecommendation/albums.md)
  The albums for the personal recommendation.
- [let id: MusicItemID](musicpersonalrecommendation/id.md)
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
### Enumerations
- [MusicPersonalRecommendation.Item](musicpersonalrecommendation/item.md)
  An item that represents an album, a playlist, or a station for a personal recommendation.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [Identifiable](../swift/identifiable.md)
- [MusicItem](musicitem.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicpersonalrecommendation)*