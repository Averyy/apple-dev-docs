# init(id:songTitle:artistName:albumName:type:duration:artwork:animatedArtwork:)

**Framework**: Now Playing  
**Kind**: init

Creates music content with static and animated artwork.

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
init(id: String, songTitle: String, artistName: String, albumName: String, type: MediaType, duration: MediaDuration?, artwork: Artwork, animatedArtwork: AnimatedArtwork?)
```

#### Discussion

Use this initializer when your track has a matching animated asset, for example motion album art.

## Parameters

- `id`: A unique identifier for this track.
- `songTitle`: The song’s display title.
- `artistName`: The name of the artist or performer.
- `albumName`: The album this track belongs to.
- `type`: The media type.
- `duration`: The total duration of the track, or `nil` when unknown.
- `artwork`: Static artwork for the track.
- `animatedArtwork`: Animated artwork for the track, or `nil` when unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/musiccontent/init(id:songtitle:artistname:albumname:type:duration:artwork:animatedartwork:))*