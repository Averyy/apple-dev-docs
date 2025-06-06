# RecordLabel

**Framework**: MusicKit  
**Kind**: struct

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

### Operators
- [static func == (RecordLabel, RecordLabel) -> Bool](recordlabel/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var artwork: Artwork?](recordlabel/artwork.md)
  The record label’s artwork.
- [var hashValue: Int](recordlabel/hashvalue.md)
  The hash value.
- [let id: MusicItemID](recordlabel/id-swift.property.md)
  The unique identifier for the record label.
- [var latestReleases: MusicItemCollection<Album>?](recordlabel/latestreleases.md)
  A collection of the most recent releases for the record label.
- [var name: String](recordlabel/name.md)
  The name of the record label.
- [var shortDescription: String?](recordlabel/shortdescription.md)
  An abbreviated description to show inline or when the record label appears alongside other content.
- [var standardDescription: String?](recordlabel/standarddescription.md)
  A description to show when the record label is prominently displayed.
- [var topReleases: MusicItemCollection<Album>?](recordlabel/topreleases.md)
  A collection of top releases for the record label.
- [var url: URL?](recordlabel/url.md)
  The URL for the record label.
### Instance Methods
- [func hash(into: inout Hasher)](recordlabel/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [RecordLabel.ID](recordlabel/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.
### Default Implementations
- [CustomDebugStringConvertible Implementations](recordlabel/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](recordlabel/customstringconvertible-implementations.md)
- [Decodable Implementations](recordlabel/decodable-implementations.md)
- [Encodable Implementations](recordlabel/encodable-implementations.md)
- [Equatable Implementations](recordlabel/equatable-implementations.md)
- [FilterableMusicItem Implementations](recordlabel/filterablemusicitem-implementations.md)
- [MusicItem Implementations](recordlabel/musicitem-implementations.md)

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
- [struct RadioShow](radioshow.md)
  A music item that represents a radio show.
- [struct Song](song.md)
  A music item that represents a song.
- [struct Station](station.md)
  A music item that represents a station.
- [enum Track](track.md)
  A music item that represents a track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/recordlabel)*