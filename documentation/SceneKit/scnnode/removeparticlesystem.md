# removeParticleSystem(_:)

**Framework**: SceneKit  
**Kind**: method

Removes a particle system attached to the node.

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

This method has no effect if the `system` parameter does not reference a particle system directly attached to the node.

## Parameters

- `system`: A particle system.

## See Also

- [func addParticleSystem(SCNParticleSystem)](scnnode/addparticlesystem(_:).md)
  Attaches a particle system to the node.
- [var particleSystems: [SCNParticleSystem]?](scnnode/particlesystems.md)
  The particle systems attached to the node.
- [func removeAllParticleSystems()](scnnode/removeallparticlesystems.md)
  Removes any particle systems directly attached to the node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/removeparticlesystem(_:))*