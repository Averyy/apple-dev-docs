# addParticleSystem(_:transform:)

**Framework**: SceneKit  
**Kind**: method

Attaches a particle system to the scene, using the specified transform.

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
func addParticleSystem(_ system: SCNParticleSystem, transform: SCNMatrix4)
```

#### Discussion

A particle system directly attached to a scene is not related to the coordinate space of any node in the scene. To attach a particle system whose emitter location follows the movement of a node within the scene, use the corresponding [`SCNNode`](scnnode.md) method.

For details on particle systems, see [`SCNParticleSystem`](scnparticlesystem.md).

## Parameters

- `system`: A particle system.
- `transform`: A transformation matrix that positions and orients the particle system relative to the world coordinate space of the scene.

## See Also

- [var particleSystems: [SCNParticleSystem]?](scnscene/particlesystems.md)
  The particle systems attached to the scene.
- [func removeParticleSystem(SCNParticleSystem)](scnscene/removeparticlesystem(_:).md)
  Removes a particle system attached to the scene.
- [func removeAllParticleSystems()](scnscene/removeallparticlesystems.md)
  Removes any particle systems directly attached to the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscene/addparticlesystem(_:transform:))*