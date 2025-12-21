# MusicCatalogSearchResponse.TopResult

**Framework**: MusicKit  
**Kind**: enum

An item that represents one of the top results in a catalog search response.

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
enum TopResult
```

## Topics

### Enumeration Cases
- [MusicCatalogSearchResponse.TopResult.album(_:)](musiccatalogsearchresponse/topresult/album(_:).md)
  An item that corresponds to an album.
- [MusicCatalogSearchResponse.TopResult.artist(_:)](musiccatalogsearchresponse/topresult/artist(_:).md)
  An item that corresponds to an artist.
- [MusicCatalogSearchResponse.TopResult.curator(_:)](musiccatalogsearchresponse/topresult/curator(_:).md)
  An item that corresponds to a curator.
- [MusicCatalogSearchResponse.TopResult.musicVideo(_:)](musiccatalogsearchresponse/topresult/musicvideo(_:).md)
  An item that corresponds to a music video.
- [MusicCatalogSearchResponse.TopResult.playlist(_:)](musiccatalogsearchresponse/topresult/playlist(_:).md)
  An item that corresponds to a playlist.
- [MusicCatalogSearchResponse.TopResult.radioShow(_:)](musiccatalogsearchresponse/topresult/radioshow(_:).md)
  An item that corresponds to a radio show.
- [MusicCatalogSearchResponse.TopResult.recordLabel(_:)](musiccatalogsearchresponse/topresult/recordlabel(_:).md)
  An item that corresponds to a record label.
- [MusicCatalogSearchResponse.TopResult.song(_:)](musiccatalogsearchresponse/topresult/song(_:).md)
  An item that corresponds to a song.
- [MusicCatalogSearchResponse.TopResult.station(_:)](musiccatalogsearchresponse/topresult/station(_:).md)
  An item that corresponds to a station.
### Instance Properties
- [var artwork: Artwork?](musiccatalogsearchresponse/topresult/artwork.md)
  The artwork of this top result for catalog search.
- [var id: MusicItemID](musiccatalogsearchresponse/topresult/id.md)
  The unique identifier of this top result for catalog search.
- [var title: String](musiccatalogsearchresponse/topresult/title.md)
  The title of this top result for catalog search.

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

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musiccatalogsearchresponse/topresult)*