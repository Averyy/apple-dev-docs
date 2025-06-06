# MusicVideo

**Framework**: MusicKit  
**Kind**: struct

A music item that represents a music video.

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
struct MusicVideo
```

## Topics

### Operators
- [static func == (MusicVideo, MusicVideo) -> Bool](musicvideo/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var albumTitle: String?](musicvideo/albumtitle.md)
  The title of the album the music video appears on.
- [var albums: MusicItemCollection<Album>?](musicvideo/albums.md)
  The music video’s associated albums.
- [var artistName: String](musicvideo/artistname.md)
  The artist’s name.
- [var artistURL: URL?](musicvideo/artisturl.md)
  The artist’s URL.
- [var artists: MusicItemCollection<Artist>?](musicvideo/artists.md)
  The music video’s associated artists.
- [var artwork: Artwork?](musicvideo/artwork.md)
  The artwork for the music video.
- [var contentRating: ContentRating?](musicvideo/contentrating.md)
  The rating of the content.
- [var duration: TimeInterval?](musicvideo/duration.md)
  The duration of the music video.
- [var editorialNotes: EditorialNotes?](musicvideo/editorialnotes.md)
  The editorial notes for the music video.
- [var genreNames: [String]](musicvideo/genrenames.md)
  The names of the music video’s associated genres.
- [var genres: MusicItemCollection<Genre>?](musicvideo/genres.md)
  The music video’s associated genres.
- [var has4K: Bool?](musicvideo/has4k.md)
  A Boolean value that indicates whether the music video has 4K content.
- [var hasHDR: Bool?](musicvideo/hashdr.md)
  A Boolean value that indicates whether the music video has HDR10-encoded content.
- [var hashValue: Int](musicvideo/hashvalue.md)
  The hash value.
- [let id: MusicItemID](musicvideo/id-swift.property.md)
  The unique identifier for the music video.
- [var isPreview: Bool](musicvideo/ispreview.md)
  A Boolean value that indicates whether this content corresponds to a subscription video preview.
- [var isrc: String?](musicvideo/isrc.md)
  The International Standard Recording Code (ISRC) for the music video.
- [var lastPlayedDate: Date?](musicvideo/lastplayeddate.md)
  The date when the user last played the music video on this device.
- [var libraryAddedDate: Date?](musicvideo/libraryaddeddate.md)
  The date when the user added the music video to the library.
- [var moreByArtist: MusicItemCollection<MusicVideo>?](musicvideo/morebyartist.md)
  A collection of additional music videos by the artist.
- [var moreInGenre: MusicItemCollection<MusicVideo>?](musicvideo/moreingenre.md)
  A collection of music videos in the same genre as this music video.
- [var playCount: Int?](musicvideo/playcount.md)
  The number of times the user played the music video.
- [var playParameters: PlayParameters?](musicvideo/playparameters.md)
  The parameters to use to play the music video.
- [var previewAssets: [PreviewAsset]?](musicvideo/previewassets.md)
  The preview assets for the music video.
- [var releaseDate: Date?](musicvideo/releasedate.md)
  The release date (or expected prerelease date) for the music video.
- [var songs: MusicItemCollection<Song>?](musicvideo/songs.md)
  The music video’s associated songs.
- [var title: String](musicvideo/title.md)
  The title of the music video.
- [var trackNumber: Int?](musicvideo/tracknumber.md)
  The music video’s number in the album’s track list.
- [var url: URL?](musicvideo/url.md)
  The URL for the music video.
- [var workName: String?](musicvideo/workname.md)
  For classical music only, the name of the associated work.
### Instance Methods
- [func hash(into: inout Hasher)](musicvideo/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [MusicVideo.ID](musicvideo/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.
### Default Implementations
- [CustomDebugStringConvertible Implementations](musicvideo/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](musicvideo/customstringconvertible-implementations.md)
- [Decodable Implementations](musicvideo/decodable-implementations.md)
- [Encodable Implementations](musicvideo/encodable-implementations.md)
- [Equatable Implementations](musicvideo/equatable-implementations.md)
- [FilterableMusicItem Implementations](musicvideo/filterablemusicitem-implementations.md)
- [MusicItem Implementations](musicvideo/musicitem-implementations.md)
- [MusicLibraryRequestable Implementations](musicvideo/musiclibraryrequestable-implementations.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicvideo)*