# SCNParticleModifierStage.preCollision

**Framework**: SceneKit  
**Kind**: case

The stage before SceneKit simulates the results of collisions between particles and scene geometry.

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
case preCollision
```

#### Discussion

Insert a modifier block at this stage to alter the inputs to collision resolution. For example, if you modify the bounce factors of particles during this stage, SceneKit uses the modified factors to compute the bounce velocity of each particle.

## See Also

- [SCNParticleModifierStage.preDynamics](scnparticlemodifierstage/predynamics.md)
  The stage before SceneKit simulates the motion of particles.
- [SCNParticleModifierStage.postDynamics](scnparticlemodifierstage/postdynamics.md)
  The stage after SceneKit simulates the motion of particles.
- [SCNParticleModifierStage.postCollision](scnparticlemodifierstage/postcollision.md)
  The stage after SceneKit simulates the results of collisions between particles and scene geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlemodifierstage/precollision)*