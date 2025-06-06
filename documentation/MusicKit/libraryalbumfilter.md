# LibraryAlbumFilter

**Framework**: MusicKit  
**Kind**: protocol

Album properties your app uses as a filter for a library request.

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
protocol LibraryAlbumFilter
```

## Topics

### Instance Properties
- [var artistName: String](libraryalbumfilter/artistname.md)
  The artist’s name.
- [var artists: MusicItemCollection<Artist>?](libraryalbumfilter/artists.md)
  The album’s associated artists.
- [var genres: MusicItemCollection<Genre>?](libraryalbumfilter/genres.md)
  The genres for the album.
- [var id: MusicItemID](libraryalbumfilter/id.md)
  The unique identifier for the album.
- [var isCompilation: Bool?](libraryalbumfilter/iscompilation.md)
  A Boolean value that indicates whether the album is a compilation.
- [var title: String](libraryalbumfilter/title.md)
  The title of the album.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/libraryalbumfilter)*