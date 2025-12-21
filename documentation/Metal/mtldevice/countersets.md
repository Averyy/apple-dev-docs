# counterSets

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The counter sets supported by the device object.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var counterSets: [any MTLCounterSet]? { get }
```

## Mentions

- [Confirming which counters and counter sets a GPU supports](confirming-which-counters-and-counter-sets-a-gpu-supports.md)

## See Also

- [func supportsCounterSampling(MTLCounterSamplingPoint) -> Bool](mtldevice/supportscountersampling(_:).md)
  Returns a Boolean value that indicates whether you can read GPU counters at the specified command boundary.
- [enum MTLCounterSamplingPoint](mtlcountersamplingpoint.md)
  Options for different times when you can sample GPU counters.
- [func makeCounterSampleBuffer(descriptor: MTLCounterSampleBufferDescriptor) throws -> any MTLCounterSampleBuffer](mtldevice/makecountersamplebuffer(descriptor:).md)
  Creates a counter sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/countersets)*