# isFullscreen

**Framework**: Media Player  
**Kind**: property

A Boolean that indicates whether the movie player is in full-screen mode.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+

## Declaration

```swift
var isFullscreen: Bool { get set }
```

#### Discussion

The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false). Changing the value of this property causes the movie player to enter or exit full-screen mode immediately. If you want to animate the transition to full-screen mode, use the [`setFullscreen(_:animated:)`](mpmovieplayercontroller/setfullscreen(_:animated:).md) method instead.

Whenever the movie player enters or exits full-screen mode, it posts appropriate notifications to reflect the change. For example, upon entering full-screen mode, it posts [`MPMoviePlayerWillEnterFullscreenNotification`](mpmovieplayerwillenterfullscreennotification.md) and [`MPMoviePlayerDidEnterFullscreenNotification`](mpmovieplayerdidenterfullscreennotification.md) notifications. Upon exiting from full-screen mode, it posts [`MPMoviePlayerWillExitFullscreenNotification`](mpmovieplayerwillexitfullscreennotification.md) and [`MPMoviePlayerDidExitFullscreenNotification`](mpmovieplayerdidexitfullscreennotification.md) notifications.

The value of this property may also change as a result of the user interacting with the movie player controls.

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
- [func setFullscreen(Bool, animated: Bool)](mpmovieplayercontroller/setfullscreen(_:animated:).md)
  Causes the movie player to enter or exit full-screen mode.
- [var scalingMode: MPMovieScalingMode](mpmovieplayercontroller/scalingmode.md)
  The scaling mode to use when displaying the movie.
- [var controlStyle: MPMovieControlStyle](mpmovieplayercontroller/controlstyle.md)
  The style of the playback controls.
- [var useApplicationAudioSession: Bool](mpmovieplayercontroller/useapplicationaudiosession.md)
  A Boolean value that indicates whether the movie player should use the app’s audio session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/isfullscreen)*