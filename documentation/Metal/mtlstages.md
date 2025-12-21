# MTLStages

**Framework**: Metal  
**Kind**: struct

The segments of command execution within the Metal pass types.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct MTLStages
```

## Mentions

- [Synchronizing passes with a fence](synchronizing-passes-with-a-fence.md)
- [Synchronizing passes with consumer barriers](synchronizing-passes-with-consumer-barriers.md)
- [Synchronizing passes with producer barriers](synchronizing-passes-with-producer-barriers.md)
- [Synchronizing stages within a pass](synchronizing-stages-within-a-pass.md)

#### Overview

Metal associates each command with one or more stages within a pass. Use these stage identifiers to synchronize command execution within a pass by selecting which stages wait for other stages to complete.

Metal 4 introduces the following unified command encoders that combine multiple stages into a single pass:

- [`MTL4RenderCommandEncoder`](mtl4rendercommandencoder.md) instances encode render passes that run vertex, fragment, object, mesh, and tile stages.
- [`MTL4ComputeCommandEncoder`](mtl4computecommandencoder.md) instances encode unified compute passes that run blit, dispatch, and acceleration structure stages.
- [`MTL4MachineLearningCommandEncoder`](mtl4machinelearningcommandencoder.md) instances encode passes that run machine learning stages.

Metal 3 provides separate command encoders for different types of work:

- [`MTLRenderCommandEncoder`](mtlrendercommandencoder.md) instances encode render passes that run vertex, fragment, object, mesh, and tile stages.
- [`MTLComputeCommandEncoder`](mtlcomputecommandencoder.md) instances encode compute passes that run dispatch stages.
- [`MTLBlitCommandEncoder`](mtlblitcommandencoder.md) instances encode blit passes that run blit stages, which initialize and copy data for resources, such as buffers and textures.
- [`MTLAccelerationStructureCommandEncoder`](mtlaccelerationstructurecommandencoder.md) instances encode passes that run acceleration structure stages, such as for ray tracing.

## Topics

### Render pass stages
- [static var vertex: MTLStages](mtlstages/vertex.md)
  Represents all vertex shader stage work in a render pass.
- [static var fragment: MTLStages](mtlstages/fragment.md)
  Represents all fragment shader stage work in a render pass.
- [static var tile: MTLStages](mtlstages/tile.md)
  Represents all tile shading stage work in a render pass.
- [static var object: MTLStages](mtlstages/object.md)
  Represents all object shader stage work in a render pass.
- [static var mesh: MTLStages](mtlstages/mesh.md)
  Represents all mesh shader stage work work in a render pass.
### Compute pass stages
- [static var dispatch: MTLStages](mtlstages/dispatch.md)
  Represents all compute dispatches in a compute pass.
- [static var blit: MTLStages](mtlstages/blit.md)
  Represents all blit operations in a pass.
- [static var accelerationStructure: MTLStages](mtlstages/accelerationstructure.md)
  Represents all acceleration structure operations.
- [static var machineLearning: MTLStages](mtlstages/machinelearning.md)
  Represents all machine learning network dispatch operations.
### Resource pass stages
- [static var resourceState: MTLStages](mtlstages/resourcestate.md)
  Represents all sparse and placement sparse resource mapping updates.
### Convenience values
- [static var all: MTLStages](mtlstages/all.md)
  Convenience mask representing all stages of GPU work.
### Swift support
- [init(rawValue: UInt)](mtlstages/init(rawvalue:).md)

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

- [Synchronizing stages within a pass](synchronizing-stages-within-a-pass.md)
  Block GPU stages in the a pass from running until other stages in the same pass finish.
- [Synchronizing passes with a fence](synchronizing-passes-with-a-fence.md)
  Block GPU stages in a pass until another pass unblocks it by signaling a fence.
- [Synchronizing passes with consumer barriers](synchronizing-passes-with-consumer-barriers.md)
  Block GPU stages in a pass, and all subsequent passes, from running until stages from earlier passes finish.
- [Synchronizing passes with producer barriers](synchronizing-passes-with-producer-barriers.md)
  Block GPU stages in subsequent passes from running until stages in a pass, and earlier passes, finish.
- [Synchronizing CPU and GPU work](synchronizing-cpu-and-gpu-work.md)
  Avoid stalls between CPU and GPU work by using multiple instances of a resource.
- [Implementing a multistage image filter using heaps and fences](implementing-a-multistage-image-filter-using-heaps-and-fences.md)
  Use fences to synchronize access to resources allocated on a heap.
- [protocol MTLFence](mtlfence.md)
  A synchronization mechanism that orders memory operations between GPU passes.
- [struct MTLRenderStages](mtlrenderstages.md)
  The stages in a render pass that triggers a synchronization command.
- [struct MTLBarrierScope](mtlbarrierscope.md)
  Describes the types of resources that a barrier operates on.
- [struct MTL4VisibilityOptions](mtl4visibilityoptions.md)
  Memory consistency options for synchronization commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstages)*