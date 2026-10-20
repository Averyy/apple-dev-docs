# Track

**Framework**: MusicKit  
**Kind**: enum  
**Role**: Enumeration

A music item that represents a track.

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
enum Track
```

## Topics

### Enumeration Cases
- [case musicVideo(MusicVideo)](./track/musicvideo%28_%29.md)
  A track that corresponds to a music video.
- [case song(Song)](./track/song%28_%29.md)
  A track that corresponds to a song.
### Instance Properties
- [var albumTitle: String?](./track/albumtitle.md)
  The title of the album the track appears on.
- [var albums: MusicItemCollection<Album>?](./track/albums.md)
  The track’s associated albums.
- [var artistName: String](./track/artistname.md)
  The artist’s name.
- [var artistURL: URL?](./track/artisturl.md)
  The artist’s URL.
- [var artists: MusicItemCollection<Artist>?](./track/artists.md)
  The track’s associated artists.
- [var artwork: Artwork?](./track/artwork.md)
  The artwork for the track.
- [var contentRating: ContentRating?](./track/contentrating.md)
  The rating of the content.
- [var discNumber: Int?](./track/discnumber.md)
  The disc number of the track.
- [var duration: TimeInterval?](./track/duration.md)
  The duration of the track.
- [var editorialNotes: EditorialNotes?](./track/editorialnotes.md)
  The editorial notes for the track.
- [var endTime: TimeInterval?](./track/endtime.md)
  The custom end time of the track.
- [var genreNames: [String]](./track/genrenames.md)
  The names of the track’s associated genres.
- [var genres: MusicItemCollection<Genre>?](./track/genres.md)
  The track’s associated genres.
- [var id: MusicItemID](./track/id.md)
  The unique identifier for the track.
- [var isrc: String?](./track/isrc.md)
  The International Standard Recording Code (ISRC) for the track.
- [var lastPlayedDate: Date?](./track/lastplayeddate.md)
  The date when the user last played the track on this device.
- [var libraryAddedDate: Date?](./track/libraryaddeddate.md)
  The date when the user added the track to the library.
- [var playCount: Int?](./track/playcount.md)
  The number of times the user played the track.
- [var playParameters: PlayParameters?](./track/playparameters.md)
  The parameters to use to play the track.
- [var previewAssets: [PreviewAsset]?](./track/previewassets.md)
  The preview assets for the track.
- [var releaseDate: Date?](./track/releasedate.md)
  The release date (or expected for pre-release) of the track.
- [var startTime: TimeInterval?](./track/starttime.md)
  The custom start time of the track.
- [var title: String](./track/title.md)
  The title of the track.
- [var trackNumber: Int?](./track/tracknumber.md)
  The track’s number in the album’s track list.
- [var url: URL?](./track/url.md)
  The URL for the track.
- [var workName: String?](./track/workname.md)
  For classical music only, the name of the associated work.
### Default Implementations
- [MusicLibraryRequestable Implementations](./track/musiclibraryrequestable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [Identifiable](../Swift/identifiable.md)
- [MusicItem](./musicitem.md)
- [MusicLibraryAddable](./musiclibraryaddable.md)
- [MusicLibraryRequestable](./musiclibraryrequestable.md)
- [MusicPlaylistAddable](./musicplaylistaddable.md)
- [MusicPropertyContainer](./musicpropertycontainer.md)
- [MusicRecentlyPlayedRequestable](./musicrecentlyplayedrequestable.md)
- [PickableMusicItem](./pickablemusicitem.md)
- [PlayableMusicItem](./playablemusicitem.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Music Items
- [struct Album](./album.md)
  A music item that represents an album.
- [struct Artist](./artist.md)
  A music item that represents an artist.
- [struct Curator](./curator.md)
  A music item that represents a curator.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/track)*