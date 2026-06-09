# ComputeNodeGraph.StateDefinition

**Framework**: ComputeGraph  
**Kind**: struct

A declaration of a named state value and where it lives in the simulation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

## Declaration

```swift
struct StateDefinition
```

#### Overview

State definitions are used by `ComputeNodeGraph/Node/Kind/loadState(definition:)` and `ComputeNodeGraph/Node/Kind/storeState(definition:)` nodes to read and write values at a particular scope.

## Topics

### Structures
- [ComputeNodeGraph.StateDefinition.Options](computenodegraph/statedefinition/options-swift.struct.md)
### Instance Properties
- [var options: ComputeNodeGraph.StateDefinition.Options](computenodegraph/statedefinition/options-swift.property.md)
  Whether this state is read, written, or both. See [`ComputeNodeGraph.StateDefinition.Options`](computenodegraph/statedefinition/options-swift.struct.md).
- [var scope: ComputeNodeGraph.Scope](computenodegraph/statedefinition/scope.md)
  The scope that owns this state. For example, `ComputeNodeGraph/Scope/element` stores a value per particle, while `ComputeNodeGraph/Scope/emitter` stores a single value used by the emission stage.
- [var type: ComputeNodeGraph.StateType](computenodegraph/statedefinition/type.md)
  The data type of the stored value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/statedefinition)*