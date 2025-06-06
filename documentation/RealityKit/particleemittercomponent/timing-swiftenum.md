# ParticleEmitterComponent.Timing

**Framework**: RealityKit  
**Kind**: enum

Options for specifying the duration of the particle effects, used by the timing property.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
enum Timing
```

## Topics

### Structures
- [ParticleEmitterComponent.Timing.VariableDuration](particleemittercomponent/timing-swift.enum/variableduration.md)
  Duration along with an optional variation used to define an amount of time.
### Operators
- [static func == (ParticleEmitterComponent.Timing, ParticleEmitterComponent.Timing) -> Bool](particleemittercomponent/timing-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [case once(warmUp: TimeInterval?, emit: ParticleEmitterComponent.Timing.VariableDuration)](particleemittercomponent/timing-swift.enum/once(warmup:emit:).md)
  Emits for the given `emit` duration and then stops, `warmUp` determines how long the simulation should appear to have run before first appearing.
- [case repeating(warmUp: TimeInterval?, emit: ParticleEmitterComponent.Timing.VariableDuration, idle: ParticleEmitterComponent.Timing.VariableDuration?)](particleemittercomponent/timing-swift.enum/repeating(warmup:emit:idle:).md)
  Emits for the given `emit` duration, and waits `idle` seconds before looping, `warmUp` determines how long the simulation should appear to have run before first appearing.
### Initializers
- [init(from: any Decoder) throws](particleemittercomponent/timing-swift.enum/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Methods
- [func encode(to: any Encoder) throws](particleemittercomponent/timing-swift.enum/encode(to:).md)
  Encodes this value into the given encoder.
### Default Implementations
- [Equatable Implementations](particleemittercomponent/timing-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/particleemittercomponent/timing-swift.enum)*