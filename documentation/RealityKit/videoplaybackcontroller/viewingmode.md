# VideoPlaybackController.ViewingMode

**Framework**: RealityKit  
**Kind**: enum

Options for viewing video playback.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
enum ViewingMode
```

## Topics

### Operators
- [static func == (VideoPlaybackController.ViewingMode, VideoPlaybackController.ViewingMode) -> Bool](videoplaybackcontroller/viewingmode/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [VideoPlaybackController.ViewingMode.mono](videoplaybackcontroller/viewingmode/mono.md)
  A viewing mode that presents video in monoscopic mode.
- [VideoPlaybackController.ViewingMode.stereo](videoplaybackcontroller/viewingmode/stereo.md)
  A viewing mode that presents video in stereoscopic mode, if it’s available.
### Instance Properties
- [var hashValue: Int](videoplaybackcontroller/viewingmode/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](videoplaybackcontroller/viewingmode/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](videoplaybackcontroller/viewingmode/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [struct VideoPlayerComponent](videoplayercomponent.md)
  A component that supports general video-playback experience with an AV player.
- [VideoPlayerComponent.ImmersiveViewingMode](videoplayercomponent/immersiveviewingmode-swift.enum.md)
  Options for viewing the video during immersive-media playback.
- [struct VideoMaterial](videomaterial.md)
  A material that supports animated textures.
- [class VideoPlaybackController](videoplaybackcontroller.md)
  An object that controls the playback of video for a video material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/videoplaybackcontroller/viewingmode)*