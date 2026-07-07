# ComputeGraphRuntimeComponent

**Framework**: RealityKit  
**Kind**: struct

Manages the live GPU simulation for an entity’s `ComputeGraphComponent_v1`.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ComputeGraphRuntimeComponent
```

#### Overview

RealityKit creates the ComputeGraphRuntimeComponent automatically on the first frame that a ComputeGraphComponent becomes active. You do not need to add it manually.

## Topics

### Instance Properties
- [var simulation: ComputeGraphSimulation](computegraphruntimecomponent/simulation.md)
  The underlying compute graph simulation driving this entity.
### Instance Methods
- [func readOutput(ComputeNodeGraph.Port.Address) -> (any MTLBuffer)?](computegraphruntimecomponent/readoutput(_:).md)
  Returns the output buffer for the port at the given address.
- [func readOutputs(ComputeNodeGraph.NodeID) -> [any MTLBuffer]?](computegraphruntimecomponent/readoutputs(_:).md)
  Returns all output buffers for the given output node.

## Relationships

### Conforms To
- [Component](component.md)
- [TransientComponent](transientcomponent.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/computegraphruntimecomponent)*