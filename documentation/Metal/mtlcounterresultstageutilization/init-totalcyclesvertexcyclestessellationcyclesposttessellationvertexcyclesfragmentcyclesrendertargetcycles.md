# init(totalCycles:vertexCycles:tessellationCycles:postTessellationVertexCycles:fragmentCycles:renderTargetCycles:)

**Framework**: Metal  
**Kind**: init

Creates a stage-utilization result from utilization values.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init(totalCycles: UInt64, vertexCycles: UInt64, tessellationCycles: UInt64, postTessellationVertexCycles: UInt64, fragmentCycles: UInt64, renderTargetCycles: UInt64)
```

#### Discussion

Metal creates [`MTLCounterResultStageUtilization`](mtlcounterresultstageutilization.md) instances for you when you resolve the counter set’s data (see [`Converting a GPU’s counter data into a readable format`](converting-a-gpus-counter-data-into-a-readable-format.md)). There’s no reason for you to manually create one in your app.

## Parameters

- `totalCycles`: The number of GPU cycles the entire render pass takes to run.
- `vertexCycles`: The number of GPU cycles the vertex shaders take to run.
- `tessellationCycles`: The number of GPU cycles the tessellating patches take to run.
- `postTessellationVertexCycles`: The number of GPU cycles the post-tessellation vertex shaders take to run.
- `fragmentCycles`: The number of GPU cycles the fragment shaders take to run.
- `renderTargetCycles`: The number of GPU cycles the pass takes writing data to render targets.

## See Also

- [init()](mtlcounterresultstageutilization/init.md)
  Creates a default stage-utilization result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcounterresultstageutilization/init(totalcycles:vertexcycles:tessellationcycles:posttessellationvertexcycles:fragmentcycles:rendertargetcycles:))*