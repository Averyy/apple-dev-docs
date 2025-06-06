# makeCounterSampleBuffer(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a counter sample buffer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func makeCounterSampleBuffer(descriptor: MTLCounterSampleBufferDescriptor) throws -> any MTLCounterSampleBuffer
```

## Mentions

- [Creating a Counter Sample Buffer to Store a GPU’s Counter Data During a Pass](creating-a-counter-sample-buffer-to-store-a-gpus-counter-data-during-a-pass.md)

#### Return Value

A new [`MTLCounterSampleBuffer`](mtlcountersamplebuffer.md) instance if the method completes successfully; otherwise Swift throws an error and Objective-C returns `nil`.

#### Discussion

The method may produce an error if the GPU driver has exhausted its underlying resources for counter sample buffers.

## Parameters

- `descriptor`: An   instance.

## See Also

- [var counterSets: [any MTLCounterSet]?](mtldevice/countersets.md)
  The counter sets supported by the device object.
- [func supportsCounterSampling(MTLCounterSamplingPoint) -> Bool](mtldevice/supportscountersampling(_:).md)
  Returns a Boolean value that indicates whether you can read GPU counters at the specified command boundary.
- [enum MTLCounterSamplingPoint](mtlcountersamplingpoint.md)
  Options for different times when you can sample GPU counters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makecountersamplebuffer(descriptor:))*