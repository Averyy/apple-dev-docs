# contentURL

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

The URL that points to the movie file.

**Availability**:
- iOS 3.2+ - Deprecated in 9.0
- iPadOS 3.2+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use AVPlayerViewController in AVKit

## Declaration

```swift
var contentURL: URL! { get set }
```

```objc
@property (nonatomic, copy) NSURL * contentURL;
```

## Discussion

If you set this property while a movie is playing, that movie pauses and the new movie begins loading. The new movie starts playing at the beginning.

## See Also

### Accessing movie properties
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
- [var isFullscreen: Bool](./isfullscreen.md)
  A Boolean that indicates whether the movie player is in full-screen mode.
- [func setFullscreen(Bool, animated: Bool)](./setfullscreen%28_,animated%29.md)
  Causes the movie player to enter or exit full-screen mode.
- [var scalingMode: MPMovieScalingMode](./scalingmode.md)
  The scaling mode to use when displaying the movie.
- [var controlStyle: MPMovieControlStyle](./controlstyle.md)
  The style of the playback controls.
- [var useApplicationAudioSession: Bool](./useapplicationaudiosession.md)
  A Boolean value that indicates whether the movie player should use the app’s audio session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/contenturl)*