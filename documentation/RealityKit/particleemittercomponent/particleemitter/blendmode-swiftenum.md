# ParticleEmitterComponent.ParticleEmitter.BlendMode

**Framework**: RealityKit  
**Kind**: enum

Options for combining source and destination pixel colors when compositing particles during rendering, used by the blendMode property.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
enum BlendMode
```

## Topics

### Operators
- [static func == (ParticleEmitterComponent.ParticleEmitter.BlendMode, ParticleEmitterComponent.ParticleEmitter.BlendMode) -> Bool](particleemittercomponent/particleemitter/blendmode-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [ParticleEmitterComponent.ParticleEmitter.BlendMode.additive](particleemittercomponent/particleemitter/blendmode-swift.enum/additive.md)
  The source and destination colors are added together.
- [ParticleEmitterComponent.ParticleEmitter.BlendMode.alpha](particleemittercomponent/particleemitter/blendmode-swift.enum/alpha.md)
  The source and destination colors are blended by multiplying the source alpha value.
- [ParticleEmitterComponent.ParticleEmitter.BlendMode.opaque](particleemittercomponent/particleemitter/blendmode-swift.enum/opaque.md)
  The particle fully occludes anything drawn before it.
### Initializers
- [init(from: any Decoder) throws](particleemittercomponent/particleemitter/blendmode-swift.enum/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [var hashValue: Int](particleemittercomponent/particleemitter/blendmode-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](particleemittercomponent/particleemitter/blendmode-swift.enum/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](particleemittercomponent/particleemitter/blendmode-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](particleemittercomponent/particleemitter/blendmode-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/particleemittercomponent/particleemitter/blendmode-swift.enum)*