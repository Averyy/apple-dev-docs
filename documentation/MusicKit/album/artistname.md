# artistName

**Framework**: MusicKit  
**Kind**: property

The artist’s name.

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
var artistName: String { get }
```

#### Discussion

You can find more precise information about this album’s artists in the [`artists`](album/artists.md) relationship, which, unlike [`artistName`](album/artistname.md), requires that you load it explicitly using the [`with(_:)`](musicpropertycontainer/with(_:).md) method, as in the following example:

```swift
    let detailedAlbum = try await album.with([.artists])
    let firstArtist = album.artists?.first
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/album/artistname)*