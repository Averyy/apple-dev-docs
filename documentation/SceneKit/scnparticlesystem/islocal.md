# isLocal

**Framework**: SceneKit  
**Kind**: property

A Boolean value that specifies whether the particle simulation runs in the local coordinate space of the node containing it.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var isLocal: Bool { get set }
```

#### Discussion

If [`false`](https://developer.apple.com/documentation/swift/false) (the default), all positions, distances, and velocities in the particle system are in the scene’s world coordinate system. If [`true`](https://developer.apple.com/documentation/swift/true), the particle system runs in the local coordinate space of the node containing it.

Use this property to choose whether particles spawned by a moving emitter follow the system as it moves.

## See Also

- [func reset()](scnparticlesystem/reset.md)
  Returns the particle system to its initial state.
- [var speedFactor: CGFloat](scnparticlesystem/speedfactor.md)
  A multiplier for the speed at which SceneKit runs the particle simulation. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/islocal)*