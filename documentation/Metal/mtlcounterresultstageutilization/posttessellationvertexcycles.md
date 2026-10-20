# postTessellationVertexCycles

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The number of cycles the GPU uses to run post-tessellation vertex shaders during a pass.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var postTessellationVertexCycles: UInt64
```

```c
uint64_t postTessellationVertexCycles;
```

## See Also

### Stage utilization values
- [var totalCycles: UInt64](./totalcycles.md)
  The total number of cycles the GPU uses to run a pass.
- [var vertexCycles: UInt64](./vertexcycles.md)
  The number of cycles the GPU uses to run vertex shaders during a pass.
- [var tessellationCycles: UInt64](./tessellationcycles.md)
  The number of cycles the GPU uses to run the tessellation stage during a pass.
- [var fragmentCycles: UInt64](./fragmentcycles.md)
  The number of cycles the GPU uses to run fragment shaders during a pass.
- [var renderTargetCycles: UInt64](./rendertargetcycles.md)
  The number of cycles the GPU uses to write data to render targets during a render pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcounterresultstageutilization/posttessellationvertexcycles)*