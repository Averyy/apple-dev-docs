# particleSystem

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

Creates a new particle system.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```objc
+ (instancetype) particleSystem;
```

#### Return Value

A new particle system object with default values for all of its properties.

#### Discussion

A particle system with default values for all of its properties renders nothing when added to a scene.

To more easily build a new visual effect, use Xcode. Choose SceneKit Particle System in the New File window, then choose one of the preconfigured particle system templates for fire, clouds, and other common visual effects. You can then modify the template particle system to create an effect appropriate to your project. To load a particle system file created in Xcode, see the [`init(named:inDirectory:)`](./init%28named,indirectory%29.md) method.

## See Also

### Creating a Particle System
- [convenience init?(named: String, inDirectory: String?)](./init%28named,indirectory%29.md)
  Loads a particle system from a file in the app’s bundle resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/particlesystem)*