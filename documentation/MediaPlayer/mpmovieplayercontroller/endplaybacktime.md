# endPlaybackTime

**Framework**: Media Player  
**Kind**: property

The end time (measured in seconds) for playback of the movie.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+

## Declaration

```swift
var endPlaybackTime: TimeInterval { get set }
```

#### Discussion

The default value of this property is -1, which indicates the natural end time of the movie. This property is not applicable for streamed content.

## See Also

- [var loadState: MPMovieLoadState](mpmovieplayercontroller/loadstate.md)
  The network load state of the movie player.
- [var playbackState: MPMoviePlaybackState](mpmovieplayercontroller/playbackstate.md)
  The current playback state of the movie player.
- [var initialPlaybackTime: TimeInterval](mpmovieplayercontroller/initialplaybacktime.md)
  The time, specified in seconds within the video timeline, when playback should start.
- [var shouldAutoplay: Bool](mpmovieplayercontroller/shouldautoplay.md)
  A Boolean that indicates whether a movie should begin playback automatically.
- [var readyForDisplay: Bool](mpmovieplayercontroller/readyfordisplay.md)
  A Boolean that indicates whether the first video frame of the movie is ready to be displayed.
- [var repeatMode: MPMovieRepeatMode](mpmovieplayercontroller/repeatmode.md)
  Determines how the movie player repeats the playback of the movie.
- [var timedMetadata: [Any]!](mpmovieplayercontroller/timedmetadata.md)
  Obtains the most recent time-based metadata provided by the streamed movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/endplaybacktime)*