# init(contentURL:)

**Framework**: Media Player  
**Kind**: init

Returns a movie player view controller initialized with the specified movie.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
init!(contentURL: URL!)
```

#### Return Value

A movie player view controller initialized with the specified URL.

## Parameters

- `contentURL`: The URL that points to the content to be played.

## See Also

- [var moviePlayer: MPMoviePlayerController!](mpmovieplayerviewcontroller/movieplayer.md)
  The movie player controller object used to present the movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieplayerviewcontroller/init(contenturl:))*