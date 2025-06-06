# MusicLibrarySearchResponse

**Framework**: MusicKit  
**Kind**: struct

An object that contains results for a library search request.

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
struct MusicLibrarySearchResponse
```

## Topics

### Operators
- [static func == (MusicLibrarySearchResponse, MusicLibrarySearchResponse) -> Bool](musiclibrarysearchresponse/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [let albums: MusicItemCollection<Album>](musiclibrarysearchresponse/albums.md)
  A collection of albums.
- [let artists: MusicItemCollection<Artist>](musiclibrarysearchresponse/artists.md)
  A collection of artists.
- [var hashValue: Int](musiclibrarysearchresponse/hashvalue.md)
  The hash value.
- [let musicVideos: MusicItemCollection<MusicVideo>](musiclibrarysearchresponse/musicvideos.md)
  A collection of music videos.
- [let playlists: MusicItemCollection<Playlist>](musiclibrarysearchresponse/playlists.md)
  A collection of playlists.
- [let songs: MusicItemCollection<Song>](musiclibrarysearchresponse/songs.md)
  A collection of songs.
- [let topResults: MusicItemCollection<MusicLibrarySearchResponse.TopResult>](musiclibrarysearchresponse/topresults.md)
  A collection of top results.
### Instance Methods
- [func hash(into: inout Hasher)](musiclibrarysearchresponse/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Enumerations
- [MusicLibrarySearchResponse.TopResult](musiclibrarysearchresponse/topresult.md)
  An item that represents one of the top results in a library search response.
### Default Implementations
- [CustomDebugStringConvertible Implementations](musiclibrarysearchresponse/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](musiclibrarysearchresponse/customstringconvertible-implementations.md)
- [Equatable Implementations](musiclibrarysearchresponse/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musiclibrarysearchresponse)*