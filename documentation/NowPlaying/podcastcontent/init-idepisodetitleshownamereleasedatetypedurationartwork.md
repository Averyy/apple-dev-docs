# init(id:episodeTitle:showName:releaseDate:type:duration:artwork:)

**Framework**: Now Playing  
**Kind**: init

Creates podcast episode content.

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
init(id: String, episodeTitle: String, showName: String, releaseDate: Date?, type: MediaType, duration: MediaDuration?, artwork: Artwork?)
```

## Parameters

- `id`: A unique identifier for this episode.
- `episodeTitle`: The episode’s display title.
- `showName`: The name of the podcast show.
- `releaseDate`: The date this episode was released, or `nil` when unknown.
- `type`: The media type.
- `duration`: The total duration of the episode, or `nil` when unknown.
- `artwork`: Episode artwork, or `nil` when unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/podcastcontent/init(id:episodetitle:showname:releasedate:type:duration:artwork:))*