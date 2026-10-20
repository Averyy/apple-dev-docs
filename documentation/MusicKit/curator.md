# Curator

**Framework**: MusicKit  
**Kind**: struct  
**Role**: Structure

A music item that represents a curator.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 12.3+
- tvOS 15.4+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct Curator
```

## Topics

### Instance Properties
- [var artwork: Artwork?](./curator/artwork.md)
  The curator artwork.
- [var editorialNotes: EditorialNotes?](./curator/editorialnotes.md)
  The notes about the curator that appear in the Music catalog.
- [let id: MusicItemID](./curator/id.md)
  The unique identifier for the curator.
- [var kind: Curator.Kind](./curator/kind-swift.property.md)
  The kind of curator.
- [var name: String](./curator/name.md)
  The name of the curator.
- [var playlists: MusicItemCollection<Playlist>?](./curator/playlists.md)
  The curator’s associated playlists.
- [var url: URL?](./curator/url.md)
  The URL for the curator.
### Enumerations
- [Curator.Kind](./curator/kind-swift.enum.md)
  The available kinds of curators.
### Default Implementations
- [FilterableMusicItem Implementations](./curator/filterablemusicitem-implementations.md)

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
- [struct Genre](./genre.md)
  A music item that represents a genre.
- [struct MusicVideo](./musicvideo.md)
  A music item that represents a music video.
- [struct Playlist](./playlist.md)
  A music item that represents a playlist.
- [struct RadioShow](./radioshow.md)
  A music item that represents a radio show.
- [struct RecordLabel](./recordlabel.md)
  A music item that represents a record label.
- [struct Song](./song.md)
  A music item that represents a song.
- [struct Station](./station.md)
  A music item that represents a station.
- [enum Track](./track.md)
  A music item that represents a track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/curator)*