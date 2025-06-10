# Playlist

**Framework**: MusicKit  
**Kind**: struct

A music item that represents a playlist.

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
struct Playlist
```

## Topics

### Structures
- [Playlist.Entry](playlist/entry.md)
  A music item that represents a playlist entry.
### Operators
- [static func == (Playlist, Playlist) -> Bool](playlist/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var artwork: Artwork?](playlist/artwork.md)
  The artwork for the playlist.
- [var curator: Curator?](playlist/curator.md)
  The playlist’s associated curator.
- [var curatorName: String?](playlist/curatorname.md)
  The display name for the playlist’s curator.
- [var entries: MusicItemCollection<Playlist.Entry>?](playlist/entries.md)
  The entries in the playlist
- [var featuredArtists: MusicItemCollection<Artist>?](playlist/featuredartists.md)
  A collection of featured artists for this playlist.
- [var hashValue: Int](playlist/hashvalue.md)
  The hash value.
- [let id: MusicItemID](playlist/id-swift.property.md)
  The unique identifier for the playlist.
- [var isChart: Bool?](playlist/ischart.md)
  A Boolean value that indicates whether the playlist represents a popularity chart.
- [var kind: Playlist.Kind?](playlist/kind-swift.property.md)
  The kind of playlist.
- [var lastModifiedDate: Date?](playlist/lastmodifieddate.md)
  The playlist’s most recent modification date.
- [var lastPlayedDate: Date?](playlist/lastplayeddate.md)
  The date when the user last played the playlist on this device.
- [var libraryAddedDate: Date?](playlist/libraryaddeddate.md)
  The date when the user added the playlist to the library.
- [var moreByCurator: MusicItemCollection<Playlist>?](playlist/morebycurator.md)
  A collection of additional playlists by the same curator.
- [var name: String](playlist/name.md)
  The name of the playlist.
- [var playParameters: PlayParameters?](playlist/playparameters.md)
  The parameters to use to play the tracks in the playlist.
- [var radioShow: RadioShow?](playlist/radioshow.md)
  The playlist’s associated radio show.
- [var shortDescription: String?](playlist/shortdescription.md)
  An abbreviated description to show inline or when the playlist appears alongside other content.
- [var standardDescription: String?](playlist/standarddescription.md)
  A description to show when the playlist is prominently displayed.
- [var tracks: MusicItemCollection<Track>?](playlist/tracks.md)
  The tracks in the playlist.
- [var url: URL?](playlist/url.md)
  The URL for the playlist.
### Instance Methods
- [func hash(into: inout Hasher)](playlist/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [typealias ID](playlist/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.
### Enumerations
- [Playlist.Kind](playlist/kind-swift.enum.md)
  The available kinds of playlists.
### Default Implementations
- [CustomDebugStringConvertible Implementations](playlist/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](playlist/customstringconvertible-implementations.md)
- [Decodable Implementations](playlist/decodable-implementations.md)
- [Encodable Implementations](playlist/encodable-implementations.md)
- [Equatable Implementations](playlist/equatable-implementations.md)
- [FilterableMusicItem Implementations](playlist/filterablemusicitem-implementations.md)
- [MusicItem Implementations](playlist/musicitem-implementations.md)
- [MusicLibraryRequestable Implementations](playlist/musiclibraryrequestable-implementations.md)

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
- [MusicCatalogChartRequestable](musiccatalogchartrequestable.md)
- [MusicCatalogSearchable](musiccatalogsearchable.md)
- [MusicItem](musicitem.md)
- [MusicLibraryAddable](musiclibraryaddable.md)
- [MusicLibraryRequestable](musiclibraryrequestable.md)
- [MusicLibrarySearchable](musiclibrarysearchable.md)
- [MusicLibrarySectionRequestable](musiclibrarysectionrequestable.md)
- [MusicPersonalRecommendationItem](musicpersonalrecommendationitem.md)
- [MusicPlaylistAddable](musicplaylistaddable.md)
- [MusicPropertyContainer](musicpropertycontainer.md)
- [PlayableMusicItem](playablemusicitem.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/playlist)*