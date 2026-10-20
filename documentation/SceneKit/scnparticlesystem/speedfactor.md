# speedFactor

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A multiplier for the speed at which SceneKit runs the particle simulation. Animatable.

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
var speedFactor: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat speedFactor;
```

#### Discussion

Use this property to speed up or slow down the overall behavior of a particle system without changing the many individual properties (such as [`acceleration`](./acceleration.md), [`particleAngularVelocity`](./particleangularvelocity.md), and [`particleBounce`](./particlebounce.md)) that affect the motion of particles.

The default value is 1.0. Lower values slow down the effect; higher values make the effect run faster.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Controlling Particle Simulation
- [var isLocal: Bool](./islocal.md)
  A Boolean value that specifies whether the particle simulation runs in the local coordinate space of the node containing it.
- [func reset()](./reset%28%29.md)
  Returns the particle system to its initial state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/speedfactor)*