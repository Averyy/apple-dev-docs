# particleSystems

**Framework**: SceneKit  
**Kind**: property

The particle systems attached to the scene.

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
var particleSystems: [SCNParticleSystem]? { get }
```

#### Discussion

An array of [`SCNParticleSystem`](scnparticlesystem.md) objects directly attached to the scene. This array does not include particle systems attached to nodes within the scene.

For details on particle systems, see [`SCNParticleSystem`](scnparticlesystem.md).

## See Also

- [func addParticleSystem(SCNParticleSystem, transform: SCNMatrix4)](scnscene/addparticlesystem(_:transform:).md)
  Attaches a particle system to the scene, using the specified transform.
- [func removeParticleSystem(SCNParticleSystem)](scnscene/removeparticlesystem(_:).md)
  Removes a particle system attached to the scene.
- [func removeAllParticleSystems()](scnscene/removeallparticlesystems.md)
  Removes any particle systems directly attached to the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscene/particlesystems)*