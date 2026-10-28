# particleSystems

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The particle systems attached to the scene.

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
var particleSystems: [SCNParticleSystem]? { get }
```

```objc
@property (readonly, nullable) NSArray<SCNParticleSystem *> * particleSystems;
```

## Discussion

An array of [`SCNParticleSystem`](../scnparticlesystem.md) objects directly attached to the scene. This array does not include particle systems attached to nodes within the scene.

For details on particle systems, see [`SCNParticleSystem`](../scnparticlesystem.md).

## See Also

### Working with Particle Systems in the Scene
- [func addParticleSystem(SCNParticleSystem, transform: SCNMatrix4)](./addparticlesystem%28_,transform%29.md)
  Attaches a particle system to the scene, using the specified transform.
- [func removeParticleSystem(SCNParticleSystem)](./removeparticlesystem%28_%29.md)
  Removes a particle system attached to the scene.
- [func removeAllParticleSystems()](./removeallparticlesystems%28%29.md)
  Removes any particle systems directly attached to the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscene/particlesystems)*