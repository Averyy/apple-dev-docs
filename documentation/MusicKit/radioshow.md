# RadioShow

**Framework**: MusicKit  
**Kind**: struct

A music item that represents a radio show.

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
struct RadioShow
```

## Topics

### Operators
- [static func == (RadioShow, RadioShow) -> Bool](radioshow/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var artwork: Artwork?](radioshow/artwork.md)
  The radio show artwork.
- [var editorialNotes: EditorialNotes?](radioshow/editorialnotes.md)
  The notes about the radio show that appear in the Music catalog.
- [var hashValue: Int](radioshow/hashvalue.md)
  The hash value.
- [var hostName: String?](radioshow/hostname.md)
  The name of the host for the radio show.
- [let id: MusicItemID](radioshow/id-swift.property.md)
  The unique identifier for the radio show.
- [var name: String](radioshow/name.md)
  The name of the radio show.
- [var playlists: MusicItemCollection<Playlist>?](radioshow/playlists.md)
  The radio show’s associated playlists.
- [var url: URL?](radioshow/url.md)
  The URL for the radio show.
### Instance Methods
- [func hash(into: inout Hasher)](radioshow/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [RadioShow.ID](radioshow/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.
### Default Implementations
- [CustomDebugStringConvertible Implementations](radioshow/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](radioshow/customstringconvertible-implementations.md)
- [Decodable Implementations](radioshow/decodable-implementations.md)
- [Encodable Implementations](radioshow/encodable-implementations.md)
- [Equatable Implementations](radioshow/equatable-implementations.md)
- [FilterableMusicItem Implementations](radioshow/filterablemusicitem-implementations.md)
- [MusicItem Implementations](radioshow/musicitem-implementations.md)

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
- [struct Curator](curator.md)
  A music item that represents a curator.
- [struct Genre](genre.md)
  A music item that represents a genre.
- [struct MusicVideo](musicvideo.md)
  A music item that represents a music video.
- [struct Playlist](playlist.md)
  A music item that represents a playlist.
- [struct RecordLabel](recordlabel.md)
  A music item that represents a record label.
- [struct Song](song.md)
  A music item that represents a song.
- [struct Station](station.md)
  A music item that represents a station.
- [enum Track](track.md)
  A music item that represents a track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/radioshow)*