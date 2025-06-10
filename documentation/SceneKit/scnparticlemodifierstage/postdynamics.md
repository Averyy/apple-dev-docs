# SCNParticleModifierStage.postDynamics

**Framework**: SceneKit  
**Kind**: case

The stage after SceneKit simulates the motion of particles.

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
case postDynamics
```

#### Discussion

Insert a modifier block at this stage to alter the output of the dynamics simulation. For example, if you modify the positions of particles during this stage, the modified positions override those determined by SceneKit’s simulation.

## See Also

- [SCNParticleModifierStage.preDynamics](scnparticlemodifierstage/predynamics.md)
  The stage before SceneKit simulates the motion of particles.
- [SCNParticleModifierStage.preCollision](scnparticlemodifierstage/precollision.md)
  The stage before SceneKit simulates the results of collisions between particles and scene geometry.
- [SCNParticleModifierStage.postCollision](scnparticlemodifierstage/postcollision.md)
  The stage after SceneKit simulates the results of collisions between particles and scene geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlemodifierstage/postdynamics)*