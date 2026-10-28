# useApplicationAudioSession

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the movie player should use the app’s audio session.

**Availability**:
- iOS 6.0+ - Deprecated in 9.0
- iPadOS 6.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: There is not replacement for this property and its use is discouraged.

## Declaration

```swift
var useApplicationAudioSession: Bool { get set }
```

```objc
@property (nonatomic) BOOL useApplicationAudioSession;
```

## Discussion

The default value of this property is [`true`](../../Swift/true.md). Setting this property to [`false`](../../Swift/false.md) causes the movie player to use a system-supplied audio session with a non-mixable playback category.

When this property is [`true`](../../Swift/true.md), the movie player shares the app’s audio session. This give you control over how the movie player content interacts with your audio and with audio from other apps, such as the iPod. For important guidance on using this feature, see [Audio Session Programming Guide](https://developer.apple.com/library/archive/documentation/Audio/Conceptual/AudioSessionProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007875) in [Audio Session Programming Guide](https://developer.apple.com/library/archive/documentation/Audio/Conceptual/AudioSessionProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007875).

Changing the value of this property does not affect the currently playing movie. For the new setting to take effect, you must stop playback and then start it again.

### Special considerations

In iOS 3.1 and earlier, a movie player always uses a system-supplied audio session. To obtain that same behavior in iOS 3.2 and newer, you must set this property’s value to [`false`](../../Swift/false.md).

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
- [var controlStyle: MPMovieControlStyle](./controlstyle.md)
  The style of the playback controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/useapplicationaudiosession)*