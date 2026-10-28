# readyForDisplay

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the first video frame of the movie is ready to be displayed.

**Availability**:
- iOS 6.0+ - Deprecated in 9.0
- iPadOS 6.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```swift
var readyForDisplay: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL readyForDisplay;
```

## Discussion

The default value of this property is [`false`](../../Swift/false.md). This property returns [`true`](../../Swift/true.md) if the first video frame is ready to be displayed and returns [`false`](../../Swift/false.md) if there are no video tracks associated. When the value of this property changes to [`true`](../../Swift/true.md), a [`MPMoviePlayerReadyForDisplayDidChangeNotification`](../mpmovieplayerreadyfordisplaydidchangenotification.md) is sent.

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
- [var repeatMode: MPMovieRepeatMode](./repeatmode.md)
  Determines how the movie player repeats the playback of the movie.
- [var timedMetadata: [Any]!](./timedmetadata.md)
  Obtains the most recent time-based metadata provided by the streamed movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/readyfordisplay)*