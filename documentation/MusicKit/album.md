# Album

**Framework**: MusicKit  
**Kind**: struct

A music item that represents an album.

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
struct Album
```

## Topics

### Operators
- [static func == (Album, Album) -> Bool](album/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var appearsOn: MusicItemCollection<Playlist>?](album/appearson.md)
  A collection of playlists that include tracks from the album.
- [var artistName: String](album/artistname.md)
  The artist’s name.
- [var artistURL: URL?](album/artisturl.md)
  The artist’s URL.
- [var artists: MusicItemCollection<Artist>?](album/artists.md)
  The album’s associated artists.
- [var artwork: Artwork?](album/artwork.md)
  The album artwork.
- [var audioVariants: [AudioVariant]?](album/audiovariants.md)
  The variants that indicate the quality of audio available for the album.
- [var contentRating: ContentRating?](album/contentrating.md)
  The rating of the content.
- [var copyright: String?](album/copyright.md)
  The copyright text for the album.
- [var editorialNotes: EditorialNotes?](album/editorialnotes.md)
  The notes about the album that appear in the Music app.
- [var genreNames: [String]](album/genrenames.md)
  The names of the album’s associated genres.
- [var genres: MusicItemCollection<Genre>?](album/genres.md)
  The genres for the album.
- [var hashValue: Int](album/hashvalue.md)
  The hash value.
- [let id: MusicItemID](album/id-swift.property.md)
  The unique identifier for the album.
- [var isAppleDigitalMaster: Bool?](album/isappledigitalmaster.md)
  A Boolean value that indicates whether the album is an Apple Digital Master.
- [var isCompilation: Bool?](album/iscompilation.md)
  A Boolean value that indicates whether the album is a compilation.
- [var isComplete: Bool?](album/iscomplete.md)
  A Boolean value that indicates whether the album is complete.
- [var isSingle: Bool?](album/issingle.md)
  A Boolean value that indicates whether the album consists of a single song.
- [var lastPlayedDate: Date?](album/lastplayeddate.md)
  The date when the user last played the album on this device.
- [var libraryAddedDate: Date?](album/libraryaddeddate.md)
  The date when the user added the album to the library.
- [var otherVersions: MusicItemCollection<Album>?](album/otherversions.md)
  A collection of other versions of the album.
- [var playParameters: PlayParameters?](album/playparameters.md)
  The parameters to use to play the tracks of the album.
- [var recordLabelName: String?](album/recordlabelname.md)
  The name of the album’s record label.
- [var recordLabels: MusicItemCollection<RecordLabel>?](album/recordlabels.md)
  The record labels for the album.
- [var relatedAlbums: MusicItemCollection<Album>?](album/relatedalbums.md)
  A collection of related albums.
- [var relatedVideos: MusicItemCollection<MusicVideo>?](album/relatedvideos.md)
  A collection of the album’s music videos.
- [var releaseDate: Date?](album/releasedate.md)
  The release date (or expected prerelease date) for the album.
- [var title: String](album/title.md)
  The title of the album.
- [var trackCount: Int](album/trackcount.md)
  The number of tracks for the album.
- [var tracks: MusicItemCollection<Track>?](album/tracks.md)
  The tracks on the album.
- [var upc: String?](album/upc.md)
  The universal product code (UPC) for the album.
- [var url: URL?](album/url.md)
  The URL for the album.
### Instance Methods
- [func hash(into: inout Hasher)](album/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [typealias ID](album/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.
### Default Implementations
- [CustomDebugStringConvertible Implementations](album/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](album/customstringconvertible-implementations.md)
- [Decodable Implementations](album/decodable-implementations.md)
- [Encodable Implementations](album/encodable-implementations.md)
- [Equatable Implementations](album/equatable-implementations.md)
- [FilterableMusicItem Implementations](album/filterablemusicitem-implementations.md)
- [MusicItem Implementations](album/musicitem-implementations.md)
- [MusicLibraryRequestable Implementations](album/musiclibraryrequestable-implementations.md)

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
- [struct RecordLabel](recordlabel.md)
  A music item that represents a record label.
- [struct Song](song.md)
  A music item that represents a song.
- [struct Station](station.md)
  A music item that represents a station.
- [enum Track](track.md)
  A music item that represents a track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/album)*