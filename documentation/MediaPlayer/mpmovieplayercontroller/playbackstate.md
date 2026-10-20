# playbackState

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

The current playback state of the movie player.

**Availability**:
- iOS 3.2+ - Deprecated in 9.0
- iPadOS 3.2+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use AVPlayerViewController in AVKit

## Declaration

```swift
var playbackState: MPMoviePlaybackState { get }
```

```objc
@property (nonatomic, readonly) MPMoviePlaybackState playbackState;
```

#### Discussion

The playback state is affected by programmatic calls to play, pause, or stop the movie player. It can also be affected by user interactions or by the network, in cases where streaming content cannot be buffered fast enough.

See the [`MPMoviePlaybackState`](../mpmovieplaybackstate.md) enumeration for possible values of this property. To be notified of changes to the playback state of a movie player, register for the [`MPMoviePlayerPlaybackStateDidChangeNotification`](../mpmovieplayerplaybackstatedidchangenotification.md) notification.

## See Also

### Controlling and monitoring playback
- [var loadState: MPMovieLoadState](./loadstate.md)
  The network load state of the movie player.
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
- [var timedMetadata: [Any]!](./timedmetadata.md)
  Obtains the most recent time-based metadata provided by the streamed movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/playbackstate)*