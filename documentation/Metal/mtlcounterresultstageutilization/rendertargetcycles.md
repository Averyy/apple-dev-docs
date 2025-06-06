# renderTargetCycles

**Framework**: Metal  
**Kind**: property

The number of cycles the GPU uses to write data to render targets during a render pass.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var renderTargetCycles: UInt64
```

## See Also

- [var totalCycles: UInt64](mtlcounterresultstageutilization/totalcycles.md)
  The total number of cycles the GPU uses to run a pass.
- [var vertexCycles: UInt64](mtlcounterresultstageutilization/vertexcycles.md)
  The number of cycles the GPU uses to run vertex shaders during a pass.
- [var tessellationCycles: UInt64](mtlcounterresultstageutilization/tessellationcycles.md)
  The number of cycles the GPU uses to run the tessellation stage during a pass.
- [var postTessellationVertexCycles: UInt64](mtlcounterresultstageutilization/posttessellationvertexcycles.md)
  The number of cycles the GPU uses to run post-tessellation vertex shaders during a pass.
- [var fragmentCycles: UInt64](mtlcounterresultstageutilization/fragmentcycles.md)
  The number of cycles the GPU uses to run fragment shaders during a pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcounterresultstageutilization/rendertargetcycles)*