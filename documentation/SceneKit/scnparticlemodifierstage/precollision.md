# SCNParticleModifierStage.preCollision

**Framework**: SceneKit  
**Kind**: case  
**Role**: Case

The stage before SceneKit simulates the results of collisions between particles and scene geometry.

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
case preCollision
```

```c
SCNParticleModifierStagePreCollision
```

#### Discussion

Insert a modifier block at this stage to alter the inputs to collision resolution. For example, if you modify the bounce factors of particles during this stage, SceneKit uses the modified factors to compute the bounce velocity of each particle.

## See Also

### Constants
- [SCNParticleModifierStage.preDynamics](./predynamics.md)
  The stage before SceneKit simulates the motion of particles.
- [SCNParticleModifierStage.postDynamics](./postdynamics.md)
  The stage after SceneKit simulates the motion of particles.
- [SCNParticleModifierStage.postCollision](./postcollision.md)
  The stage after SceneKit simulates the results of collisions between particles and scene geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlemodifierstage/precollision)*