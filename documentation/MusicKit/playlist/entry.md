# Playlist.Entry

**Framework**: MusicKit  
**Kind**: struct  
**Role**: Structure

A music item that represents a playlist entry.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct Entry
```

## Topics

### Instance Properties
- [var albumTitle: String?](./entry/albumtitle.md)
  The title of the album the playlist entry appears on.
- [var artistName: String](./entry/artistname.md)
  The artist’s name.
- [var artistURL: URL?](./entry/artisturl.md)
  The artist’s URL.
- [var artwork: Artwork?](./entry/artwork.md)
  The artwork of the playlist entry.
- [var contentRating: ContentRating?](./entry/contentrating.md)
  The rating of the content.
- [var duration: TimeInterval?](./entry/duration.md)
  The duration of the playlist entry.
- [var editorialNotes: EditorialNotes?](./entry/editorialnotes.md)
  The editorial notes for the playlist entry.
- [var genreNames: [String]](./entry/genrenames.md)
  The names of the playlist entry’s associated genres.
- [let id: MusicItemID](./entry/id.md)
  The unique identifier for the playlist entry.
- [var isrc: String?](./entry/isrc.md)
  The International Standard Recording Code (ISRC) for the playlist entry.
- [var item: Playlist.Entry.Item?](./entry/item-swift.property.md)
  The item of the playlist entry.
- [var lastPlayedDate: Date?](./entry/lastplayeddate.md)
  The date when the user last played the playlist entry on this device.
- [var libraryAddedDate: Date?](./entry/libraryaddeddate.md)
  The date when the user added the playlist entry to the library.
- [var playCount: Int?](./entry/playcount.md)
  The number of times the user played the playlist entry.
- [var playParameters: PlayParameters?](./entry/playparameters.md)
  The parameters to use to play the playlist entry.
- [var position: Int](./entry/position.md)
  The position of the playlist entry.
- [var previewAssets: [PreviewAsset]?](./entry/previewassets.md)
  The preview assets for the playlist entry.
- [var releaseDate: Date?](./entry/releasedate.md)
  The release date (or expected for pre-release) of the playlist entry.
- [var title: String](./entry/title.md)
  The title of the playlist entry.
- [var url: URL?](./entry/url.md)
  The URL for the playlist entry.
### Enumerations
- [Playlist.Entry.Item](./entry/item-swift.enum.md)
  An item that corresponds to an entry in a playlist.
### Default Implementations
- [MusicLibraryRequestable Implementations](./entry/musiclibraryrequestable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [Identifiable](../../Swift/identifiable.md)
- [MusicItem](../musicitem.md)
- [MusicLibraryAddable](../musiclibraryaddable.md)
- [MusicLibraryRequestable](../musiclibraryrequestable.md)
- [MusicPlaylistAddable](../musicplaylistaddable.md)
- [MusicPropertyContainer](../musicpropertycontainer.md)
- [PlayableMusicItem](../playablemusicitem.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/playlist/entry)*