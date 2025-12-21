# Artist

**Framework**: MusicKit  
**Kind**: struct

A music item that represents an artist.

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
struct Artist
```

## Topics

### Instance Properties
- [var albums: MusicItemCollection<Album>?](artist/albums.md)
  The artist’s associated albums.
- [var appearsOnAlbums: MusicItemCollection<Album>?](artist/appearsonalbums.md)
  A collection of albums from other artists that this artist appears on.
- [var artwork: Artwork?](artist/artwork.md)
  The artist artwork.
- [var compilationAlbums: MusicItemCollection<Album>?](artist/compilationalbums.md)
  A collection of compilation albums that include tracks by the artist.
- [var editorialNotes: EditorialNotes?](artist/editorialnotes.md)
  The notes about the artist that appear in the Music catalog.
- [var featuredAlbums: MusicItemCollection<Album>?](artist/featuredalbums.md)
  A collection of featured albums of the artist.
- [var featuredPlaylists: MusicItemCollection<Playlist>?](artist/featuredplaylists.md)
  A collection of the artist’s associated playlists.
- [var fullAlbums: MusicItemCollection<Album>?](artist/fullalbums.md)
  A collection of the artist’s full-release albums.
- [var genreNames: [String]?](artist/genrenames.md)
  The names of this artist’s associated genres.
- [var genres: MusicItemCollection<Genre>?](artist/genres.md)
  The artist’s associated genres.
- [let id: MusicItemID](artist/id.md)
  The unique identifier for the artist.
- [var latestRelease: Album?](artist/latestrelease.md)
  The artist’s most recent album.
- [var libraryAddedDate: Date?](artist/libraryaddeddate.md)
  The date when the user added the artist to the library.
- [var liveAlbums: MusicItemCollection<Album>?](artist/livealbums.md)
  A collection of the artist’s live albums.
- [var musicVideos: MusicItemCollection<MusicVideo>?](artist/musicvideos.md)
  The artist’s associated music videos.
- [var name: String](artist/name.md)
  The name of the artist.
- [var playlists: MusicItemCollection<Playlist>?](artist/playlists.md)
  The artist’s associated playlists.
- [var similarArtists: MusicItemCollection<Artist>?](artist/similarartists.md)
  A collection of artists similar to this artist.
- [var singles: MusicItemCollection<Album>?](artist/singles.md)
  A collection of the artist’s associated albums in the  category.
- [var station: Station?](artist/station.md)
  The artist’s associated station.
- [var topMusicVideos: MusicItemCollection<MusicVideo>?](artist/topmusicvideos.md)
  A collection of the artist’s top music videos.
- [var topSongs: MusicItemCollection<Song>?](artist/topsongs.md)
  A collection of the artist’s top songs.
- [var url: URL?](artist/url.md)
  The URL for the artist.
### Default Implementations
- [FilterableMusicItem Implementations](artist/filterablemusicitem-implementations.md)
- [MusicLibraryRequestable Implementations](artist/musiclibraryrequestable-implementations.md)

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
- [MusicLibraryRequestable](musiclibraryrequestable.md)
- [MusicLibrarySearchable](musiclibrarysearchable.md)
- [MusicLibrarySectionRequestable](musiclibrarysectionrequestable.md)
- [MusicPropertyContainer](musicpropertycontainer.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct Album](album.md)
  A music item that represents an album.
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

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/artist)*