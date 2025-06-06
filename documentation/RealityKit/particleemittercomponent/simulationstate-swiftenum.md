# ParticleEmitterComponent.SimulationState

**Framework**: RealityKit  
**Kind**: enum

Options for the particle simulation state, used by the `simulationState` property.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
enum SimulationState
```

## Topics

### Operators
- [static func == (ParticleEmitterComponent.SimulationState, ParticleEmitterComponent.SimulationState) -> Bool](particleemittercomponent/simulationstate-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [ParticleEmitterComponent.SimulationState.pause](particleemittercomponent/simulationstate-swift.enum/pause.md)
  Simulation will pause.
- [ParticleEmitterComponent.SimulationState.play](particleemittercomponent/simulationstate-swift.enum/play.md)
  Simulation will play.
- [ParticleEmitterComponent.SimulationState.stop](particleemittercomponent/simulationstate-swift.enum/stop.md)
  Simulation will stop and clear existing particles.
### Initializers
- [init(from: any Decoder) throws](particleemittercomponent/simulationstate-swift.enum/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [var hashValue: Int](particleemittercomponent/simulationstate-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](particleemittercomponent/simulationstate-swift.enum/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](particleemittercomponent/simulationstate-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](particleemittercomponent/simulationstate-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/particleemittercomponent/simulationstate-swift.enum)*