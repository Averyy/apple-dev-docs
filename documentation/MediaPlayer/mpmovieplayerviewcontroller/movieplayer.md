# moviePlayer

**Framework**: Media Player  
**Kind**: property

The movie player controller object used to present the movie.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var moviePlayer: MPMoviePlayerController! { get }
```

#### Discussion

The [`MPMoviePlayerController`](mpmovieplayercontroller.md) object in this property is created automatically by the receiver and cannot be changed. However, you can use the object to manage the presentation and configuration of the movie playback.

## See Also

- [init!(contentURL: URL!)](mpmovieplayerviewcontroller/init(contenturl:).md)
  Returns a movie player view controller initialized with the specified movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieplayerviewcontroller/movieplayer)*