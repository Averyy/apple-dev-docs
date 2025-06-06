# controlStyle

**Framework**: Media Player  
**Kind**: property

The style of the playback controls.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+

## Declaration

```swift
var controlStyle: MPMovieControlStyle { get set }
```

#### Discussion

The default value of this property is [`default`](mpmoviecontrolstyle/default.md). You can change the value of this property to change the style of the controls or to hide the controls altogether. For a list of available control styles, see [`MPMovieControlStyle`](mpmoviecontrolstyle.md).

## See Also

- [var contentURL: URL!](mpmovieplayercontroller/contenturl.md)
  The URL that points to the movie file.
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
- [var useApplicationAudioSession: Bool](mpmovieplayercontroller/useapplicationaudiosession.md)
  A Boolean value that indicates whether the movie player should use the app’s audio session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/controlstyle)*