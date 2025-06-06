# ParticleEmitterComponent.BirthLocation

**Framework**: RealityKit  
**Kind**: enum

Options for the location on the shape of where particles are born, used by the birthLocation property.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
enum BirthLocation
```

## Topics

### Operators
- [static func == (ParticleEmitterComponent.BirthLocation, ParticleEmitterComponent.BirthLocation) -> Bool](particleemittercomponent/birthlocation-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [ParticleEmitterComponent.BirthLocation.surface](particleemittercomponent/birthlocation-swift.enum/surface.md)
  Particles emit from the surface of the shape.
- [ParticleEmitterComponent.BirthLocation.vertices(count:)](particleemittercomponent/birthlocation-swift.enum/vertices(count:).md)
  Particles emit from the vertices of the shape. `count` is the number of vertices in each direction, the distribution depends on the EmitterShape chosen.
- [ParticleEmitterComponent.BirthLocation.volume](particleemittercomponent/birthlocation-swift.enum/volume.md)
  Particles emit from the internal volume of the shape.
### Initializers
- [init(from: any Decoder) throws](particleemittercomponent/birthlocation-swift.enum/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [var hashValue: Int](particleemittercomponent/birthlocation-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](particleemittercomponent/birthlocation-swift.enum/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](particleemittercomponent/birthlocation-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](particleemittercomponent/birthlocation-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/particleemittercomponent/birthlocation-swift.enum)*