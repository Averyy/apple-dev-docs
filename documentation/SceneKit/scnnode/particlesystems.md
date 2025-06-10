# particleSystems

**Framework**: SceneKit  
**Kind**: property

The particle systems attached to the node.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var particleSystems: [SCNParticleSystem]? { get }
```

#### Discussion

An array of [`SCNParticleSystem`](scnparticlesystem.md) objects directly attached to the node. This array does not include particle systems attached to the node’s child nodes.

For details on particle systems, see [`SCNParticleSystem`](scnparticlesystem.md).

## See Also

- [func addParticleSystem(SCNParticleSystem)](scnnode/addparticlesystem(_:).md)
  Attaches a particle system to the node.
- [func removeParticleSystem(SCNParticleSystem)](scnnode/removeparticlesystem(_:).md)
  Removes a particle system attached to the node.
- [func removeAllParticleSystems()](scnnode/removeallparticlesystems.md)
  Removes any particle systems directly attached to the node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/particlesystems)*