# VideoPlayerComponent.ImmersiveViewingMode

**Framework**: RealityKit  
**Kind**: enum

Options for viewing the video during immersive-media playback.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
enum ImmersiveViewingMode
```

#### Overview

This applies only to immersive media types.

## Topics

### Operators
- [static func == (VideoPlayerComponent.ImmersiveViewingMode, VideoPlayerComponent.ImmersiveViewingMode) -> Bool](videoplayercomponent/immersiveviewingmode-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [VideoPlayerComponent.ImmersiveViewingMode.full](videoplayercomponent/immersiveviewingmode-swift.enum/full.md)
  A viewing mode that renders immersive video covering the viewer’s entire field of view.
- [VideoPlayerComponent.ImmersiveViewingMode.portal](videoplayercomponent/immersiveviewingmode-swift.enum/portal.md)
  A viewing mode that renders immersive video as a portal window matching the containing entity’s transform.
### Instance Properties
- [var hashValue: Int](videoplayercomponent/immersiveviewingmode-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](videoplayercomponent/immersiveviewingmode-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](videoplayercomponent/immersiveviewingmode-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [struct VideoPlayerComponent](videoplayercomponent.md)
  A component that supports general video-playback experience with an AV player.
- [struct VideoMaterial](videomaterial.md)
  A material that supports animated textures.
- [class VideoPlaybackController](videoplaybackcontroller.md)
  An object that controls the playback of video for a video material.
- [VideoPlaybackController.ViewingMode](videoplaybackcontroller/viewingmode.md)
  Options for viewing video playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/videoplayercomponent/immersiveviewingmode-swift.enum)*