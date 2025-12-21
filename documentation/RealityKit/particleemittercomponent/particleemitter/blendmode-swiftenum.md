# ParticleEmitterComponent.ParticleEmitter.BlendMode

**Framework**: RealityKit  
**Kind**: enum

Options for combining source and destination pixel colors when compositing particles during rendering, used by the blendMode property.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
enum BlendMode
```

## Topics

### Enumeration Cases
- [ParticleEmitterComponent.ParticleEmitter.BlendMode.additive](particleemittercomponent/particleemitter/blendmode-swift.enum/additive.md)
  The source and destination colors are added together.
- [ParticleEmitterComponent.ParticleEmitter.BlendMode.alpha](particleemittercomponent/particleemitter/blendmode-swift.enum/alpha.md)
  The source and destination colors are blended by multiplying the source alpha value.
- [ParticleEmitterComponent.ParticleEmitter.BlendMode.opaque](particleemittercomponent/particleemitter/blendmode-swift.enum/opaque.md)
  The particle fully occludes anything drawn before it.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/particleemittercomponent/particleemitter/blendmode-swift.enum)*