# useApplicationAudioSession

**Framework**: Media Player  
**Kind**: property

A Boolean value that indicates whether the movie player should use the app’s audio session.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var useApplicationAudioSession: Bool { get set }
```

#### Discussion

The default value of this property is [`true`](https://developer.apple.com/documentation/swift/true). Setting this property to [`false`](https://developer.apple.com/documentation/swift/false) causes the movie player to use a system-supplied audio session with a non-mixable playback category.

When this property is [`true`](https://developer.apple.com/documentation/swift/true), the movie player shares the app’s audio session. This give you control over how the movie player content interacts with your audio and with audio from other apps, such as the iPod. For important guidance on using this feature, see [`Audio Session Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Audio/Conceptual/AudioSessionProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007875) in [`Audio Session Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Audio/Conceptual/AudioSessionProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007875).

Changing the value of this property does not affect the currently playing movie. For the new setting to take effect, you must stop playback and then start it again.

##### Special Considerations

In iOS 3.1 and earlier, a movie player always uses a system-supplied audio session. To obtain that same behavior in iOS 3.2 and newer, you must set this property’s value to [`false`](https://developer.apple.com/documentation/swift/false).

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
- [var controlStyle: MPMovieControlStyle](mpmovieplayercontroller/controlstyle.md)
  The style of the playback controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/useapplicationaudiosession)*