# ParticleEmitterComponent.SpawnOccasion

**Framework**: RealityKit  
**Kind**: enum

Options for when the spawned effect starts, used by the spawnOccasion property.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
enum SpawnOccasion
```

## Topics

### Operators
- [static func == (ParticleEmitterComponent.SpawnOccasion, ParticleEmitterComponent.SpawnOccasion) -> Bool](particleemittercomponent/spawnoccasion-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [ParticleEmitterComponent.SpawnOccasion.onBirth](particleemittercomponent/spawnoccasion-swift.enum/onbirth.md)
  The spawned effect starts at the birth time of a main particle.
- [ParticleEmitterComponent.SpawnOccasion.onDeath](particleemittercomponent/spawnoccasion-swift.enum/ondeath.md)
  The spawned effect starts at the death of a main particle.
- [ParticleEmitterComponent.SpawnOccasion.onUpdate](particleemittercomponent/spawnoccasion-swift.enum/onupdate.md)
  The spawned effect starts on every tick of the engine.
### Initializers
- [init(from: any Decoder) throws](particleemittercomponent/spawnoccasion-swift.enum/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [var hashValue: Int](particleemittercomponent/spawnoccasion-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](particleemittercomponent/spawnoccasion-swift.enum/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](particleemittercomponent/spawnoccasion-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](particleemittercomponent/spawnoccasion-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/particleemittercomponent/spawnoccasion-swift.enum)*