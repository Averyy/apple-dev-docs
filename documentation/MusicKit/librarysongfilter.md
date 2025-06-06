# LibrarySongFilter

**Framework**: MusicKit  
**Kind**: protocol

Song properties your app uses as a filter for a library request.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
protocol LibrarySongFilter
```

## Topics

### Instance Properties
- [var albumTitle: String?](librarysongfilter/albumtitle.md)
  The title of the album the song appears on.
- [var albums: MusicItemCollection<Album>?](librarysongfilter/albums.md)
  The song’s associated albums.
- [var artistName: String?](librarysongfilter/artistname.md)
  The artist’s name.
- [var artists: MusicItemCollection<Artist>?](librarysongfilter/artists.md)
  The song’s associated artists.
- [var composerName: String?](librarysongfilter/composername.md)
  The name of the song’s composer.
- [var genres: MusicItemCollection<Genre>?](librarysongfilter/genres.md)
  The song’s associated genres.
- [var id: MusicItemID](librarysongfilter/id.md)
  The unique identifier for the song.
- [var title: String](librarysongfilter/title.md)
  The title of the song.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/librarysongfilter)*