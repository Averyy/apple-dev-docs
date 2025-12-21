# MusicLibrarySearchResponse.TopResult

**Framework**: MusicKit  
**Kind**: enum

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
- [MusicLibrarySearchResponse.TopResult.album(_:)](musiclibrarysearchresponse/topresult/album(_:).md)
  An item that corresponds to an album.
- [MusicLibrarySearchResponse.TopResult.artist(_:)](musiclibrarysearchresponse/topresult/artist(_:).md)
  An item that corresponds to an artist.
- [MusicLibrarySearchResponse.TopResult.musicVideo(_:)](musiclibrarysearchresponse/topresult/musicvideo(_:).md)
  An item that corresponds to a music video.
- [MusicLibrarySearchResponse.TopResult.playlist(_:)](musiclibrarysearchresponse/topresult/playlist(_:).md)
  An item that corresponds to a playlist.
- [MusicLibrarySearchResponse.TopResult.song(_:)](musiclibrarysearchresponse/topresult/song(_:).md)
  An item that corresponds to a song.
### Instance Properties
- [var artwork: Artwork?](musiclibrarysearchresponse/topresult/artwork.md)
  The artwork of this top result for library search.
- [var id: MusicItemID](musiclibrarysearchresponse/topresult/id.md)
  The unique identifier of this item.
- [var title: String](musiclibrarysearchresponse/topresult/title.md)
  The title of this top result for library search.

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

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musiclibrarysearchresponse/topresult)*