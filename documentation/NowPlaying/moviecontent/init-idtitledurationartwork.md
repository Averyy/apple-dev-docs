# init(id:title:duration:artwork:)

**Framework**: Now Playing  
**Kind**: init

Creates movie content.

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
init(id: String, title: String, duration: MediaDuration?, artwork: Artwork?)
```

## Parameters

- `id`: A unique identifier for this movie.
- `title`: The movie’s display title.
- `duration`: The total runtime, or `nil` when unknown.
- `artwork`: Poster artwork, or `nil` when unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/moviecontent/init(id:title:duration:artwork:))*