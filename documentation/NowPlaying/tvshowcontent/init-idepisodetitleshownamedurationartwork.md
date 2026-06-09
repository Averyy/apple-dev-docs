# init(id:episodeTitle:showName:duration:artwork:)

**Framework**: Now Playing  
**Kind**: init

Creates TV show episode content.

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
init(id: String, episodeTitle: String, showName: String, duration: MediaDuration?, artwork: Artwork?)
```

## Parameters

- `id`: A unique identifier for this episode.
- `episodeTitle`: The title of the individual episode.
- `showName`: The name of the series.
- `duration`: The total duration of the episode, or `nil` when unknown.
- `artwork`: Artwork for the episode, or `nil` when unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/tvshowcontent/init(id:episodetitle:showname:duration:artwork:))*