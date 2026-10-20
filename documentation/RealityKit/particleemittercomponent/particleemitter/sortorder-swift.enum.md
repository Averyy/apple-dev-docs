# ParticleEmitterComponent.ParticleEmitter.SortOrder

**Framework**: RealityKit  
**Kind**: enum  
**Role**: Enumeration

Options for the rendering order of particles.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
enum SortOrder
```

## Topics

### Enumeration Cases
- [ParticleEmitterComponent.ParticleEmitter.SortOrder.decreasingAge](./sortorder-swift.enum/decreasingage.md)
  Particles emitted earlier are rendered before particles emitted more recently.
- [ParticleEmitterComponent.ParticleEmitter.SortOrder.decreasingDepth](./sortorder-swift.enum/decreasingdepth.md)
  Particles closer to camera are rendered first
- [ParticleEmitterComponent.ParticleEmitter.SortOrder.decreasingID](./sortorder-swift.enum/decreasingid.md)
  Particles with higher IDs are rendered first
- [ParticleEmitterComponent.ParticleEmitter.SortOrder.increasingAge](./sortorder-swift.enum/increasingage.md)
  Particles emitted more recently are rendered before particles emitted earlier.
- [ParticleEmitterComponent.ParticleEmitter.SortOrder.increasingDepth](./sortorder-swift.enum/increasingdepth.md)
  Particles further from camera are rendered first.
- [ParticleEmitterComponent.ParticleEmitter.SortOrder.increasingID](./sortorder-swift.enum/increasingid.md)
  Particles with lower IDs are rendered first
- [ParticleEmitterComponent.ParticleEmitter.SortOrder.unsorted](./sortorder-swift.enum/unsorted.md)
  Particles are not sorted; they may be rendered in any order.

## Relationships

### Conforms To
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/particleemittercomponent/particleemitter/sortorder-swift.enum)*