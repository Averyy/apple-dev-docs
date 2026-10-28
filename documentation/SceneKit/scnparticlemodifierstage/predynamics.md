# SCNParticleModifierStage.preDynamics

**Framework**: SceneKit  
**Kind**: case  
**Role**: Case

The stage before SceneKit simulates the motion of particles.

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
case preDynamics
```

```c
SCNParticleModifierStagePreDynamics
```

## Discussion

Insert a modifier block at this stage to alter the inputs to the dynamics simulation. For example, if you modify the velocities of particles during this stage, SceneKit computes new positions for each particle based on its modified velocity.

## See Also

### Constants
- [SCNParticleModifierStage.postDynamics](./postdynamics.md)
  The stage after SceneKit simulates the motion of particles.
- [SCNParticleModifierStage.preCollision](./precollision.md)
  The stage before SceneKit simulates the results of collisions between particles and scene geometry.
- [SCNParticleModifierStage.postCollision](./postcollision.md)
  The stage after SceneKit simulates the results of collisions between particles and scene geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlemodifierstage/predynamics)*