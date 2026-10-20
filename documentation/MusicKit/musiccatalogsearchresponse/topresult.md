# MusicCatalogSearchResponse.TopResult

**Framework**: MusicKit  
**Kind**: enum  
**Role**: Enumeration

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
- [MusicCatalogSearchResponse.TopResult.album(_:)](./topresult/album%28_%29.md)
  An item that corresponds to an album.
- [MusicCatalogSearchResponse.TopResult.artist(_:)](./topresult/artist%28_%29.md)
  An item that corresponds to an artist.
- [MusicCatalogSearchResponse.TopResult.curator(_:)](./topresult/curator%28_%29.md)
  An item that corresponds to a curator.
- [MusicCatalogSearchResponse.TopResult.musicVideo(_:)](./topresult/musicvideo%28_%29.md)
  An item that corresponds to a music video.
- [MusicCatalogSearchResponse.TopResult.playlist(_:)](./topresult/playlist%28_%29.md)
  An item that corresponds to a playlist.
- [MusicCatalogSearchResponse.TopResult.radioShow(_:)](./topresult/radioshow%28_%29.md)
  An item that corresponds to a radio show.
- [MusicCatalogSearchResponse.TopResult.recordLabel(_:)](./topresult/recordlabel%28_%29.md)
  An item that corresponds to a record label.
- [MusicCatalogSearchResponse.TopResult.song(_:)](./topresult/song%28_%29.md)
  An item that corresponds to a song.
- [MusicCatalogSearchResponse.TopResult.station(_:)](./topresult/station%28_%29.md)
  An item that corresponds to a station.
### Instance Properties
- [var artwork: Artwork?](./topresult/artwork.md)
  The artwork of this top result for catalog search.
- [var id: MusicItemID](./topresult/id.md)
  The unique identifier of this top result for catalog search.
- [var title: String](./topresult/title.md)
  The title of this top result for catalog search.

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

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musiccatalogsearchresponse/topresult)*