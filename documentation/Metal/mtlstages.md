# MTLStages

**Framework**: Metal  
**Kind**: struct

Describes stages of GPU work.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct MTLStages
```

## Mentions

- [Synchronizing resource accesses with subsequent passes with a producer-based queue barrier](synchronizing-resource-accesses-with-subsequent-passes-with-a-producer-based-queue-barrier.md)
- [Synchronizing resource accesses with earlier passes with a consumer-based queue barrier](synchronizing-resource-accesses-with-earlier-passes-with-a-consumer-based-queue-barrier.md)
- [Synchronizing resource accesses between multiple passes with a fence](synchronizing-resource-accesses-between-multiple-passes-with-a-fence.md)
- [Synchronizing resource accesses within a single pass with an intrapass barrier](synchronizing-resource-accesses-within-a-single-pass-with-an-intrapass-barrier.md)

#### Overview

All commands you encoder into command buffers relate to one or more shader stages, for example, a compute dispatch command from a compute command encoder relates to stage [`dispatch`](mtlstages/dispatch.md).

Use these stages to issue barriers between shader stages to ensure Metal correctly synchronizes GPU commands.

## Topics

### Initializers
- [init(rawValue: UInt)](mtlstages/init(rawvalue:).md)
### Type Properties
- [static var accelerationStructure: MTLStages](mtlstages/accelerationstructure.md)
  Represents all acceleration structure operations.
- [static var all: MTLStages](mtlstages/all.md)
  Convenience mask representing all stages of GPU work.
- [static var blit: MTLStages](mtlstages/blit.md)
  Represents all blit operations in a pass.
- [static var dispatch: MTLStages](mtlstages/dispatch.md)
  Represents all compute dispatches in a compute pass.
- [static var fragment: MTLStages](mtlstages/fragment.md)
  Represents all fragment shader stage work in a render pass.
- [static var machineLearning: MTLStages](mtlstages/machinelearning.md)
  Represents all machine learning network dispatch operations.
- [static var mesh: MTLStages](mtlstages/mesh.md)
  Represents all mesh shader stage work work in a render pass.
- [static var object: MTLStages](mtlstages/object.md)
  Represents all object shader stage work in a render pass.
- [static var resourceState: MTLStages](mtlstages/resourcestate.md)
  Represents all sparse and placement sparse resource mapping updates.
- [static var tile: MTLStages](mtlstages/tile.md)
  Represents all tile shading stage work in a render pass.
- [static var vertex: MTLStages](mtlstages/vertex.md)
  Represents all vertex shader stage work in a render pass.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [Synchronizing resource accesses within a single pass with an intrapass barrier](synchronizing-resource-accesses-within-a-single-pass-with-an-intrapass-barrier.md)
  Resolve resource access conflicts between stages within a single pass by adding an intrapass barrier.
- [Synchronizing resource accesses between multiple passes with a fence](synchronizing-resource-accesses-between-multiple-passes-with-a-fence.md)
  Resolve resource access conflicts between multiple passes within a single command queue by signaling a fence in one pass and waiting for it in another.
- [Synchronizing resource accesses with earlier passes with a consumer-based queue barrier](synchronizing-resource-accesses-with-earlier-passes-with-a-consumer-based-queue-barrier.md)
  Resolve resource access conflicts between multiple passes within a single command queue by creating a consumer-based intraqueue barrier.
- [Synchronizing resource accesses with subsequent passes with a producer-based queue barrier](synchronizing-resource-accesses-with-subsequent-passes-with-a-producer-based-queue-barrier.md)
  Resolve resource access conflicts between multiple passes within a single command queue by creating a producer-based intraqueue barrier.
- [Synchronizing CPU and GPU Work](synchronizing-cpu-and-gpu-work.md)
  Avoid stalls between CPU and GPU work by using multiple instances of a resource.
- [Implementing a Multistage Image Filter Using Heaps and Fences](implementing-a-multistage-image-filter-using-heaps-and-fences.md)
  Use fences to synchronize access to resources allocated on a heap.
- [protocol MTLFence](mtlfence.md)
  A memory fence to capture, track, and manage resource dependencies across command encoders.
- [struct MTLRenderStages](mtlrenderstages.md)
  The stages in a render pass that triggers a synchronization command.
- [struct MTLBarrierScope](mtlbarrierscope.md)
  Describes the types of resources that a barrier operates on.
- [struct MTL4VisibilityOptions](mtl4visibilityoptions.md)
  Memory consistency options for synchronization commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstages)*