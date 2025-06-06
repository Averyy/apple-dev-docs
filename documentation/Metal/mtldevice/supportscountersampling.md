# supportsCounterSampling(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Returns a Boolean value that indicates whether you can read GPU counters at the specified command boundary.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func supportsCounterSampling(_ samplingPoint: MTLCounterSamplingPoint) -> Bool
```

## Mentions

- [Sampling GPU Data into Counter Sample Buffers](sampling-gpu-data-into-counter-sample-buffers.md)

## Parameters

- `samplingPoint`: The command boundary to test.

## See Also

- [var counterSets: [any MTLCounterSet]?](mtldevice/countersets.md)
  The counter sets supported by the device object.
- [enum MTLCounterSamplingPoint](mtlcountersamplingpoint.md)
  Options for different times when you can sample GPU counters.
- [func makeCounterSampleBuffer(descriptor: MTLCounterSampleBufferDescriptor) throws -> any MTLCounterSampleBuffer](mtldevice/makecountersamplebuffer(descriptor:).md)
  Creates a counter sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/supportscountersampling(_:))*