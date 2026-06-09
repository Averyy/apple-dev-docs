# init(id:songTitle:artistName:albumName:type:duration:artwork:)

**Framework**: Now Playing  
**Kind**: init

Creates music content with the specified metadata.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
init(id: String, songTitle: String, artistName: String, albumName: String, type: MediaType, duration: MediaDuration?, artwork: Artwork?)
```

## Parameters

- `id`: A unique identifier for this track.
- `songTitle`: The song’s display title.
- `artistName`: The name of the artist or performer.
- `albumName`: The album this track belongs to.
- `type`: The media type.
- `duration`: The total duration of the track, or `nil` when unknown.
- `artwork`: Album artwork for the track, or `nil` when unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/musiccontent/init(id:songtitle:artistname:albumname:type:duration:artwork:))*