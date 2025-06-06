# MTLBarrierScope

**Framework**: Metal  
**Kind**: struct

Describes the types of resources that a barrier operates on.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
struct MTLBarrierScope
```

## Topics

### Initializers
- [init(rawValue: UInt)](mtlbarrierscope/init(rawvalue:).md)
### Type Properties
- [static var buffers: MTLBarrierScope](mtlbarrierscope/buffers.md)
  The barrier affects any buffer objects.
- [static var renderTargets: MTLBarrierScope](mtlbarrierscope/rendertargets.md)
  The barrier affects any render targets.
- [static var textures: MTLBarrierScope](mtlbarrierscope/textures.md)
  The barrier affects textures.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [Implementing a Multistage Image Filter Using Heaps and Fences](implementing-a-multistage-image-filter-using-heaps-and-fences.md)
  Use fences to synchronize access to resources allocated on a heap.
- [protocol MTLFence](mtlfence.md)
  A memory fence to capture, track, and manage resource dependencies across command encoders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlbarrierscope)*