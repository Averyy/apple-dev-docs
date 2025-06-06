# ParticleEmitterComponent.ParticleEmitter.SortOrder

**Framework**: RealityKit  
**Kind**: enum

Options for the rendering order of particles, used by the sortingMode property.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
enum SortOrder
```

## Topics

### Operators
- [static func == (ParticleEmitterComponent.ParticleEmitter.SortOrder, ParticleEmitterComponent.ParticleEmitter.SortOrder) -> Bool](particleemittercomponent/particleemitter/sortorder-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [ParticleEmitterComponent.ParticleEmitter.SortOrder.decreasingAge](particleemittercomponent/particleemitter/sortorder-swift.enum/decreasingage.md)
  Particles emitted earlier are rendered before particles emitted more recently.
- [ParticleEmitterComponent.ParticleEmitter.SortOrder.decreasingDepth](particleemittercomponent/particleemitter/sortorder-swift.enum/decreasingdepth.md)
  Particles closer to camera are rendered first
- [ParticleEmitterComponent.ParticleEmitter.SortOrder.decreasingID](particleemittercomponent/particleemitter/sortorder-swift.enum/decreasingid.md)
  Particles with higher IDs are rendered first
- [ParticleEmitterComponent.ParticleEmitter.SortOrder.increasingAge](particleemittercomponent/particleemitter/sortorder-swift.enum/increasingage.md)
  Particles emitted more recently are rendered before particles emitted earlier.
- [ParticleEmitterComponent.ParticleEmitter.SortOrder.increasingDepth](particleemittercomponent/particleemitter/sortorder-swift.enum/increasingdepth.md)
  Particles further from camera are rendered first.
- [ParticleEmitterComponent.ParticleEmitter.SortOrder.increasingID](particleemittercomponent/particleemitter/sortorder-swift.enum/increasingid.md)
  Particles with lower IDs are rendered first
- [ParticleEmitterComponent.ParticleEmitter.SortOrder.unsorted](particleemittercomponent/particleemitter/sortorder-swift.enum/unsorted.md)
  Particles are not sorted; they may be rendered in any order.
### Initializers
- [init(from: any Decoder) throws](particleemittercomponent/particleemitter/sortorder-swift.enum/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [var hashValue: Int](particleemittercomponent/particleemitter/sortorder-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](particleemittercomponent/particleemitter/sortorder-swift.enum/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](particleemittercomponent/particleemitter/sortorder-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](particleemittercomponent/particleemitter/sortorder-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/particleemittercomponent/particleemitter/sortorder-swift.enum)*