# init(id:episodeTitle:showName:duration:artwork:animatedArtwork:)

**Framework**: Now Playing  
**Kind**: init

Creates TV show episode content with static and animated artwork.

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
init(id: String, episodeTitle: String, showName: String, duration: MediaDuration?, artwork: Artwork, animatedArtwork: AnimatedArtwork?)
```

## Parameters

- `id`: A unique identifier for this episode.
- `episodeTitle`: The title of the individual episode.
- `showName`: The name of the series.
- `duration`: The total duration of the episode, or `nil` when unknown.
- `artwork`: Static artwork for the episode.
- `animatedArtwork`: Animated artwork for the episode, or `nil` when unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/tvshowcontent/init(id:episodetitle:showname:duration:artwork:animatedartwork:))*