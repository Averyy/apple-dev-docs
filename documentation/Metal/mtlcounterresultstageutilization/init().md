# init()

**Framework**: Metal  
**Kind**: init  
**Role**: Initializer

Creates a default stage-utilization result.

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

#### Discussion

Metal creates [`MTLCounterResultStageUtilization`](../mtlcounterresultstageutilization.md) instances for you when you resolve the counter set’s data (see [Converting a GPU’s counter data into a readable format](../converting-a-gpus-counter-data-into-a-readable-format.md)). There’s no reason for you to manually create one in your app.

## See Also

### Swift support
- [init(totalCycles: UInt64, vertexCycles: UInt64, tessellationCycles: UInt64, postTessellationVertexCycles: UInt64, fragmentCycles: UInt64, renderTargetCycles: UInt64)](./init%28totalcycles,vertexcycles,tessellationcycles,posttessellationvertexcycles,fragmentcycles,rendertargetcycles%29.md)
  Creates a stage-utilization result from utilization values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcounterresultstageutilization/init())*