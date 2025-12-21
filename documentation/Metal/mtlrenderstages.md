# MTLRenderStages

**Framework**: Metal  
**Kind**: struct

The stages in a render pass that triggers a synchronization command.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
struct MTLRenderStages
```

#### Overview

Render stage boundaries provide synchronization opportunities within a render pass for specific resources and resource types. For example, you can designate render stage a synchronization point for a memory barrier or a fence (see [`memoryBarrier(resources:after:before:)`](mtlrendercommandencoder/memorybarrier(resources:after:before:).md) and [`MTLFence`](mtlfence.md), respectively). This allows a GPU to overlap its execution of two adjacent stages, which can shorten its overall runtime for the render pass.

## Topics

### Render pass stages
- [static var object: MTLRenderStages](mtlrenderstages/object.md)
  The object rendering stage.
- [static var mesh: MTLRenderStages](mtlrenderstages/mesh.md)
  The mesh rendering stage.
- [static var vertex: MTLRenderStages](mtlrenderstages/vertex.md)
  The vertex rendering stage.
- [static var fragment: MTLRenderStages](mtlrenderstages/fragment.md)
  The fragment rendering stage.
- [static var tile: MTLRenderStages](mtlrenderstages/tile.md)
  The tile rendering stage.
### Swift support
- [init(rawValue: UInt)](mtlrenderstages/init(rawvalue:).md)
  Creates a render stage from a raw value.

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
- [struct MTLStages](mtlstages.md)
  The segments of command execution within the Metal pass types.
- [protocol MTLFence](mtlfence.md)
  A synchronization mechanism that orders memory operations between GPU passes.
- [struct MTLBarrierScope](mtlbarrierscope.md)
  Describes the types of resources that a barrier operates on.
- [struct MTL4VisibilityOptions](mtl4visibilityoptions.md)
  Memory consistency options for synchronization commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderstages)*