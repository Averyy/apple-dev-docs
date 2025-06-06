# init(tessellationInputPatches:vertexInvocations:postTessellationVertexInvocations:clipperInvocations:clipperPrimitivesOut:fragmentInvocations:fragmentsPassed:computeKernelInvocations:)

**Framework**: Metal  
**Kind**: init

Creates a statistics result from statistic values.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init(tessellationInputPatches: UInt64, vertexInvocations: UInt64, postTessellationVertexInvocations: UInt64, clipperInvocations: UInt64, clipperPrimitivesOut: UInt64, fragmentInvocations: UInt64, fragmentsPassed: UInt64, computeKernelInvocations: UInt64)
```

#### Discussion

Metal creates [`MTLCounterResultStatistic`](mtlcounterresultstatistic.md) instances for you when you resolve the counter set’s data (see [`Converting a GPU’s Counter Data into a Readable Format`](converting-a-gpus-counter-data-into-a-readable-format.md)). There’s no reason for you to manually create one in your app.

## Parameters

- `tessellationInputPatches`: The number of tessellation patches the render pass sends to the tessellation stage.
- `vertexInvocations`: The number of times the render pass calls vertex shaders.
- `postTessellationVertexInvocations`: The number of vertices the tessellation stage creates.
- `clipperInvocations`: The number of primitives the clip stage consumes.
- `clipperPrimitivesOut`: The number of primitives the clip stage produces.
- `fragmentInvocations`: The number of times the render pass calls fragment shaders.
- `fragmentsPassed`: The number of fragments the render pass sends to the visibility and blend stages.
- `computeKernelInvocations`: The number of times the pass calls compute kernels.

## See Also

- [init()](mtlcounterresultstatistic/init.md)
  Creates a default statistics result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcounterresultstatistic/init(tessellationinputpatches:vertexinvocations:posttessellationvertexinvocations:clipperinvocations:clipperprimitivesout:fragmentinvocations:fragmentspassed:computekernelinvocations:))*