# MTLCounterResultStageUtilization

**Framework**: Metal  
**Kind**: struct

The data structure for storing the data you resolve from a stage-utilization counter set.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
struct MTLCounterResultStageUtilization
```

## Mentions

- [Converting a GPU’s counter data into a readable format](converting-a-gpus-counter-data-into-a-readable-format.md)

#### Overview

For steps that explain how to resolve data from a counter set, such as [`stageUtilization`](mtlcommoncounterset/stageutilization.md), see [`Converting a GPU’s counter data into a readable format`](converting-a-gpus-counter-data-into-a-readable-format.md).

## Topics

### Stage utilization values
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
- [var renderTargetCycles: UInt64](mtlcounterresultstageutilization/rendertargetcycles.md)
  The number of cycles the GPU uses to write data to render targets during a render pass.
### Swift support
- [init()](mtlcounterresultstageutilization/init.md)
  Creates a default stage-utilization result.
- [init(totalCycles: UInt64, vertexCycles: UInt64, tessellationCycles: UInt64, postTessellationVertexCycles: UInt64, fragmentCycles: UInt64, renderTargetCycles: UInt64)](mtlcounterresultstageutilization/init(totalcycles:vertexcycles:tessellationcycles:posttessellationvertexcycles:fragmentcycles:rendertargetcycles:).md)
  Creates a stage-utilization result from utilization values.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Converting a GPU’s counter data into a readable format](converting-a-gpus-counter-data-into-a-readable-format.md)
  Inspect and use the data within a GPU’s counter sample buffer by resolving it into a standard format.
- [struct MTLCounterResultTimestamp](mtlcounterresulttimestamp.md)
  The data structure for storing the data you resolve from a timestamp counter set.
- [struct MTLCounterResultStatistic](mtlcounterresultstatistic.md)
  The data structure for storing the data you resolve from a statistic counter set.
- [var MTLCounterErrorValue: UInt64](mtlcountererrorvalue.md)
  A sentinel value for an entry in a counter sample buffer that indicates the entry’s data is invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcounterresultstageutilization)*