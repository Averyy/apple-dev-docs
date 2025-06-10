# MTLCommonCounter

**Framework**: Metal  
**Kind**: struct

The name of a specific counter that can appear in a GPU device’s counter sets.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
struct MTLCommonCounter
```

## Mentions

- [Confirming which Counters and Counter Sets a GPU Supports](confirming-which-counters-and-counter-sets-a-gpu-supports.md)

#### Overview

This type defines the constants that let a GPU device declare which counters it supports within a counter set. For more information, see [`Confirming which Counters and Counter Sets a GPU Supports`](confirming-which-counters-and-counter-sets-a-gpu-supports.md).

## Topics

### Common Counter Names
- [static let timestamp: MTLCommonCounter](mtlcommoncounter/timestamp.md)
  The common name for the counter that tracks the current time.
- [static let tessellationInputPatches: MTLCommonCounter](mtlcommoncounter/tessellationinputpatches.md)
  The common name for the counter that tracks the number of tessellation patches a render pass sends to the tessellation stage.
- [static let vertexInvocations: MTLCommonCounter](mtlcommoncounter/vertexinvocations.md)
  The common name for the counter that tracks the number of times a render pass calls any vertex shader.
- [static let postTessellationVertexInvocations: MTLCommonCounter](mtlcommoncounter/posttessellationvertexinvocations.md)
  The common name for the counter that tracks the number of vertices a render pass sends to a post-tessellation vertex shader.
- [static let clipperInvocations: MTLCommonCounter](mtlcommoncounter/clipperinvocations.md)
  The common name for the counter that tracks the number of primitives a render pass sends to the clip stage.
- [static let clipperPrimitivesOut: MTLCommonCounter](mtlcommoncounter/clipperprimitivesout.md)
  The common name for the counter that tracks the number of primitives the clip stage produces during a render pass.
- [static let fragmentInvocations: MTLCommonCounter](mtlcommoncounter/fragmentinvocations.md)
  The common name for the counter that tracks the number of times a render pass calls fragment shaders.
- [static let fragmentsPassed: MTLCommonCounter](mtlcommoncounter/fragmentspassed.md)
  The common name for the counter that tracks the number of fragments a render pass sends to the visibility and blend stages.
- [static let computeKernelInvocations: MTLCommonCounter](mtlcommoncounter/computekernelinvocations.md)
  The common name for the counter that tracks the number of times a pass invokes any compute kernel.
- [static let totalCycles: MTLCommonCounter](mtlcommoncounter/totalcycles.md)
  The common name for the counter that tracks the total number of cycles the GPU uses to run a pass.
- [static let vertexCycles: MTLCommonCounter](mtlcommoncounter/vertexcycles.md)
  The common name for the counter that tracks the number of cycles the GPU uses to run vertex shaders during a pass.
- [static let postTessellationVertexCycles: MTLCommonCounter](mtlcommoncounter/posttessellationvertexcycles.md)
  The common name for the counter that tracks the number of cycles the GPU uses to run post-tessellation vertex shaders during a pass.
- [static let fragmentCycles: MTLCommonCounter](mtlcommoncounter/fragmentcycles.md)
  The common name for the counter that tracks the number of cycles the GPU uses to run fragment shaders during a pass.
- [static let tessellationCycles: MTLCommonCounter](mtlcommoncounter/tessellationcycles.md)
  The common name for the counter that tracks the number of cycles the GPU uses to run the tessellation stage during a pass.
- [static let renderTargetWriteCycles: MTLCommonCounter](mtlcommoncounter/rendertargetwritecycles.md)
  The common name for the counter that tracks the number of cycles the GPU uses to write data to render targets during a render pass.
### Swift Support
- [init(rawValue: String)](mtlcommoncounter/init(rawvalue:).md)
  Creates a common counter name from a raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Confirming which Counters and Counter Sets a GPU Supports](confirming-which-counters-and-counter-sets-a-gpu-supports.md)
  Check whether a GPU produces the runtime performance data you want to sample.
- [protocol MTLCounterSet](mtlcounterset.md)
  A collection of individual counters a GPU device supports for a counter set.
- [struct MTLCommonCounterSet](mtlcommoncounterset.md)
  The name of a specific counter set that a GPU device can support.
- [protocol MTLCounter](mtlcounter.md)
  An individual counter a GPU device lists within one of its counter sets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommoncounter)*