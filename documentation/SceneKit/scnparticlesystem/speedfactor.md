# speedFactor

**Framework**: SceneKit  
**Kind**: property

A multiplier for the speed at which SceneKit runs the particle simulation. Animatable.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var speedFactor: CGFloat { get set }
```

#### Discussion

Use this property to speed up or slow down the overall behavior of a particle system without changing the many individual properties (such as [`acceleration`](scnparticlesystem/acceleration.md), [`particleAngularVelocity`](scnparticlesystem/particleangularvelocity.md), and [`particleBounce`](scnparticlesystem/particlebounce.md)) that affect the motion of particles.

The default value is 1.0. Lower values slow down the effect; higher values make the effect run faster.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var isLocal: Bool](scnparticlesystem/islocal.md)
  A Boolean value that specifies whether the particle simulation runs in the local coordinate space of the node containing it.
- [func reset()](scnparticlesystem/reset.md)
  Returns the particle system to its initial state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/speedfactor)*