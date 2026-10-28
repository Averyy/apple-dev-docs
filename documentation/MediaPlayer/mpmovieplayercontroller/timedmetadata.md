# timedMetadata

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

Obtains the most recent time-based metadata provided by the streamed movie.

**Availability**:
- iOS 4.0+ - Deprecated in 9.0
- iPadOS 4.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use AVPlayerViewController in AVKit.

## Declaration

```swift
var timedMetadata: [Any]! { get }
```

```objc
@property (nonatomic, readonly) NSArray * timedMetadata;
```

## Return Value

An array of the most recent [`MPTimedMetadata`](../mptimedmetadata.md) objects provided by the streamed movie.

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
- [var repeatMode: MPMovieRepeatMode](./repeatmode.md)
  Determines how the movie player repeats the playback of the movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/timedmetadata)*