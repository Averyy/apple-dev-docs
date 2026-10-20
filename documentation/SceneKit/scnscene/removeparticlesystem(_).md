# removeParticleSystem(_:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Removes a particle system attached to the scene.

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
func removeParticleSystem(_ system: SCNParticleSystem)
```

```objc
- (void) removeParticleSystem:(SCNParticleSystem *) system;
```

#### Discussion

This method has no effect if the `system` parameter does not reference a particle system directly attached to the scene.

## Parameters

- `system`: A particle system.

## See Also

### Working with Particle Systems in the Scene
- [func addParticleSystem(SCNParticleSystem, transform: SCNMatrix4)](./addparticlesystem%28_,transform%29.md)
  Attaches a particle system to the scene, using the specified transform.
- [var particleSystems: [SCNParticleSystem]?](./particlesystems.md)
  The particle systems attached to the scene.
- [func removeAllParticleSystems()](./removeallparticlesystems%28%29.md)
  Removes any particle systems directly attached to the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscene/removeparticlesystem(_:))*