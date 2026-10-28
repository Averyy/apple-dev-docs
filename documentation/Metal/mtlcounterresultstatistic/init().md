# init()

**Framework**: Metal  
**Kind**: init  
**Role**: Initializer

Creates a default statistics result.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init()
```

## Discussion

Metal creates [`MTLCounterResultStatistic`](../mtlcounterresultstatistic.md) instances for you when you resolve the counter set’s data (see [Converting a GPU’s counter data into a readable format](../converting-a-gpus-counter-data-into-a-readable-format.md)). There’s no reason for you to manually create one in your app.

## See Also

### Swift support
- [init(tessellationInputPatches: UInt64, vertexInvocations: UInt64, postTessellationVertexInvocations: UInt64, clipperInvocations: UInt64, clipperPrimitivesOut: UInt64, fragmentInvocations: UInt64, fragmentsPassed: UInt64, computeKernelInvocations: UInt64)](./init%28tessellationinputpatches,vertexinvocations,posttessellationvertexinvocations,clipperinvocations,clipperprimitivesout,fragmentinvocations,fragmentspassed,computekernelinvocations%29.md)
  Creates a statistics result from statistic values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcounterresultstatistic/init())*