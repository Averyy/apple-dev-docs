# Song

**Framework**: MusicKit  
**Kind**: struct

A music item that represents a song.

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
struct Song
```

## Topics

### Operators
- [static func == (Song, Song) -> Bool](song/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var albumTitle: String?](song/albumtitle.md)
  The title of the album the song appears on.
- [var albums: MusicItemCollection<Album>?](song/albums.md)
  The song’s associated albums.
- [var artistName: String](song/artistname.md)
  The artist’s name.
- [var artistURL: URL?](song/artisturl.md)
  The artist’s URL.
- [var artists: MusicItemCollection<Artist>?](song/artists.md)
  The song’s associated artists.
- [var artwork: Artwork?](song/artwork.md)
  The artwork for the song.
- [var attribution: String?](song/attribution.md)
  For classical music only, the name of the artist or composer to attribute to the song.
- [var audioVariants: [AudioVariant]?](song/audiovariants.md)
  The variants that indicate the quality of audio available for the song.
- [var composerName: String?](song/composername.md)
  The name of the song’s composer.
- [var composers: MusicItemCollection<Artist>?](song/composers.md)
  The song’s composers.
- [var contentRating: ContentRating?](song/contentrating.md)
  The rating of the content.
- [var discNumber: Int?](song/discnumber.md)
  The number of the disc the song appears on.
- [var duration: TimeInterval?](song/duration.md)
  The duration of the song.
- [var editorialNotes: EditorialNotes?](song/editorialnotes.md)
  The editorial notes for the song.
- [var genreNames: [String]](song/genrenames.md)
  The names of the song’s associated genres.
- [var genres: MusicItemCollection<Genre>?](song/genres.md)
  The song’s associated genres.
- [var hasLyrics: Bool](song/haslyrics.md)
  A Boolean value that indicates whether the song has lyrics available in the catalog. If true, the song has lyrics available; otherwise, it doesn’t.
- [var hashValue: Int](song/hashvalue.md)
  The hash value.
- [let id: MusicItemID](song/id-swift.property.md)
  The unique identifier for the song.
- [var isAppleDigitalMaster: Bool?](song/isappledigitalmaster.md)
  A Boolean value that indicates whether the song is an Apple Digital Master.
- [var isrc: String?](song/isrc.md)
  The International Standard Recording Code (ISRC) for the song.
- [var lastPlayedDate: Date?](song/lastplayeddate.md)
  The date when the user last played the song on this device.
- [var libraryAddedDate: Date?](song/libraryaddeddate.md)
  The date when the user added the song to the library.
- [var movementCount: Int?](song/movementcount.md)
  For classical music only, the movement count of this song.
- [var movementName: String?](song/movementname.md)
  For classical music only, the movement name of this song.
- [var movementNumber: Int?](song/movementnumber.md)
  For classical music only, the movement number of this song.
- [var musicVideos: MusicItemCollection<MusicVideo>?](song/musicvideos.md)
  The song’s associated music videos.
- [var playCount: Int?](song/playcount.md)
  The number of times the user played the song.
- [var playParameters: PlayParameters?](song/playparameters.md)
  The parameters to use to play the song.
- [var previewAssets: [PreviewAsset]?](song/previewassets.md)
  The preview assets for the song.
- [var releaseDate: Date?](song/releasedate.md)
  The release date (or expected prerelease date) for the song.
- [var station: Station?](song/station.md)
  The song’s associated station.
- [var title: String](song/title.md)
  The title of the song.
- [var trackNumber: Int?](song/tracknumber.md)
  The song’s number in the album’s track list.
- [var url: URL?](song/url.md)
  The URL for the song.
- [var workName: String?](song/workname.md)
  For classical music only, the name of the associated work.
### Instance Methods
- [func hash(into: inout Hasher)](song/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [typealias ID](song/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.
### Default Implementations
- [CustomDebugStringConvertible Implementations](song/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](song/customstringconvertible-implementations.md)
- [Decodable Implementations](song/decodable-implementations.md)
- [Encodable Implementations](song/encodable-implementations.md)
- [Equatable Implementations](song/equatable-implementations.md)
- [FilterableMusicItem Implementations](song/filterablemusicitem-implementations.md)
- [MusicItem Implementations](song/musicitem-implementations.md)
- [MusicLibraryRequestable Implementations](song/musiclibraryrequestable-implementations.md)

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
- [MusicPlaylistAddable](musicplaylistaddable.md)
- [MusicPropertyContainer](musicpropertycontainer.md)
- [MusicRecentlyPlayedRequestable](musicrecentlyplayedrequestable.md)
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
- [struct Playlist](playlist.md)
  A music item that represents a playlist.
- [struct RadioShow](radioshow.md)
  A music item that represents a radio show.
- [struct RecordLabel](recordlabel.md)
  A music item that represents a record label.
- [struct Station](station.md)
  A music item that represents a station.
- [enum Track](track.md)
  A music item that represents a track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/song)*