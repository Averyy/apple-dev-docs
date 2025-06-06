# LibraryTrackFilter

**Framework**: MusicKit  
**Kind**: protocol

Track properties your app uses as a filter for a library request.

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
protocol LibraryTrackFilter
```

## Topics

### Instance Properties
- [var albumTitle: String?](librarytrackfilter/albumtitle.md)
  The title of the album the track appears on.
- [var albums: MusicItemCollection<Album>?](librarytrackfilter/albums.md)
  The track’s associated albums.
- [var artistName: String?](librarytrackfilter/artistname.md)
  The artist’s name.
- [var artists: MusicItemCollection<Artist>?](librarytrackfilter/artists.md)
  The track’s associated artists.
- [var genres: MusicItemCollection<Genre>?](librarytrackfilter/genres.md)
  The track’s associated genres.
- [var id: MusicItemID](librarytrackfilter/id.md)
  The unique identifier for the track.
- [var title: String](librarytrackfilter/title.md)
  The title of the track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/librarytrackfilter)*