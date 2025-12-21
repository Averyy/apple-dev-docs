# startOfEncoderSampleIndex

**Framework**: Metal  
**Kind**: property

The index the Metal device object should use to store GPU counters when starting the resource state pass.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var startOfEncoderSampleIndex: Int { get set }
```

## Mentions

- [Sampling GPU data into counter sample buffers](sampling-gpu-data-into-counter-sample-buffers.md)

#### Discussion

Specify [`MTLCounterDontSample`](mtlcounterdontsample.md) if you don’t want to sample GPU counters at the start of the resource state pass. Otherwise, specify an index within the sample buffer where you want the GPU to write the sample data.

On devices that don’t support [`MTLCounterSamplingPoint.atStageBoundary`](mtlcountersamplingpoint/atstageboundary.md) you need to set the value to [`MTLCounterDontSample`](mtlcounterdontsample.md).

## See Also

- [var sampleBuffer: (any MTLCounterSampleBuffer)?](mtlresourcestatepasssamplebufferattachmentdescriptor/samplebuffer.md)
  A specialized memory buffer that the GPU uses to store its counter data during the resource state pass.
- [var endOfEncoderSampleIndex: Int](mtlresourcestatepasssamplebufferattachmentdescriptor/endofencodersampleindex.md)
  The index the Metal device object should use to store GPU counters when ending the resource state pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresourcestatepasssamplebufferattachmentdescriptor/startofencodersampleindex)*