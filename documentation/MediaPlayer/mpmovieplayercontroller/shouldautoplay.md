# shouldAutoplay

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether a movie should begin playback automatically.

**Availability**:
- iOS 3.2+ - Deprecated in 9.0
- iPadOS 3.2+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use AVPlayerViewController in AVKit

## Declaration

```swift
var shouldAutoplay: Bool { get set }
```

```objc
@property (nonatomic) BOOL shouldAutoplay;
```

## Discussion

The default value of this property is [`true`](../../Swift/true.md). This property determines whether the playback of network-based content begins automatically when there is enough buffered data to ensure uninterrupted playback.

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
- [var readyForDisplay: Bool](./readyfordisplay.md)
  A Boolean that indicates whether the first video frame of the movie is ready to be displayed.
- [var repeatMode: MPMovieRepeatMode](./repeatmode.md)
  Determines how the movie player repeats the playback of the movie.
- [var timedMetadata: [Any]!](./timedmetadata.md)
  Obtains the most recent time-based metadata provided by the streamed movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/shouldautoplay)*