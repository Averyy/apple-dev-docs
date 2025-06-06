# ParticleEmitterComponent.ParticleEmitter.BillboardMode

**Framework**: RealityKit  
**Kind**: enum

Options for specifying the axis about which the particle will be oriented, used by the `billboardMode` property.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
enum BillboardMode
```

## Topics

### Operators
- [static func == (ParticleEmitterComponent.ParticleEmitter.BillboardMode, ParticleEmitterComponent.ParticleEmitter.BillboardMode) -> Bool](particleemittercomponent/particleemitter/billboardmode-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [ParticleEmitterComponent.ParticleEmitter.BillboardMode.billboard](particleemittercomponent/particleemitter/billboardmode-swift.enum/billboard.md)
  Each particle is oriented to face the camera.
- [ParticleEmitterComponent.ParticleEmitter.BillboardMode.billboardYAligned](particleemittercomponent/particleemitter/billboardmode-swift.enum/billboardyaligned.md)
  Each particle is oriented to face the camera but remains fixed about the y-axis
- [ParticleEmitterComponent.ParticleEmitter.BillboardMode.free(axis:variation:)](particleemittercomponent/particleemitter/billboardmode-swift.enum/free(axis:variation:).md)
  The axis about which the particle will be oriented is the given `axis`. The `variation` is a unit multiplier that determines how far from the given axis the particle is allowed to actually be oriented.
### Initializers
- [init(from: any Decoder) throws](particleemittercomponent/particleemitter/billboardmode-swift.enum/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [var hashValue: Int](particleemittercomponent/particleemitter/billboardmode-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](particleemittercomponent/particleemitter/billboardmode-swift.enum/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](particleemittercomponent/particleemitter/billboardmode-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](particleemittercomponent/particleemitter/billboardmode-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/particleemittercomponent/particleemitter/billboardmode-swift.enum)*