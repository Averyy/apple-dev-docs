# MTLCounterSamplingPoint.atStageBoundary

**Framework**: Metal  
**Kind**: case

Counter sampling is allowed at the start and end of a render pass’s vertex and fragment stages, and at the start and end of compute and blit passes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
case atStageBoundary
```

## Mentions

- [Sampling GPU data into counter sample buffers](sampling-gpu-data-into-counter-sample-buffers.md)

## See Also

- [MTLCounterSamplingPoint.atBlitBoundary](mtlcountersamplingpoint/atblitboundary.md)
  Counter sampling is allowed between blit commands in a blit pass.
- [MTLCounterSamplingPoint.atDispatchBoundary](mtlcountersamplingpoint/atdispatchboundary.md)
  Counter sampling is allowed between kernel dispatches in a compute pass.
- [MTLCounterSamplingPoint.atDrawBoundary](mtlcountersamplingpoint/atdrawboundary.md)
  Counter sampling is allowed between draw commands in a render pass.
- [MTLCounterSamplingPoint.atTileDispatchBoundary](mtlcountersamplingpoint/attiledispatchboundary.md)
  Counter sampling is allowed between tile dispatches in a render pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcountersamplingpoint/atstageboundary)*