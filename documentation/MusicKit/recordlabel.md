# RecordLabel

**Framework**: MusicKit  
**Kind**: struct  
**Role**: Structure

A music item that represents a record label.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct RecordLabel
```

## Topics

### Instance Properties
- [var artwork: Artwork?](./recordlabel/artwork.md)
  The record label’s artwork.
- [let id: MusicItemID](./recordlabel/id.md)
  The unique identifier for the record label.
- [var latestReleases: MusicItemCollection<Album>?](./recordlabel/latestreleases.md)
  A collection of the most recent releases for the record label.
- [var name: String](./recordlabel/name.md)
  The name of the record label.
- [var shortDescription: String?](./recordlabel/shortdescription.md)
  An abbreviated description to show inline or when the record label appears alongside other content.
- [var standardDescription: String?](./recordlabel/standarddescription.md)
  A description to show when the record label is prominently displayed.
- [var topReleases: MusicItemCollection<Album>?](./recordlabel/topreleases.md)
  A collection of top releases for the record label.
- [var url: URL?](./recordlabel/url.md)
  The URL for the record label.
### Default Implementations
- [FilterableMusicItem Implementations](./recordlabel/filterablemusicitem-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [FilterableMusicItem](./filterablemusicitem.md)
- [Hashable](../Swift/hashable.md)
- [Identifiable](../Swift/identifiable.md)
- [MusicCatalogSearchable](./musiccatalogsearchable.md)
- [MusicItem](./musicitem.md)
- [MusicPropertyContainer](./musicpropertycontainer.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Music Items
- [struct Album](./album.md)
  A music item that represents an album.
- [struct Artist](./artist.md)
  A music item that represents an artist.
- [struct Curator](./curator.md)
  A music item that represents a curator.
- [struct Genre](./genre.md)
  A music item that represents a genre.
- [struct MusicVideo](./musicvideo.md)
  A music item that represents a music video.
- [struct Playlist](./playlist.md)
  A music item that represents a playlist.
- [struct RadioShow](./radioshow.md)
  A music item that represents a radio show.
- [struct Song](./song.md)
  A music item that represents a song.
- [struct Station](./station.md)
  A music item that represents a station.
- [enum Track](./track.md)
  A music item that represents a track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/recordlabel)*