# VideoPlaybackController

**Framework**: RealityKit  
**Kind**: class

An object that controls the playback of video for a video material.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency class VideoPlaybackController
```

## Topics

### Instance Properties
- [var audioInputMode: AudioResource.InputMode](videoplaybackcontroller/audioinputmode.md)
- [var currentImageSize: CGSize?](videoplaybackcontroller/currentimagesize-4m7b0.md)
  What is the width and height of currently playing video (for stereo, the width and height of each eye)? This is optional because the video may not currently be playing, or the size is otherwise not available.
- [var currentImageSize: CGSize?](videoplaybackcontroller/currentimagesize-85cha.md)
  What is the width and height of currently playing video (for stereo, the width and height of each eye)? This is optional because the video may not currently be playing, or the size is otherwise not available.
- [var currentViewingMode: VideoPlaybackController.ViewingMode?](videoplaybackcontroller/currentviewingmode-2x2m.md)
  Is the currently playing video in mono or stereo? This is optional because the video may not currently be playing, or the mode is otherwise not available.
- [var currentViewingMode: VideoPlaybackController.ViewingMode?](videoplaybackcontroller/currentviewingmode-fo2v.md)
  Is the currently playing video in mono or stereo? This is optional because the video may not currently be playing, or the mode is otherwise not available.
- [var preferredViewingMode: VideoPlaybackController.ViewingMode](videoplaybackcontroller/preferredviewingmode-5fqz4.md)
  Do we want to play stereo video in mono or stereo? Default is to play in stereo.
- [var preferredViewingMode: VideoPlaybackController.ViewingMode](videoplaybackcontroller/preferredviewingmode-9sstw.md)
  Do we want to play stereo video in mono or stereo? Default is to play in stereo.
- [var reverbSendLevel: AudioPlaybackController.Decibel](videoplaybackcontroller/reverbsendlevel.md)
### Enumerations
- [VideoPlaybackController.ViewingMode](videoplaybackcontroller/viewingmode-38c52.md)
  Options for viewing video playback.
- [VideoPlaybackController.ViewingMode](videoplaybackcontroller/viewingmode-42yh2.md)
  Options for viewing video playback.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct VideoPlayerComponent](videoplayercomponent.md)
  A component that supports general video-playback experience with an AV player.
- [VideoPlayerComponent.ImmersiveViewingMode](videoplayercomponent/immersiveviewingmode-swift.enum.md)
  Options for viewing the video during immersive-media playback.
- [struct VideoMaterial](videomaterial.md)
  A material that supports animated textures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/videoplaybackcontroller)*