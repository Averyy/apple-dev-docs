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

### Enumeration Cases
- [VideoPlayerComponent.ImmersiveViewingMode.full](videoplayercomponent/immersiveviewingmode-swift.enum/full.md)
  A viewing mode that renders immersive video covering the viewer’s entire field of view.
- [VideoPlayerComponent.ImmersiveViewingMode.portal](videoplayercomponent/immersiveviewingmode-swift.enum/portal.md)
  A viewing mode that renders immersive video as a portal window matching the containing entity’s transform.
- [VideoPlayerComponent.ImmersiveViewingMode.progressive](videoplayercomponent/immersiveviewingmode-swift.enum/progressive.md)
  A viewing mode that renders immersive video covering the viewer’s field of view(partial to full) and the percentage coverage can be controller by crown button. This is not available for Spatial Video and will be not be acknowledged if the content is Spatial

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct VideoPlayerComponent](videoplayercomponent.md)
  A component that supports general video-playback experience with an AV player.
- [struct VideoMaterial](videomaterial.md)
  A material that supports animated textures.
- [class VideoPlaybackController](videoplaybackcontroller.md)
  An object that controls the playback of video for a video material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/videoplayercomponent/immersiveviewingmode-swift.enum)*