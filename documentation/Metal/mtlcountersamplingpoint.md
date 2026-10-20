# MTLCounterSamplingPoint

**Framework**: Metal  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum MTLCounterSamplingPoint : NSUInteger;
```

## Mentions

- [Sampling GPU data into counter sample buffers](./sampling-gpu-data-into-counter-sample-buffers.md)

## Topics

### Reading sampling boundary types
- [MTLCounterSamplingPoint.atBlitBoundary](./mtlcountersamplingpoint/atblitboundary.md)
  Counter sampling is allowed between blit commands in a blit pass.
- [MTLCounterSamplingPoint.atDispatchBoundary](./mtlcountersamplingpoint/atdispatchboundary.md)
  Counter sampling is allowed between kernel dispatches in a compute pass.
- [MTLCounterSamplingPoint.atDrawBoundary](./mtlcountersamplingpoint/atdrawboundary.md)
  Counter sampling is allowed between draw commands in a render pass.
- [MTLCounterSamplingPoint.atStageBoundary](./mtlcountersamplingpoint/atstageboundary.md)
  Counter sampling is allowed at the start and end of a render pass’s vertex and fragment stages, and at the start and end of compute and blit passes.
- [MTLCounterSamplingPoint.atTileDispatchBoundary](./mtlcountersamplingpoint/attiledispatchboundary.md)
  Counter sampling is allowed between tile dispatches in a render pass.
### Initializers
- [init?(rawValue: UInt)](./mtlcountersamplingpoint/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Sampling a GPU device’s counters
- [var counterSets: [any MTLCounterSet]?](./mtldevice/countersets.md)
  The counter sets supported by the device object.
- [func supportsCounterSampling(MTLCounterSamplingPoint) -> Bool](./mtldevice/supportscountersampling%28_%29.md)
  Returns a Boolean value that indicates whether you can read GPU counters at the specified command boundary.
- [func makeCounterSampleBuffer(descriptor: MTLCounterSampleBufferDescriptor) throws -> any MTLCounterSampleBuffer](./mtldevice/makecountersamplebuffer%28descriptor%29.md)
  Creates a counter sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcountersamplingpoint)*