# initialPlaybackTime

**Framework**: Media Player  
**Kind**: property

The time, specified in seconds within the video timeline, when playback should start.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+

## Declaration

```swift
var initialPlaybackTime: TimeInterval { get set }
```

#### Discussion

For progressively downloaded content, playback starts at the closest key frame prior to the provided time. For video-on-demand content, playback starts at the nearest segment boundary to the provided time. For live video streams, the playback start time is measured from the start of the current playlist and is rounded to the nearest segment boundary.

The default value of this property is -1, which indicates the natural start time of the movie.

## See Also

- [var loadState: MPMovieLoadState](mpmovieplayercontroller/loadstate.md)
  The network load state of the movie player.
- [var playbackState: MPMoviePlaybackState](mpmovieplayercontroller/playbackstate.md)
  The current playback state of the movie player.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/initialplaybacktime)*