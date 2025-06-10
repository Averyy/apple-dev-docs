# MusicLibraryRequestable

**Framework**: MusicKit  
**Kind**: protocol

A protocol for music items that your app can fetch by using a library request.

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
protocol MusicLibraryRequestable : MusicItem
```

## Topics

### Associated Types
- [associatedtype LibraryFilter](musiclibraryrequestable/libraryfilter.md)
  The associated type that contains the set of music item properties your app uses as a filter for a library request.
- [associatedtype LibrarySortProperties](musiclibraryrequestable/librarysortproperties.md)
  The associated type that contains the set of properties your app uses to sort results for a library request.

## Relationships

### Inherits From
- [MusicItem](musicitem.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [Album](album.md)
- [Artist](artist.md)
- [Genre](genre.md)
- [MusicVideo](musicvideo.md)
- [Playlist](playlist.md)
- [Playlist.Entry](playlist/entry.md)
- [Song](song.md)
- [Track](track.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musiclibraryrequestable)*