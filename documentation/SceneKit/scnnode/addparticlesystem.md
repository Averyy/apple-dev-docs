# addParticleSystem(_:)

**Framework**: SceneKit  
**Kind**: method

Attaches a particle system to the node.

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
func addParticleSystem(_ system: SCNParticleSystem)
```

#### Discussion

When attached to a node, a particle system’s emitter location follows that node as it moves through the scene. To instead attach a particle system to a location in the scene’s world coordinate space, use the corresponding method on [`SCNScene`](scnscene.md).

For details on particle systems, see [`SCNParticleSystem`](scnparticlesystem.md).

## Parameters

- `system`: A particle system.

## See Also

- [var particleSystems: [SCNParticleSystem]?](scnnode/particlesystems.md)
  The particle systems attached to the node.
- [func removeParticleSystem(SCNParticleSystem)](scnnode/removeparticlesystem(_:).md)
  Removes a particle system attached to the node.
- [func removeAllParticleSystems()](scnnode/removeallparticlesystems.md)
  Removes any particle systems directly attached to the node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/addparticlesystem(_:))*