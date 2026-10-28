# systemSpawnedOnCollision

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

Another particle system to be added to the scene when a particle collides with scene geometry.

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
var systemSpawnedOnCollision: SCNParticleSystem? { get set }
```

```objc
@property (nonatomic, retain, nullable) SCNParticleSystem * systemSpawnedOnCollision;
```

## Discussion

When a particle collides with scene geometry, SceneKit adds a copy of the specified particle system to the scene at the location of the collision. (To define collision behavior, see the [`colliderNodes`](./collidernodes.md) property.)

Use this property to simulate effects such as rain—one particle system simulates falling raindrops, and another particle system simulates the splashes that occur where each raindrop strikes a surface.

The default value of this property is `nil`, specifying that no additional systems are added to the scene on particle collision.

> ❗ **Important**:  Adding a new particle system to the scene for each collision can drastically increase the total number of rendered particles. To maintain adequate rendering performance, set the [`loops`](./loops.md) property to [`false`](../../Swift/false.md) for any particle system you assign to the [`systemSpawnedOnCollision`](./systemspawnedoncollision.md) property.

## See Also

### Spawning Additional Particle Systems
- [var systemSpawnedOnDying: SCNParticleSystem?](./systemspawnedondying.md)
  Another particle system to be added to the scene when a particle dies.
- [var systemSpawnedOnLiving: SCNParticleSystem?](./systemspawnedonliving.md)
  Another particle system to be added to the scene for each living particle in the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/systemspawnedoncollision)*