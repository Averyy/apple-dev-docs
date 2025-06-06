# systemSpawnedOnDying

**Framework**: SceneKit  
**Kind**: property

Another particle system to be added to the scene when a particle dies.

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
var systemSpawnedOnDying: SCNParticleSystem? { get set }
```

#### Discussion

When a particle reaches the end of its [`particleLifeSpan`](scnparticlesystem/particlelifespan.md) duration and is removed from the scene, SceneKit adds a copy of the specified particle system to the scene at the particle’s final location.

Use this property to simulate effects such as fireworks—one particle system simulates launching fireworks, and another particle system simulates each firework’s explosion.

The default value of this property is `nil`, specifying that no additional systems are added to the scene on particle death.

> ❗ **Important**:  Adding a new particle system to the scene for each particle death can drastically increase the total number of rendered particles. To maintain adequate rendering performance, set the [`loops`](scnparticlesystem/loops.md) property to [`false`](https://developer.apple.com/documentation/swift/false) for any particle system you assign to the [`systemSpawnedOnDying`](scnparticlesystem/systemspawnedondying.md) property.

 Adding a new particle system to the scene for each particle death can drastically increase the total number of rendered particles. To maintain adequate rendering performance, set the [`loops`](scnparticlesystem/loops.md) property to [`false`](https://developer.apple.com/documentation/swift/false) for any particle system you assign to the [`systemSpawnedOnDying`](scnparticlesystem/systemspawnedondying.md) property.

## See Also

- [var systemSpawnedOnCollision: SCNParticleSystem?](scnparticlesystem/systemspawnedoncollision.md)
  Another particle system to be added to the scene when a particle collides with scene geometry.
- [var systemSpawnedOnLiving: SCNParticleSystem?](scnparticlesystem/systemspawnedonliving.md)
  Another particle system to be added to the scene for each living particle in the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/systemspawnedondying)*