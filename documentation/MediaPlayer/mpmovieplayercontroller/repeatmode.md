# repeatMode

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

Determines how the movie player repeats the playback of the movie.

**Availability**:
- iOS 3.2+ - Deprecated in 9.0
- iPadOS 3.2+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use AVPlayerViewController in AVKit

## Declaration

```swift
var repeatMode: MPMovieRepeatMode { get set }
```

```objc
@property (nonatomic) MPMovieRepeatMode repeatMode;
```

## Discussion

The default value of this property is [`MPMovieRepeatMode.none`](../mpmovierepeatmode/none.md). For a list of available repeat modes, see [`MPMovieRepeatMode`](../mpmovierepeatmode.md).

## See Also

### Controlling and monitoring playback
- [var loadState: MPMovieLoadState](./loadstate.md)
  The network load state of the movie player.
- [var playbackState: MPMoviePlaybackState](./playbackstate.md)
  The current playback state of the movie player.
- [var initialPlaybackTime: TimeInterval](./initialplaybacktime.md)
  The time, specified in seconds within the video timeline, when playback should start.
- [var endPlaybackTime: TimeInterval](./endplaybacktime.md)
  The end time (measured in seconds) for playback of the movie.
- [var shouldAutoplay: Bool](./shouldautoplay.md)
  A Boolean that indicates whether a movie should begin playback automatically.
- [var readyForDisplay: Bool](./readyfordisplay.md)
  A Boolean that indicates whether the first video frame of the movie is ready to be displayed.
- [var timedMetadata: [Any]!](./timedmetadata.md)
  Obtains the most recent time-based metadata provided by the streamed movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/repeatmode)*