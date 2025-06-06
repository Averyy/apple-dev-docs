# audioListener

**Framework**: RealityKit  
**Kind**: property

The entity that defines the listener position and orientation for spatial audio.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+

## Declaration

```swift
@MainActor
@preconcurrency var audioListener: Entity? { get set }
```

#### Discussion

Set the [`audioListener`](arview/audiolistener.md) to the entity in the scene from whose point of view RealityKit should render spatial audio.

By default, the property is set to `nil`, in which case the active camera acts as the audio listener. This is usually what you want, because the camera typically mirrors the user’s point of view.

## See Also

- [var environment: ARView.Environment](arview/environment-swift.property.md)
  The view’s background, lighting, and acoustic properties.
- [var physicsOrigin: Entity?](arview/physicsorigin.md)
  The entity that defines the origin of the scene’s physics simulation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/audiolistener)*