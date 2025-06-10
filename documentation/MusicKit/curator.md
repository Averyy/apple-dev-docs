# Curator

**Framework**: MusicKit  
**Kind**: struct

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

### Operators
- [static func == (Curator, Curator) -> Bool](curator/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var artwork: Artwork?](curator/artwork.md)
  The curator artwork.
- [var editorialNotes: EditorialNotes?](curator/editorialnotes.md)
  The notes about the curator that appear in the Music catalog.
- [var hashValue: Int](curator/hashvalue.md)
  The hash value.
- [let id: MusicItemID](curator/id-swift.property.md)
  The unique identifier for the curator.
- [var kind: Curator.Kind](curator/kind-swift.property.md)
  The kind of curator.
- [var name: String](curator/name.md)
  The name of the curator.
- [var playlists: MusicItemCollection<Playlist>?](curator/playlists.md)
  The curator’s associated playlists.
- [var url: URL?](curator/url.md)
  The URL for the curator.
### Instance Methods
- [func hash(into: inout Hasher)](curator/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [typealias ID](curator/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.
### Enumerations
- [Curator.Kind](curator/kind-swift.enum.md)
  The available kinds of curators.
### Default Implementations
- [CustomDebugStringConvertible Implementations](curator/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](curator/customstringconvertible-implementations.md)
- [Decodable Implementations](curator/decodable-implementations.md)
- [Encodable Implementations](curator/encodable-implementations.md)
- [Equatable Implementations](curator/equatable-implementations.md)
- [FilterableMusicItem Implementations](curator/filterablemusicitem-implementations.md)
- [MusicItem Implementations](curator/musicitem-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [FilterableMusicItem](filterablemusicitem.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [MusicCatalogSearchable](musiccatalogsearchable.md)
- [MusicItem](musicitem.md)
- [MusicPropertyContainer](musicpropertycontainer.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct Album](album.md)
  A music item that represents an album.
- [struct Artist](artist.md)
  A music item that represents an artist.
- [struct Genre](genre.md)
  A music item that represents a genre.
- [struct MusicVideo](musicvideo.md)
  A music item that represents a music video.
- [struct Playlist](playlist.md)
  A music item that represents a playlist.
- [struct RadioShow](radioshow.md)
  A music item that represents a radio show.
- [struct RecordLabel](recordlabel.md)
  A music item that represents a record label.
- [struct Song](song.md)
  A music item that represents a song.
- [struct Station](station.md)
  A music item that represents a station.
- [enum Track](track.md)
  A music item that represents a track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/curator)*