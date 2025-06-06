# computeKernelInvocations

**Framework**: Metal  
**Kind**: property

The common name for the counter that tracks the number of times a pass invokes any compute kernel.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
static let computeKernelInvocations: MTLCommonCounter
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommoncounter/computekernelinvocations)*