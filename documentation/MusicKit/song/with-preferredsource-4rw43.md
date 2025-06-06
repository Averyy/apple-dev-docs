# with(_:preferredSource:)

**Framework**: MusicKit  
**Kind**: method

Loads a new instance of the music item that includes the specified properties.

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
func with(_ properties: PartialMusicAsyncProperty<Self>..., preferredSource: MusicPropertySource) async throws -> Self
```

#### Discussion

This asynchronous method fetches a more complete representation of the receiver, loading the contents for each property you request from either the Apple Music catalog or the user’s library, depending on the preferred source as well the availability of the content in those respective data sources.

For example, if you want to load the [`tracks`](partialmusicproperty/tracks-9mk2l.md) relationship for an [`Album`](album.md), as found in the user’s library, as well as other associations of content that only live in the Apple Music catalog, like the [`recordLabels`](partialmusicproperty/recordlabels.md) and [`relatedAlbums`](partialmusicproperty/relatedalbums.md) associations, you can use this code:

```swift
let album: Album = …
let detailedAlbum = try await album.with(
    .tracks,
    .recordLabels,
    .relatedAlbums, 
    preferredSource: .library
)
```

Here, because the [`tracks`](partialmusicproperty/tracks-9mk2l.md) relationship for an [`Album`](album.md) is supported in both the library and the catalog, and because the this code specifically requests [`MusicPropertySource.library`](musicpropertysource/library.md) as the preferred source, the framework will load the tracks from the user’s library. However, because the [`recordLabels`](partialmusicproperty/recordlabels.md) and [`relatedAlbums`](partialmusicproperty/relatedalbums.md) associations are only available in the Apple Music catalog, the framework will also issue a network request to Apple Music API to fetch those associations of content from the catalog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/song/with(_:preferredsource:)-4rw43)*