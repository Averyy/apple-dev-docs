# MTLCounterResultStatistic

**Framework**: Metal  
**Kind**: struct

The data structure for storing the data you resolve from a statistic counter set.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
struct MTLCounterResultStatistic
```

## Mentions

- [Converting a GPU’s Counter Data into a Readable Format](converting-a-gpus-counter-data-into-a-readable-format.md)

#### Overview

For steps that explain how to resolve data from a counter set, such as [`statistic`](mtlcommoncounterset/statistic.md), see [`Converting a GPU’s Counter Data into a Readable Format`](converting-a-gpus-counter-data-into-a-readable-format.md).

## Topics

### Statistics Values
- [var tessellationInputPatches: UInt64](mtlcounterresultstatistic/tessellationinputpatches.md)
  The number of tessellation patches a render pass sends to the tessellation stage.
- [var vertexInvocations: UInt64](mtlcounterresultstatistic/vertexinvocations.md)
  The number of times a render pass calls any vertex shader.
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
### Swift Support
- [init()](mtlcounterresultstatistic/init.md)
  Creates a default statistics result.
- [init(tessellationInputPatches: UInt64, vertexInvocations: UInt64, postTessellationVertexInvocations: UInt64, clipperInvocations: UInt64, clipperPrimitivesOut: UInt64, fragmentInvocations: UInt64, fragmentsPassed: UInt64, computeKernelInvocations: UInt64)](mtlcounterresultstatistic/init(tessellationinputpatches:vertexinvocations:posttessellationvertexinvocations:clipperinvocations:clipperprimitivesout:fragmentinvocations:fragmentspassed:computekernelinvocations:).md)
  Creates a statistics result from statistic values.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Converting a GPU’s Counter Data into a Readable Format](converting-a-gpus-counter-data-into-a-readable-format.md)
  Inspect and use the data within a GPU’s counter sample buffer by resolving it into a standard format.
- [struct MTLCounterResultTimestamp](mtlcounterresulttimestamp.md)
  The data structure for storing the data you resolve from a timestamp counter set.
- [struct MTLCounterResultStageUtilization](mtlcounterresultstageutilization.md)
  The data structure for storing the data you resolve from a stage-utilization counter set.
- [var MTLCounterErrorValue: UInt64](mtlcountererrorvalue.md)
  A sentinel value for an entry in a counter sample buffer that indicates the entry’s data is invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcounterresultstatistic)*