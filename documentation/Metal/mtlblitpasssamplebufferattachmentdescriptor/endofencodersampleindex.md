# endOfEncoderSampleIndex

**Framework**: Metal  
**Kind**: property

An index within a counter sample buffer that tells the GPU where to store counter data from the end of a blit pass.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var endOfEncoderSampleIndex: Int { get set }
```

## Mentions

- [Sampling GPU Data into Counter Sample Buffers](sampling-gpu-data-into-counter-sample-buffers.md)

#### Discussion

This property indicates where the GPU stores the counter data within an [`MTLCounterSampleBuffer`](mtlcountersamplebuffer.md) instance that it samples at the end of a blit pass.

You can tell the GPU to skip sampling at the end of the blit pass by assigning [`MTLCounterDontSample`](mtlcounterdontsample.md) to this property.

> ❗ **Important**:  For [`MTLDevice`](mtldevice.md) instances that don’t support [`MTLCounterSamplingPoint.atStageBoundary`](mtlcountersamplingpoint/atstageboundary.md) (see [`supportsCounterSampling(_:)`](mtldevice/supportscountersampling(_:).md)), set this property to [`MTLCounterDontSample`](mtlcounterdontsample.md).

## See Also

- [var sampleBuffer: (any MTLCounterSampleBuffer)?](mtlblitpasssamplebufferattachmentdescriptor/samplebuffer.md)
  A specialized memory buffer that the GPU uses to store its counter data during the blit pass.
- [var startOfEncoderSampleIndex: Int](mtlblitpasssamplebufferattachmentdescriptor/startofencodersampleindex.md)
  An index within a counter sample buffer that tells the GPU where to store counter data from the start of a blit pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitpasssamplebufferattachmentdescriptor/endofencodersampleindex)*