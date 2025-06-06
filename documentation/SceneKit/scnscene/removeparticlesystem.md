# removeParticleSystem(_:)

**Framework**: SceneKit  
**Kind**: method

Removes a particle system attached to the scene.

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
func removeParticleSystem(_ system: SCNParticleSystem)
```

#### Discussion

This method has no effect if the `system` parameter does not reference a particle system directly attached to the scene.

## Parameters

- `system`: A particle system.

## See Also

- [func addParticleSystem(SCNParticleSystem, transform: SCNMatrix4)](scnscene/addparticlesystem(_:transform:).md)
  Attaches a particle system to the scene, using the specified transform.
- [var particleSystems: [SCNParticleSystem]?](scnscene/particlesystems.md)
  The particle systems attached to the scene.
- [func removeAllParticleSystems()](scnscene/removeallparticlesystems.md)
  Removes any particle systems directly attached to the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscene/removeparticlesystem(_:))*