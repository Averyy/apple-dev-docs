# MTL4VisibilityOptions

**Framework**: Metal  
**Kind**: struct

Memory consistency options for synchronization commands.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct MTL4VisibilityOptions
```

## Topics

### Initializers
- [init(rawValue: Int)](mtl4visibilityoptions/init(rawvalue:).md)
### Type Properties
- [static var device: MTL4VisibilityOptions](mtl4visibilityoptions/device.md)
  Flushes caches to the GPU (device) memory coherence point.

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
- [struct MTLStages](mtlstages.md)
  Describes stages of GPU work.
- [protocol MTLFence](mtlfence.md)
  A memory fence to capture, track, and manage resource dependencies across command encoders.
- [struct MTLRenderStages](mtlrenderstages.md)
  The stages in a render pass that triggers a synchronization command.
- [struct MTLBarrierScope](mtlbarrierscope.md)
  Describes the types of resources that a barrier operates on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4visibilityoptions)*