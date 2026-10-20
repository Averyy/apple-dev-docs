# MusicPersonalRecommendation.Item

**Framework**: MusicKit  
**Kind**: enum  
**Role**: Enumeration

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
- [MusicPersonalRecommendation.Item.album(_:)](./item/album%28_%29.md)
  An item that corresponds to an album.
- [MusicPersonalRecommendation.Item.playlist(_:)](./item/playlist%28_%29.md)
  An item that corresponds to a playlist.
- [MusicPersonalRecommendation.Item.station(_:)](./item/station%28_%29.md)
  An item that corresponds to a station.
### Instance Properties
- [var artwork: Artwork?](./item/artwork.md)
  The artwork of this item.
- [var id: MusicItemID](./item/id.md)
  The unique identifier of this item.
- [var subtitle: String?](./item/subtitle.md)
  The subtitle of this item.
- [var title: String](./item/title.md)
  The title of this item.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [Identifiable](../../Swift/identifiable.md)
- [MusicItem](../musicitem.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicpersonalrecommendation/item)*