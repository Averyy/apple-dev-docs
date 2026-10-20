# systemSpawnedOnDying

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

Another particle system to be added to the scene when a particle dies.

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
var systemSpawnedOnDying: SCNParticleSystem? { get set }
```

```objc
@property (nonatomic, retain, nullable) SCNParticleSystem * systemSpawnedOnDying;
```

#### Discussion

When a particle reaches the end of its [`particleLifeSpan`](./particlelifespan.md) duration and is removed from the scene, SceneKit adds a copy of the specified particle system to the scene at the particle’s final location.

Use this property to simulate effects such as fireworks—one particle system simulates launching fireworks, and another particle system simulates each firework’s explosion.

The default value of this property is `nil`, specifying that no additional systems are added to the scene on particle death.

> ❗ **Important**:  Adding a new particle system to the scene for each particle death can drastically increase the total number of rendered particles. To maintain adequate rendering performance, set the [`loops`](./loops.md) property to [`false`](../../Swift/false.md) for any particle system you assign to the [`systemSpawnedOnDying`](./systemspawnedondying.md) property.

## See Also

### Spawning Additional Particle Systems
- [var systemSpawnedOnCollision: SCNParticleSystem?](./systemspawnedoncollision.md)
  Another particle system to be added to the scene when a particle collides with scene geometry.
- [var systemSpawnedOnLiving: SCNParticleSystem?](./systemspawnedonliving.md)
  Another particle system to be added to the scene for each living particle in the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/systemspawnedondying)*