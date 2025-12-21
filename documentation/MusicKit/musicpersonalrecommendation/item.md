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
- [var id: MusicItemID](musicpersonalrecommendation/item/id.md)
  The unique identifier of this item.
- [var subtitle: String?](musicpersonalrecommendation/item/subtitle.md)
  The subtitle of this item.
- [var title: String](musicpersonalrecommendation/item/title.md)
  The title of this item.

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
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicpersonalrecommendation/item)*