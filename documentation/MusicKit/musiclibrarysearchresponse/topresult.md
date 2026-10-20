# MusicLibrarySearchResponse.TopResult

**Framework**: MusicKit  
**Kind**: enum  
**Role**: Enumeration

An item that represents one of the top results in a library search response.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
enum TopResult
```

## Topics

### Enumeration Cases
- [MusicLibrarySearchResponse.TopResult.album(_:)](./topresult/album%28_%29.md)
  An item that corresponds to an album.
- [MusicLibrarySearchResponse.TopResult.artist(_:)](./topresult/artist%28_%29.md)
  An item that corresponds to an artist.
- [MusicLibrarySearchResponse.TopResult.musicVideo(_:)](./topresult/musicvideo%28_%29.md)
  An item that corresponds to a music video.
- [MusicLibrarySearchResponse.TopResult.playlist(_:)](./topresult/playlist%28_%29.md)
  An item that corresponds to a playlist.
- [MusicLibrarySearchResponse.TopResult.song(_:)](./topresult/song%28_%29.md)
  An item that corresponds to a song.
### Instance Properties
- [var artwork: Artwork?](./topresult/artwork.md)
  The artwork of this top result for library search.
- [var id: MusicItemID](./topresult/id.md)
  The unique identifier of this item.
- [var title: String](./topresult/title.md)
  The title of this top result for library search.

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

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musiclibrarysearchresponse/topresult)*