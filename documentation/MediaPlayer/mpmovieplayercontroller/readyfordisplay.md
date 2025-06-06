# readyForDisplay

**Framework**: Media Player  
**Kind**: property

A Boolean that indicates whether the first video frame of the movie is ready to be displayed.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var readyForDisplay: Bool { get }
```

#### Discussion

The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false). This property returns [`true`](https://developer.apple.com/documentation/swift/true) if the first video frame is ready to be displayed and returns [`false`](https://developer.apple.com/documentation/swift/false) if there are no video tracks associated. When the value of this property changes to [`true`](https://developer.apple.com/documentation/swift/true), a [`MPMoviePlayerReadyForDisplayDidChangeNotification`](mpmovieplayerreadyfordisplaydidchangenotification.md) is sent.

## See Also

- [var loadState: MPMovieLoadState](mpmovieplayercontroller/loadstate.md)
  The network load state of the movie player.
- [var playbackState: MPMoviePlaybackState](mpmovieplayercontroller/playbackstate.md)
  The current playback state of the movie player.
- [var initialPlaybackTime: TimeInterval](mpmovieplayercontroller/initialplaybacktime.md)
  The time, specified in seconds within the video timeline, when playback should start.
- [var endPlaybackTime: TimeInterval](mpmovieplayercontroller/endplaybacktime.md)
  The end time (measured in seconds) for playback of the movie.
- [var shouldAutoplay: Bool](mpmovieplayercontroller/shouldautoplay.md)
  A Boolean that indicates whether a movie should begin playback automatically.
- [var repeatMode: MPMovieRepeatMode](mpmovieplayercontroller/repeatmode.md)
  Determines how the movie player repeats the playback of the movie.
- [var timedMetadata: [Any]!](mpmovieplayercontroller/timedmetadata.md)
  Obtains the most recent time-based metadata provided by the streamed movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/readyfordisplay)*