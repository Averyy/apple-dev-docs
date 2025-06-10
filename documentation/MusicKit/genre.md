# Genre

**Framework**: MusicKit  
**Kind**: struct

A music item that represents a genre.

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
struct Genre
```

## Topics

### Operators
- [static func == (Genre, Genre) -> Bool](genre/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](genre/hashvalue.md)
  The hash value.
- [let id: MusicItemID](genre/id-swift.property.md)
  The unique identifier for the genre.
- [var libraryAddedDate: Date?](genre/libraryaddeddate.md)
  The date when the user added the genre to the library.
- [var name: String](genre/name.md)
  The localized name of the genre.
- [var parent: Genre?](genre/parent.md)
  The parent genre, if any.
### Instance Methods
- [func hash(into: inout Hasher)](genre/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [typealias ID](genre/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.
### Default Implementations
- [CustomDebugStringConvertible Implementations](genre/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](genre/customstringconvertible-implementations.md)
- [Decodable Implementations](genre/decodable-implementations.md)
- [Encodable Implementations](genre/encodable-implementations.md)
- [Equatable Implementations](genre/equatable-implementations.md)
- [FilterableMusicItem Implementations](genre/filterablemusicitem-implementations.md)
- [MusicItem Implementations](genre/musicitem-implementations.md)
- [MusicLibraryRequestable Implementations](genre/musiclibraryrequestable-implementations.md)

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
- [MusicCatalogTopLevelResourceRequesting](musiccatalogtoplevelresourcerequesting.md)
- [MusicItem](musicitem.md)
- [MusicLibraryRequestable](musiclibraryrequestable.md)
- [MusicLibrarySectionRequestable](musiclibrarysectionrequestable.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/genre)*