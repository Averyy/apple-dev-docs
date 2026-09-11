# init(id:title:duration:artwork:animatedArtwork:)

**Framework**: Now Playing  
**Kind**: init

Creates movie content with static and animated artwork.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
init(id: String, title: String, duration: MediaDuration?, artwork: Artwork, animatedArtwork: AnimatedArtwork?)
```

## Parameters

- `id`: A unique identifier for this movie.
- `title`: The movie’s display title.
- `duration`: The total runtime, or `nil` when unknown.
- `artwork`: Static poster artwork.
- `animatedArtwork`: Animated artwork for the movie, or `nil` when unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/moviecontent/init(id:title:duration:artwork:animatedartwork:))*