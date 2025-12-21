# systemSpawnedOnCollision

**Framework**: SceneKit  
**Kind**: property

Another particle system to be added to the scene when a particle collides with scene geometry.

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
var systemSpawnedOnCollision: SCNParticleSystem? { get set }
```

#### Discussion

When a particle collides with scene geometry, SceneKit adds a copy of the specified particle system to the scene at the location of the collision. (To define collision behavior, see the [`colliderNodes`](scnparticlesystem/collidernodes.md) property.)

Use this property to simulate effects such as rain—one particle system simulates falling raindrops, and another particle system simulates the splashes that occur where each raindrop strikes a surface.

The default value of this property is `nil`, specifying that no additional systems are added to the scene on particle collision.

> ❗ **Important**:  Adding a new particle system to the scene for each collision can drastically increase the total number of rendered particles. To maintain adequate rendering performance, set the [`loops`](scnparticlesystem/loops.md) property to [`false`](https://developer.apple.com/documentation/Swift/false) for any particle system you assign to the [`systemSpawnedOnCollision`](scnparticlesystem/systemspawnedoncollision.md) property.

## See Also

- [var systemSpawnedOnDying: SCNParticleSystem?](scnparticlesystem/systemspawnedondying.md)
  Another particle system to be added to the scene when a particle dies.
- [var systemSpawnedOnLiving: SCNParticleSystem?](scnparticlesystem/systemspawnedonliving.md)
  Another particle system to be added to the scene for each living particle in the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/systemspawnedoncollision)*