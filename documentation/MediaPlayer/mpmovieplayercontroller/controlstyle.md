# controlStyle

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

The style of the playback controls.

**Availability**:
- iOS 3.2+ - Deprecated in 9.0
- iPadOS 3.2+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use AVPlayerViewController in AVKit

## Declaration

```swift
var controlStyle: MPMovieControlStyle { get set }
```

```objc
@property (nonatomic) MPMovieControlStyle controlStyle;
```

## Discussion

The default value of this property is [`default`](../mpmoviecontrolstyle/default.md). You can change the value of this property to change the style of the controls or to hide the controls altogether. For a list of available control styles, see [`MPMovieControlStyle`](../mpmoviecontrolstyle.md).

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
- [var isFullscreen: Bool](./isfullscreen.md)
  A Boolean that indicates whether the movie player is in full-screen mode.
- [func setFullscreen(Bool, animated: Bool)](./setfullscreen%28_,animated%29.md)
  Causes the movie player to enter or exit full-screen mode.
- [var scalingMode: MPMovieScalingMode](./scalingmode.md)
  The scaling mode to use when displaying the movie.
- [var useApplicationAudioSession: Bool](./useapplicationaudiosession.md)
  A Boolean value that indicates whether the movie player should use the app’s audio session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/controlstyle)*