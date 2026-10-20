# init(contentURL:)

**Framework**: Media Player  
**Kind**: init  
**Role**: Initializer

Returns a movie player view controller initialized with the specified movie.

**Availability**:
- iOS 3.2+ - Deprecated in 9.0
- iPadOS 3.2+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use AVPlayerViewController in AVKit.

## Declaration

```swift
init!(contentURL: URL!)
```

```objc
- (instancetype) initWithContentURL:(NSURL *) contentURL;
```

#### Return Value

A movie player view controller initialized with the specified URL.

## Parameters

- `contentURL`: The URL that points to the content to be played.

## See Also

### New methods
- [var moviePlayer: MPMoviePlayerController!](./movieplayer.md)
  The movie player controller object used to present the movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieplayerviewcontroller/init(contenturl:))*