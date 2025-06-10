# MTLCounterSamplingPoint

**Framework**: Metal  
**Kind**: enum

Options for different times when you can sample GPU counters.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum MTLCounterSamplingPoint
```

## Mentions

- [Sampling GPU Data into Counter Sample Buffers](sampling-gpu-data-into-counter-sample-buffers.md)

## Topics

### Reading Sampling Boundary Types
- [MTLCounterSamplingPoint.atBlitBoundary](mtlcountersamplingpoint/atblitboundary.md)
  Counter sampling is allowed between blit commands in a blit pass.
- [MTLCounterSamplingPoint.atDispatchBoundary](mtlcountersamplingpoint/atdispatchboundary.md)
  Counter sampling is allowed between kernel dispatches in a compute pass.
- [MTLCounterSamplingPoint.atDrawBoundary](mtlcountersamplingpoint/atdrawboundary.md)
  Counter sampling is allowed between draw commands in a render pass.
- [MTLCounterSamplingPoint.atStageBoundary](mtlcountersamplingpoint/atstageboundary.md)
  Counter sampling is allowed at the start and end of a render pass’s vertex and fragment stages, and at the start and end of compute and blit passes.
- [MTLCounterSamplingPoint.atTileDispatchBoundary](mtlcountersamplingpoint/attiledispatchboundary.md)
  Counter sampling is allowed between tile dispatches in a render pass.
### Initializers
- [init?(rawValue: UInt)](mtlcountersamplingpoint/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var counterSets: [any MTLCounterSet]?](mtldevice/countersets.md)
  The counter sets supported by the device object.
- [func supportsCounterSampling(MTLCounterSamplingPoint) -> Bool](mtldevice/supportscountersampling(_:).md)
  Returns a Boolean value that indicates whether you can read GPU counters at the specified command boundary.
- [func makeCounterSampleBuffer(descriptor: MTLCounterSampleBufferDescriptor) throws -> any MTLCounterSampleBuffer](mtldevice/makecountersamplebuffer(descriptor:).md)
  Creates a counter sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcountersamplingpoint)*