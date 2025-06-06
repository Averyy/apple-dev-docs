# ParticleEmitterComponent.Timing.VariableDuration

**Framework**: RealityKit  
**Kind**: struct

Duration along with an optional variation used to define an amount of time.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct VariableDuration
```

## Topics

### Operators
- [static func == (ParticleEmitterComponent.Timing.VariableDuration, ParticleEmitterComponent.Timing.VariableDuration) -> Bool](particleemittercomponent/timing-swift.enum/variableduration/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(duration: TimeInterval, variation: TimeInterval?)](particleemittercomponent/timing-swift.enum/variableduration/init(duration:variation:).md)
- [init(from: any Decoder) throws](particleemittercomponent/timing-swift.enum/variableduration/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [let duration: TimeInterval](particleemittercomponent/timing-swift.enum/variableduration/duration.md)
  Base duration of time.
- [let variation: TimeInterval?](particleemittercomponent/timing-swift.enum/variableduration/variation.md)
  Defines a plus/minus range from which a value is randomly selected and used to offset duration.
### Instance Methods
- [func encode(to: any Encoder) throws](particleemittercomponent/timing-swift.enum/variableduration/encode(to:).md)
  Encodes this value into the given encoder.
### Default Implementations
- [Equatable Implementations](particleemittercomponent/timing-swift.enum/variableduration/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/particleemittercomponent/timing-swift.enum/variableduration)*