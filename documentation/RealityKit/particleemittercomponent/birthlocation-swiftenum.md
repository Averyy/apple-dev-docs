# ParticleEmitterComponent.BirthLocation

**Framework**: RealityKit  
**Kind**: enum

Options for the location on the shape of where particles are born, used by the birthLocation property.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
enum BirthLocation
```

## Topics

### Enumeration Cases
- [ParticleEmitterComponent.BirthLocation.surface](particleemittercomponent/birthlocation-swift.enum/surface.md)
  Particles emit from the surface of the shape.
- [ParticleEmitterComponent.BirthLocation.vertices(count:)](particleemittercomponent/birthlocation-swift.enum/vertices(count:).md)
  Particles emit from the vertices of the shape. `count` is the number of vertices in each direction, the distribution depends on the EmitterShape chosen.
- [ParticleEmitterComponent.BirthLocation.volume](particleemittercomponent/birthlocation-swift.enum/volume.md)
  Particles emit from the internal volume of the shape.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/particleemittercomponent/birthlocation-swift.enum)*