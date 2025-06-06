# SCNParticleModifierStage.postCollision

**Framework**: SceneKit  
**Kind**: case

The stage after SceneKit simulates the results of collisions between particles and scene geometry.

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
case postCollision
```

#### Discussion

Insert a modifier block at this stage to alter the output of collision resolution. For example, if you modify the velocities of particles during this stage, the modified velocities override the bounce velocity determined by SceneKit’s simulation.

## See Also

- [SCNParticleModifierStage.preDynamics](scnparticlemodifierstage/predynamics.md)
  The stage before SceneKit simulates the motion of particles.
- [SCNParticleModifierStage.postDynamics](scnparticlemodifierstage/postdynamics.md)
  The stage after SceneKit simulates the motion of particles.
- [SCNParticleModifierStage.preCollision](scnparticlemodifierstage/precollision.md)
  The stage before SceneKit simulates the results of collisions between particles and scene geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlemodifierstage/postcollision)*