# loadState

**Framework**: Media Player  
**Kind**: property

The network load state of the movie player.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+

## Declaration

```swift
var loadState: MPMovieLoadState { get }
```

#### Discussion

See the [`MPMovieLoadState`](mpmovieloadstate.md) enumeration for possible values of this property. To be notified of changes to the load state of a movie player, register for the [`MPMoviePlayerLoadStateDidChangeNotification`](mpmovieplayerloadstatedidchangenotification.md) notification.

## See Also

- [var playbackState: MPMoviePlaybackState](mpmovieplayercontroller/playbackstate.md)
  The current playback state of the movie player.
- [var initialPlaybackTime: TimeInterval](mpmovieplayercontroller/initialplaybacktime.md)
  The time, specified in seconds within the video timeline, when playback should start.
- [var endPlaybackTime: TimeInterval](mpmovieplayercontroller/endplaybacktime.md)
  The end time (measured in seconds) for playback of the movie.
- [var shouldAutoplay: Bool](mpmovieplayercontroller/shouldautoplay.md)
  A Boolean that indicates whether a movie should begin playback automatically.
- [var readyForDisplay: Bool](mpmovieplayercontroller/readyfordisplay.md)
  A Boolean that indicates whether the first video frame of the movie is ready to be displayed.
- [var repeatMode: MPMovieRepeatMode](mpmovieplayercontroller/repeatmode.md)
  Determines how the movie player repeats the playback of the movie.
- [var timedMetadata: [Any]!](mpmovieplayercontroller/timedmetadata.md)
  Obtains the most recent time-based metadata provided by the streamed movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/loadstate)*