# supportsCounterSampling(_:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (BOOL) supportsCounterSampling:(MTLCounterSamplingPoint) samplingPoint;
```

## Mentions

- [Sampling GPU data into counter sample buffers](../sampling-gpu-data-into-counter-sample-buffers.md)

## Parameters

- `samplingPoint`: The command boundary to test.

## See Also

### Sampling a GPU device’s counters
- [var counterSets: [any MTLCounterSet]?](./countersets.md)
  The counter sets supported by the device object.
- [enum MTLCounterSamplingPoint](../mtlcountersamplingpoint.md)
  Options for different times when you can sample GPU counters.
- [func makeCounterSampleBuffer(descriptor: MTLCounterSampleBufferDescriptor) throws -> any MTLCounterSampleBuffer](./makecountersamplebuffer%28descriptor%29.md)
  Creates a counter sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/supportscountersampling(_:))*