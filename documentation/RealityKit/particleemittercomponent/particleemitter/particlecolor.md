# ParticleEmitterComponent.ParticleEmitter.ParticleColor

**Framework**: RealityKit  
**Kind**: enum  
**Role**: Enumeration

Options for specifying the behavior of the color of the particles.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
enum ParticleColor
```

## Topics

### Enumeration Cases
- [case constant(ParticleEmitterComponent.ParticleEmitter.ParticleColor.ColorValue)](./particlecolor/constant%28_%29.md)
  The particle will remain the given color throughout its lifetime.
- [case evolving(start: ParticleEmitterComponent.ParticleEmitter.ParticleColor.ColorValue, end: ParticleEmitterComponent.ParticleEmitter.ParticleColor.ColorValue)](./particlecolor/evolving%28start,end%29.md)
  The particle’s color will start at the `start` color and transition over its lifetime to the `end` color.
### Enumerations
- [ParticleEmitterComponent.ParticleEmitter.ParticleColor.ColorValue](./particlecolor/colorvalue.md)
  Options for specifying whether the particle color is a single color, or if the particle should take a random color in the given range.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/particleemittercomponent/particleemitter/particlecolor)*