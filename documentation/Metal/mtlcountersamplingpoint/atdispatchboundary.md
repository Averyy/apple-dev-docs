# MTLCounterSamplingPoint.atDispatchBoundary

**Framework**: Metal  
**Kind**: case

Counter sampling is allowed between kernel dispatches in a compute pass.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
case atDispatchBoundary
```

## Mentions

- [Sampling GPU data into counter sample buffers](sampling-gpu-data-into-counter-sample-buffers.md)

#### Discussion

When a Metal device instance supports this sampling boundary, you can call the [`sampleCounters(sampleBuffer:sampleIndex:barrier:)`](mtlcomputecommandencoder/samplecounters(samplebuffer:sampleindex:barrier:).md) method on an [`MTLComputeCommandEncoder`](mtlcomputecommandencoder.md) to sample the counters between individual dispatch commands.

## See Also

- [MTLCounterSamplingPoint.atBlitBoundary](mtlcountersamplingpoint/atblitboundary.md)
  Counter sampling is allowed between blit commands in a blit pass.
- [MTLCounterSamplingPoint.atDrawBoundary](mtlcountersamplingpoint/atdrawboundary.md)
  Counter sampling is allowed between draw commands in a render pass.
- [MTLCounterSamplingPoint.atStageBoundary](mtlcountersamplingpoint/atstageboundary.md)
  Counter sampling is allowed at the start and end of a render pass’s vertex and fragment stages, and at the start and end of compute and blit passes.
- [MTLCounterSamplingPoint.atTileDispatchBoundary](mtlcountersamplingpoint/attiledispatchboundary.md)
  Counter sampling is allowed between tile dispatches in a render pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcountersamplingpoint/atdispatchboundary)*