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

### Render Pass Stages
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
### Swift Support
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
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [Synchronizing CPU and GPU Work](synchronizing-cpu-and-gpu-work.md)
  Avoid stalls between CPU and GPU work by using multiple instances of a resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderstages)*