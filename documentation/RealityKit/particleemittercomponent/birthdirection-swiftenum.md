# ParticleEmitterComponent.BirthDirection

**Framework**: RealityKit  
**Kind**: enum

Options for the initial direction of each emitted particle, used by the birthDirection property.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
enum BirthDirection
```

## Topics

### Operators
- [static func == (ParticleEmitterComponent.BirthDirection, ParticleEmitterComponent.BirthDirection) -> Bool](particleemittercomponent/birthdirection-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [ParticleEmitterComponent.BirthDirection.local](particleemittercomponent/birthdirection-swift.enum/local.md)
  Emit direction is relative to the orientation of the emitter entity’s transform.
- [ParticleEmitterComponent.BirthDirection.normal](particleemittercomponent/birthdirection-swift.enum/normal.md)
  The emitting direction for each particle is along the surface normal vector at the point where the particle is emitted.
- [ParticleEmitterComponent.BirthDirection.world](particleemittercomponent/birthdirection-swift.enum/world.md)
  Ignores the orientation from the emitter entity’s transform.
### Initializers
- [init(from: any Decoder) throws](particleemittercomponent/birthdirection-swift.enum/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [var hashValue: Int](particleemittercomponent/birthdirection-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](particleemittercomponent/birthdirection-swift.enum/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](particleemittercomponent/birthdirection-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](particleemittercomponent/birthdirection-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/particleemittercomponent/birthdirection-swift.enum)*