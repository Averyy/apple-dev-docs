# removeAllParticleSystems()

**Framework**: SceneKit  
**Kind**: method

Removes any particle systems directly attached to the scene.

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
func removeAllParticleSystems()
```

#### Discussion

Calling this method does not remove particle systems attached to nodes within the scene.

## See Also

- [func addParticleSystem(SCNParticleSystem, transform: SCNMatrix4)](scnscene/addparticlesystem(_:transform:).md)
  Attaches a particle system to the scene, using the specified transform.
- [var particleSystems: [SCNParticleSystem]?](scnscene/particlesystems.md)
  The particle systems attached to the scene.
- [func removeParticleSystem(SCNParticleSystem)](scnscene/removeparticlesystem(_:).md)
  Removes a particle system attached to the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscene/removeallparticlesystems())*