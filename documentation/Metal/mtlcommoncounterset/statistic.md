# statistic

**Framework**: Metal  
**Kind**: property

The common name for the counter set that contains GPU workload statistics.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
static let statistic: MTLCommonCounterSet
```

## Mentions

- [Converting a GPU’s Counter Data into a Readable Format](converting-a-gpus-counter-data-into-a-readable-format.md)

#### Discussion

The statistics counter set contains the following counters:

- [`computeKernelInvocations`](mtlcommoncounter/computekernelinvocations.md)
- [`vertexInvocations`](mtlcommoncounter/vertexinvocations.md)
- [`fragmentInvocations`](mtlcommoncounter/fragmentinvocations.md)
- [`fragmentsPassed`](mtlcommoncounter/fragmentspassed.md)
- [`tessellationInputPatches`](mtlcommoncounter/tessellationinputpatches.md)
- [`postTessellationVertexInvocations`](mtlcommoncounter/posttessellationvertexinvocations.md)
- [`clipperInvocations`](mtlcommoncounter/clipperinvocations.md)
- [`clipperPrimitivesOut`](mtlcommoncounter/clipperprimitivesout.md)

Use this name to check whether a GPU device supports the corresponding counter set (see [`Confirming which Counters and Counter Sets a GPU Supports`](confirming-which-counters-and-counter-sets-a-gpu-supports.md)).

## See Also

- [static let timestamp: MTLCommonCounterSet](mtlcommoncounterset/timestamp.md)
  The common name for the counter set that contains the timestamp counter.
- [static let stageUtilization: MTLCommonCounterSet](mtlcommoncounterset/stageutilization.md)
  The common name for the counter set that contains hardware utilization measurements from various render stages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommoncounterset/statistic)*