# Playlist.Entry

**Framework**: MusicKit  
**Kind**: struct

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
- [var albumTitle: String?](playlist/entry/albumtitle.md)
  The title of the album the playlist entry appears on.
- [var artistName: String](playlist/entry/artistname.md)
  The artist’s name.
- [var artistURL: URL?](playlist/entry/artisturl.md)
  The artist’s URL.
- [var artwork: Artwork?](playlist/entry/artwork.md)
  The artwork of the playlist entry.
- [var contentRating: ContentRating?](playlist/entry/contentrating.md)
  The rating of the content.
- [var duration: TimeInterval?](playlist/entry/duration.md)
  The duration of the playlist entry.
- [var editorialNotes: EditorialNotes?](playlist/entry/editorialnotes.md)
  The editorial notes for the playlist entry.
- [var genreNames: [String]](playlist/entry/genrenames.md)
  The names of the playlist entry’s associated genres.
- [let id: MusicItemID](playlist/entry/id.md)
  The unique identifier for the playlist entry.
- [var isrc: String?](playlist/entry/isrc.md)
  The International Standard Recording Code (ISRC) for the playlist entry.
- [var item: Playlist.Entry.Item?](playlist/entry/item-swift.property.md)
  The item of the playlist entry.
- [var lastPlayedDate: Date?](playlist/entry/lastplayeddate.md)
  The date when the user last played the playlist entry on this device.
- [var libraryAddedDate: Date?](playlist/entry/libraryaddeddate.md)
  The date when the user added the playlist entry to the library.
- [var playCount: Int?](playlist/entry/playcount.md)
  The number of times the user played the playlist entry.
- [var playParameters: PlayParameters?](playlist/entry/playparameters.md)
  The parameters to use to play the playlist entry.
- [var position: Int](playlist/entry/position.md)
  The position of the playlist entry.
- [var previewAssets: [PreviewAsset]?](playlist/entry/previewassets.md)
  The preview assets for the playlist entry.
- [var releaseDate: Date?](playlist/entry/releasedate.md)
  The release date (or expected for pre-release) of the playlist entry.
- [var title: String](playlist/entry/title.md)
  The title of the playlist entry.
- [var url: URL?](playlist/entry/url.md)
  The URL for the playlist entry.
### Enumerations
- [Playlist.Entry.Item](playlist/entry/item-swift.enum.md)
  An item that corresponds to an entry in a playlist.
### Default Implementations
- [MusicLibraryRequestable Implementations](playlist/entry/musiclibraryrequestable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [MusicItem](musicitem.md)
- [MusicLibraryAddable](musiclibraryaddable.md)
- [MusicLibraryRequestable](musiclibraryrequestable.md)
- [MusicPlaylistAddable](musicplaylistaddable.md)
- [MusicPropertyContainer](musicpropertycontainer.md)
- [PlayableMusicItem](playablemusicitem.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/playlist/entry)*