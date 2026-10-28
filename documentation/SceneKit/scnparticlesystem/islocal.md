# isLocal

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that specifies whether the particle simulation runs in the local coordinate space of the node containing it.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var isLocal: Bool { get set }
```

```objc
@property (nonatomic, getter=isLocal) BOOL local;
```

## Discussion

If [`false`](../../Swift/false.md) (the default), all positions, distances, and velocities in the particle system are in the scene’s world coordinate system. If [`true`](../../Swift/true.md), the particle system runs in the local coordinate space of the node containing it.

Use this property to choose whether particles spawned by a moving emitter follow the system as it moves.

## See Also

### Controlling Particle Simulation
- [func reset()](./reset%28%29.md)
  Returns the particle system to its initial state.
- [var speedFactor: CGFloat](./speedfactor.md)
  A multiplier for the speed at which SceneKit runs the particle simulation. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/islocal)*