# sampleBuffer

**Framework**: Metal  
**Kind**: property

A specialized memory buffer that the GPU uses to store its counter data during a compute pass.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var sampleBuffer: (any MTLCounterSampleBuffer)? { get set }
```

## Mentions

- [Sampling GPU data into counter sample buffers](sampling-gpu-data-into-counter-sample-buffers.md)

#### Discussion

The property defaults to `nil`, which means the GPU doesn’t save any GPU counter information during the compute pass. For more information, see [`Creating a counter sample buffer to store a GPU’s counter data during a pass`](creating-a-counter-sample-buffer-to-store-a-gpus-counter-data-during-a-pass.md) and [`Sampling GPU data into counter sample buffers`](sampling-gpu-data-into-counter-sample-buffers.md).

## See Also

- [var startOfEncoderSampleIndex: Int](mtlcomputepasssamplebufferattachmentdescriptor/startofencodersampleindex.md)
  An index within a counter sample buffer that tells the GPU where to store counter data from the start of a compute pass.
- [var endOfEncoderSampleIndex: Int](mtlcomputepasssamplebufferattachmentdescriptor/endofencodersampleindex.md)
  An index within a counter sample buffer that tells the GPU where to store counter data from the end of a compute pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputepasssamplebufferattachmentdescriptor/samplebuffer)*