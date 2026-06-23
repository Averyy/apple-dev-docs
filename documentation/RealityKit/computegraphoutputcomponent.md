# ComputeGraphOutputComponent

**Framework**: RealityKit  
**Kind**: struct

A transient component that identifies the compute graph output associated with an entity.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ComputeGraphOutputComponent
```

#### Overview

The system attaches this component to child entities that represent individual graph outputs. Use `outputID` to correlate the entity with a specific output inside the owning entity’s running simulation.

## Topics

### Instance Properties
- [var outputID: ComputeNodeGraph.NodeID](computegraphoutputcomponent/outputid.md)
  The identifier of the output node in the compute graph that this entity represents.

## Relationships

### Conforms To
- [Component](component.md)
- [TransientComponent](transientcomponent.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/computegraphoutputcomponent)*