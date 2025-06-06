# ForceEffectComponent.SimulationState

**Framework**: RealityKit  
**Kind**: enum

The simulation runtime states.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
enum SimulationState
```

## Topics

### Operators
- [static func == (ForceEffectComponent.SimulationState, ForceEffectComponent.SimulationState) -> Bool](forceeffectcomponent/simulationstate-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [ForceEffectComponent.SimulationState.pause](forceeffectcomponent/simulationstate-swift.enum/pause.md)
  The simulation will pause.
- [ForceEffectComponent.SimulationState.resume](forceeffectcomponent/simulationstate-swift.enum/resume.md)
  The simulation will resume, if paused.
- [ForceEffectComponent.SimulationState.start](forceeffectcomponent/simulationstate-swift.enum/start.md)
  The simulation will start, and its time set to zero. The simulation will restart if already started.
### Instance Properties
- [var hashValue: Int](forceeffectcomponent/simulationstate-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](forceeffectcomponent/simulationstate-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](forceeffectcomponent/simulationstate-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/forceeffectcomponent/simulationstate-swift.enum)*