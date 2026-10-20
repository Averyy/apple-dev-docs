# systemSpawnedOnLiving

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

Another particle system to be added to the scene for each living particle in the system.

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
var systemSpawnedOnLiving: SCNParticleSystem? { get set }
```

```objc
@property (nonatomic, retain, nullable) SCNParticleSystem * systemSpawnedOnLiving;
```

#### Discussion

Each time SceneKit renders a frame, it adds an instance of the specified particle system to the scene at the location of each rendered particle.

Use this property to simulate continuous secondary effects on particles. For example, to create a fountain of sparklers, use one particle system as the fountain, and attach another system that simulates each sparkler.

The default value of this property is `nil`, specifying that no additional systems are added to the scene when rendering particles.

> ❗ **Important**:  This property adds one new particle system to the scene *for each rendered particle, on each rendered frame*, drastically increasing the total number of rendered particles. To avoid performance problems, plan your use of this property to limit the total number of particles in the scene. For example, attach a short-lived particle system to a system with few particles and whose [`loops`](./loops.md) property is set to [`false`](../../Swift/false.md).

## See Also

### Spawning Additional Particle Systems
- [var systemSpawnedOnCollision: SCNParticleSystem?](./systemspawnedoncollision.md)
  Another particle system to be added to the scene when a particle collides with scene geometry.
- [var systemSpawnedOnDying: SCNParticleSystem?](./systemspawnedondying.md)
  Another particle system to be added to the scene when a particle dies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/systemspawnedonliving)*