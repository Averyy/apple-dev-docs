# contentURL

**Framework**: Media Player  
**Kind**: property

The URL that points to the movie file.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+

## Declaration

```swift
var contentURL: URL! { get set }
```

#### Discussion

If you set this property while a movie is playing, that movie pauses and the new movie begins loading. The new movie starts playing at the beginning.

## See Also

- [var movieSourceType: MPMovieSourceType](mpmovieplayercontroller/moviesourcetype.md)
  The playback type of the movie.
- [var movieMediaTypes: MPMovieMediaTypeMask](mpmovieplayercontroller/moviemediatypes.md)
  The types of media available in the movie.
- [var allowsAirPlay: Bool](mpmovieplayercontroller/allowsairplay.md)
  Specifies whether the movie player allows AirPlay movie playback.
- [var isAirPlayVideoActive: Bool](mpmovieplayercontroller/isairplayvideoactive.md)
  Indicates whether the movie player is currently playing video via AirPlay.
- [var naturalSize: CGSize](mpmovieplayercontroller/naturalsize.md)
  The width and height of the movie frame.
- [var isFullscreen: Bool](mpmovieplayercontroller/isfullscreen.md)
  A Boolean that indicates whether the movie player is in full-screen mode.
- [func setFullscreen(Bool, animated: Bool)](mpmovieplayercontroller/setfullscreen(_:animated:).md)
  Causes the movie player to enter or exit full-screen mode.
- [var scalingMode: MPMovieScalingMode](mpmovieplayercontroller/scalingmode.md)
  The scaling mode to use when displaying the movie.
- [var controlStyle: MPMovieControlStyle](mpmovieplayercontroller/controlstyle.md)
  The style of the playback controls.
- [var useApplicationAudioSession: Bool](mpmovieplayercontroller/useapplicationaudiosession.md)
  A Boolean value that indicates whether the movie player should use the app’s audio session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/contenturl)*