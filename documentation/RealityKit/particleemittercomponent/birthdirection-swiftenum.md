# ParticleEmitterComponent.BirthDirection

**Framework**: RealityKit  
**Kind**: enum

Options for the initial direction of each emitted particle, used by the birthDirection property.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
enum BirthDirection
```

## Topics

### Enumeration Cases
- [ParticleEmitterComponent.BirthDirection.local](particleemittercomponent/birthdirection-swift.enum/local.md)
  Emit direction is relative to the orientation of the emitter entity’s transform.
- [ParticleEmitterComponent.BirthDirection.normal](particleemittercomponent/birthdirection-swift.enum/normal.md)
  The emitting direction for each particle is along the surface normal vector at the point where the particle is emitted.
- [ParticleEmitterComponent.BirthDirection.world](particleemittercomponent/birthdirection-swift.enum/world.md)
  Ignores the orientation from the emitter entity’s transform.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/particleemittercomponent/birthdirection-swift.enum)*