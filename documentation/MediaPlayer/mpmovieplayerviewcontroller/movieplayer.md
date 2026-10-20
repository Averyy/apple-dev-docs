# moviePlayer

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

The movie player controller object used to present the movie.

**Availability**:
- iOS 3.2+ - Deprecated in 9.0
- iPadOS 3.2+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use AVPlayerViewController in AVKit.

## Declaration

```swift
var moviePlayer: MPMoviePlayerController! { get }
```

```objc
@property (nonatomic, readonly) MPMoviePlayerController * moviePlayer;
```

#### Discussion

The [`MPMoviePlayerController`](../mpmovieplayercontroller.md) object in this property is created automatically by the receiver and cannot be changed. However, you can use the object to manage the presentation and configuration of the movie playback.

## See Also

### New methods
- [init!(contentURL: URL!)](./init%28contenturl%29.md)
  Returns a movie player view controller initialized with the specified movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieplayerviewcontroller/movieplayer)*