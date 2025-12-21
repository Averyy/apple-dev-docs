# RecentlyPlayedMusicItem

**Framework**: MusicKit  
**Kind**: enum

An item that represents an album, a playlist, or a station that the user has recently played.

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
enum RecentlyPlayedMusicItem
```

## Topics

### Enumeration Cases
- [RecentlyPlayedMusicItem.album(_:)](recentlyplayedmusicitem/album(_:).md)
  An item that corresponds to an album.
- [RecentlyPlayedMusicItem.playlist(_:)](recentlyplayedmusicitem/playlist(_:).md)
  An item that corresponds to a playlist.
- [RecentlyPlayedMusicItem.station(_:)](recentlyplayedmusicitem/station(_:).md)
  An item that corresponds to a station.
### Instance Properties
- [var artwork: Artwork?](recentlyplayedmusicitem/artwork.md)
  The artwork of this item.
- [var id: MusicItemID](recentlyplayedmusicitem/id.md)
  The unique identifier of this item.
- [var playParameters: PlayParameters?](recentlyplayedmusicitem/playparameters.md)
  The parameters to use to play this item.
- [var subtitle: String?](recentlyplayedmusicitem/subtitle.md)
  The subtitle of this item.
- [var title: String](recentlyplayedmusicitem/title.md)
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
- [MusicRecentlyPlayedRequestable](musicrecentlyplayedrequestable.md)
- [PlayableMusicItem](playablemusicitem.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/recentlyplayedmusicitem)*