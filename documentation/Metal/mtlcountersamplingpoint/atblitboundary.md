# MTLCounterSamplingPoint.atBlitBoundary

**Framework**: Metal  
**Kind**: case

Counter sampling is allowed between blit commands in a blit pass.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
case atBlitBoundary
```

## Mentions

- [Sampling GPU Data into Counter Sample Buffers](sampling-gpu-data-into-counter-sample-buffers.md)

#### Discussion

When a Metal device object supports this sampling boundary, you can call the [`sampleCounters(sampleBuffer:sampleIndex:barrier:)`](mtlblitcommandencoder/samplecounters(samplebuffer:sampleindex:barrier:).md) method on a [`MTLBlitCommandEncoder`](mtlblitcommandencoder.md) to sample the counters between individual blit commands.

## See Also

- [MTLCounterSamplingPoint.atDispatchBoundary](mtlcountersamplingpoint/atdispatchboundary.md)
  Counter sampling is allowed between kernel dispatches in a compute pass.
- [MTLCounterSamplingPoint.atDrawBoundary](mtlcountersamplingpoint/atdrawboundary.md)
  Counter sampling is allowed between draw commands in a render pass.
- [MTLCounterSamplingPoint.atStageBoundary](mtlcountersamplingpoint/atstageboundary.md)
  Counter sampling is allowed at the start and end of a render pass’s vertex and fragment stages, and at the start and end of compute and blit passes.
- [MTLCounterSamplingPoint.atTileDispatchBoundary](mtlcountersamplingpoint/attiledispatchboundary.md)
  Counter sampling is allowed between tile dispatches in a render pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcountersamplingpoint/atblitboundary)*