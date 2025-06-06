# vertexInvocations

**Framework**: Metal  
**Kind**: property

The number of times a render pass calls any vertex shader.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var vertexInvocations: UInt64
```

## See Also

- [var tessellationInputPatches: UInt64](mtlcounterresultstatistic/tessellationinputpatches.md)
  The number of tessellation patches a render pass sends to the tessellation stage.
- [var postTessellationVertexInvocations: UInt64](mtlcounterresultstatistic/posttessellationvertexinvocations.md)
  The number of vertices a render pass sends to a post-tessellation vertex shader.
- [var clipperInvocations: UInt64](mtlcounterresultstatistic/clipperinvocations.md)
  The number of primitives a render pass sends to the clip stage.
- [var clipperPrimitivesOut: UInt64](mtlcounterresultstatistic/clipperprimitivesout.md)
  The number of primitives the clip stage produces during a render pass.
- [var fragmentInvocations: UInt64](mtlcounterresultstatistic/fragmentinvocations.md)
  The number of times a render pass calls fragment shaders.
- [var fragmentsPassed: UInt64](mtlcounterresultstatistic/fragmentspassed.md)
  The number of fragments a render pass sends to the visibility and blend stages because they pass the scissor, depth, and stencil tests.
- [var computeKernelInvocations: UInt64](mtlcounterresultstatistic/computekernelinvocations.md)
  The number of times a pass calls any compute kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcounterresultstatistic/vertexinvocations)*