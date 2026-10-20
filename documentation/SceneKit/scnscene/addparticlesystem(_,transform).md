# addParticleSystem(_:transform:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Attaches a particle system to the scene, using the specified transform.

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
func addParticleSystem(_ system: SCNParticleSystem, transform: SCNMatrix4)
```

```objc
- (void) addParticleSystem:(SCNParticleSystem *) system withTransform:(SCNMatrix4) transform;
```

#### Discussion

A particle system directly attached to a scene is not related to the coordinate space of any node in the scene. To attach a particle system whose emitter location follows the movement of a node within the scene, use the corresponding [`SCNNode`](../scnnode.md) method.

For details on particle systems, see [`SCNParticleSystem`](../scnparticlesystem.md).

## Parameters

- `system`: A particle system.
- `transform`: A transformation matrix that positions and orients the particle system relative to the world coordinate space of the scene.

## See Also

### Working with Particle Systems in the Scene
- [var particleSystems: [SCNParticleSystem]?](./particlesystems.md)
  The particle systems attached to the scene.
- [func removeParticleSystem(SCNParticleSystem)](./removeparticlesystem%28_%29.md)
  Removes a particle system attached to the scene.
- [func removeAllParticleSystems()](./removeallparticlesystems%28%29.md)
  Removes any particle systems directly attached to the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscene/addparticlesystem(_:transform:))*