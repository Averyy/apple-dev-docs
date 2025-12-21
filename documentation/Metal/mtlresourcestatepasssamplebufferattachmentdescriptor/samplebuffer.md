# sampleBuffer

**Framework**: Metal  
**Kind**: property

A specialized memory buffer that the GPU uses to store its counter data during the resource state pass.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var sampleBuffer: (any MTLCounterSampleBuffer)? { get set }
```

## Mentions

- [Sampling GPU data into counter sample buffers](sampling-gpu-data-into-counter-sample-buffers.md)

#### Discussion

The property defaults to `nil`, which means the GPU doesn’t save any GPU counter information during the resource state pass. For more information, see [`Creating a counter sample buffer to store a GPU’s counter data during a pass`](creating-a-counter-sample-buffer-to-store-a-gpus-counter-data-during-a-pass.md) and [`Sampling GPU data into counter sample buffers`](sampling-gpu-data-into-counter-sample-buffers.md).

## See Also

- [var startOfEncoderSampleIndex: Int](mtlresourcestatepasssamplebufferattachmentdescriptor/startofencodersampleindex.md)
  The index the Metal device object should use to store GPU counters when starting the resource state pass.
- [var endOfEncoderSampleIndex: Int](mtlresourcestatepasssamplebufferattachmentdescriptor/endofencodersampleindex.md)
  The index the Metal device object should use to store GPU counters when ending the resource state pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresourcestatepasssamplebufferattachmentdescriptor/samplebuffer)*