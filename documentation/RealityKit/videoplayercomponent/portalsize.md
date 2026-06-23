# portalSize

**Framework**: RealityKit  
**Kind**: property

The size of the portal window for immersive video playback, in meters.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
var portalSize: SIMD2<Float> { get set }
```

#### Discussion

Use this property to control the dimensions of the portal window when [`desiredImmersiveViewingMode`](videoplayercomponent/desiredimmersiveviewingmode.md) is [`VideoPlayerComponent.ImmersiveViewingMode.portal`](videoplayercomponent/immersiveviewingmode-swift.enum/portal.md). The first component specifies the width and the second component specifies the height, both in meters.

The default value is `[1.0, 0.5625]`, which produces a 16:9 aspect ratio.

You can assign a new value before immersive playback transitions to portal mode, or while playback is already in portal mode to resize the portal in place. Both components must be greater than zero; if you assign a non-positive width or height, the property keeps its previous value.

```swift
var component = VideoPlayerComponent(avPlayer: player)

// Use a 4:3 immersive portal that's one meter wide.
component.portalSize = [1.0, 0.75]

// Render the immersive video into a portal window.
component.desiredImmersiveViewingMode = .portal
```

This property doesn’t apply to spatial videos.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/videoplayercomponent/portalsize)*