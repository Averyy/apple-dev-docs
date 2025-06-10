# Playlist.Entry.Item

**Framework**: MusicKit  
**Kind**: enum

An item that corresponds to an entry in a playlist.

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
enum Item
```

## Topics

### Operators
- [static func == (Playlist.Entry.Item, Playlist.Entry.Item) -> Bool](playlist/entry/item-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [Playlist.Entry.Item.musicVideo(_:)](playlist/entry/item-swift.enum/musicvideo(_:).md)
  An item that corresponds to a music video.
- [Playlist.Entry.Item.song(_:)](playlist/entry/item-swift.enum/song(_:).md)
  An item that corresponds to a song.
### Instance Properties
- [var albumTitle: String?](playlist/entry/item-swift.enum/albumtitle.md)
  The title of the album the playlist entry’s item appears on.
- [var artistName: String](playlist/entry/item-swift.enum/artistname.md)
  The artist’s name.
- [var artistURL: URL?](playlist/entry/item-swift.enum/artisturl.md)
  The artist’s URL.
- [var artwork: Artwork?](playlist/entry/item-swift.enum/artwork.md)
  The artwork for the playlist entry’s item.
- [var contentRating: ContentRating?](playlist/entry/item-swift.enum/contentrating.md)
  The rating of the content.
- [var duration: TimeInterval?](playlist/entry/item-swift.enum/duration.md)
  The duration of the playlist entry’s item.
- [var editorialNotes: EditorialNotes?](playlist/entry/item-swift.enum/editorialnotes.md)
  The editorial notes for the playlist entry’s item.
- [var genreNames: [String]](playlist/entry/item-swift.enum/genrenames.md)
  The names of the playlist entry’s item associated genres.
- [var hashValue: Int](playlist/entry/item-swift.enum/hashvalue.md)
  The hash value.
- [var id: MusicItemID](playlist/entry/item-swift.enum/id-swift.property.md)
  The unique identifier for the playlist entry item.
- [var isrc: String?](playlist/entry/item-swift.enum/isrc.md)
  The International Standard Recording Code (ISRC) for the playlist entry’s item.
- [var lastPlayedDate: Date?](playlist/entry/item-swift.enum/lastplayeddate.md)
  The date when the user last played the playlist entry’s item on this device.
- [var libraryAddedDate: Date?](playlist/entry/item-swift.enum/libraryaddeddate.md)
  The date when the user added the playlist entry’s item to the library.
- [var playCount: Int?](playlist/entry/item-swift.enum/playcount.md)
  The number of times the user played the playlist entry’s item.
- [var playParameters: PlayParameters?](playlist/entry/item-swift.enum/playparameters.md)
  The parameters to use to play the playlist entry’s item.
- [var previewAssets: [PreviewAsset]?](playlist/entry/item-swift.enum/previewassets.md)
  The preview assets for the playlist entry’s item.
- [var releaseDate: Date?](playlist/entry/item-swift.enum/releasedate.md)
  The release date of the playlist entry’s item.
- [var title: String](playlist/entry/item-swift.enum/title.md)
  The title of the playlist entry’s item.
- [var url: URL?](playlist/entry/item-swift.enum/url.md)
  The URL for the playlist entry’s item.
### Instance Methods
- [func hash(into: inout Hasher)](playlist/entry/item-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [Playlist.Entry.Item.ID](playlist/entry/item-swift.enum/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.
### Default Implementations
- [CustomDebugStringConvertible Implementations](playlist/entry/item-swift.enum/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](playlist/entry/item-swift.enum/customstringconvertible-implementations.md)
- [Decodable Implementations](playlist/entry/item-swift.enum/decodable-implementations.md)
- [Encodable Implementations](playlist/entry/item-swift.enum/encodable-implementations.md)
- [Equatable Implementations](playlist/entry/item-swift.enum/equatable-implementations.md)
- [MusicItem Implementations](playlist/entry/item-swift.enum/musicitem-implementations.md)

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
- [MusicPropertyContainer](musicpropertycontainer.md)
- [PlayableMusicItem](playablemusicitem.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/playlist/entry/item-swift.enum)*