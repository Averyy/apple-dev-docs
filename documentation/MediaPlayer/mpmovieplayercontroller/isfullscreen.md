# isFullscreen

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the movie player is in full-screen mode.

**Availability**:
- iOS 3.2+ - Deprecated in 9.0
- iPadOS 3.2+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use AVPlayerViewController in AVKit

## Declaration

```swift
var isFullscreen: Bool { get set }
```

```objc
@property (nonatomic, getter=isFullscreen) BOOL fullscreen;
```

## Discussion

The default value of this property is [`false`](../../Swift/false.md). Changing the value of this property causes the movie player to enter or exit full-screen mode immediately. If you want to animate the transition to full-screen mode, use the [`setFullscreen(_:animated:)`](./setfullscreen%28_,animated%29.md) method instead.

Whenever the movie player enters or exits full-screen mode, it posts appropriate notifications to reflect the change. For example, upon entering full-screen mode, it posts [`MPMoviePlayerWillEnterFullscreenNotification`](../mpmovieplayerwillenterfullscreennotification.md) and [`MPMoviePlayerDidEnterFullscreenNotification`](../mpmovieplayerdidenterfullscreennotification.md) notifications. Upon exiting from full-screen mode, it posts [`MPMoviePlayerWillExitFullscreenNotification`](../mpmovieplayerwillexitfullscreennotification.md) and [`MPMoviePlayerDidExitFullscreenNotification`](../mpmovieplayerdidexitfullscreennotification.md) notifications.

The value of this property may also change as a result of the user interacting with the movie player controls.

## See Also

### Accessing movie properties
- [var contentURL: URL!](./contenturl.md)
  The URL that points to the movie file.
- [var movieSourceType: MPMovieSourceType](./moviesourcetype.md)
  The playback type of the movie.
- [var movieMediaTypes: MPMovieMediaTypeMask](./moviemediatypes.md)
  The types of media available in the movie.
- [var allowsAirPlay: Bool](./allowsairplay.md)
  Specifies whether the movie player allows AirPlay movie playback.
- [var isAirPlayVideoActive: Bool](./isairplayvideoactive.md)
  Indicates whether the movie player is currently playing video via AirPlay.
- [var naturalSize: CGSize](./naturalsize.md)
  The width and height of the movie frame.
- [func setFullscreen(Bool, animated: Bool)](./setfullscreen%28_,animated%29.md)
  Causes the movie player to enter or exit full-screen mode.
- [var scalingMode: MPMovieScalingMode](./scalingmode.md)
  The scaling mode to use when displaying the movie.
- [var controlStyle: MPMovieControlStyle](./controlstyle.md)
  The style of the playback controls.
- [var useApplicationAudioSession: Bool](./useapplicationaudiosession.md)
  A Boolean value that indicates whether the movie player should use the app’s audio session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/isfullscreen)*