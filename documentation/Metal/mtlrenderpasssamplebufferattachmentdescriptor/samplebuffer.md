# sampleBuffer

**Framework**: Metal  
**Kind**: property

A specialized memory buffer that the GPU uses to store its counter data during the render pass.

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

- [Sampling GPU Data into Counter Sample Buffers](sampling-gpu-data-into-counter-sample-buffers.md)

#### Discussion

The property defaults to `nil`, which means the GPU doesn’t save any GPU counter information during the render pass. See [`Creating a Counter Sample Buffer to Store a GPU’s Counter Data During a Pass`](creating-a-counter-sample-buffer-to-store-a-gpus-counter-data-during-a-pass.md) and [`Sampling GPU Data into Counter Sample Buffers`](sampling-gpu-data-into-counter-sample-buffers.md) for more information.

## See Also

- [var startOfVertexSampleIndex: Int](mtlrenderpasssamplebufferattachmentdescriptor/startofvertexsampleindex.md)
  The index the Metal device object should use to store GPU counters when starting the render pass’s vertex stage.
- [var endOfVertexSampleIndex: Int](mtlrenderpasssamplebufferattachmentdescriptor/endofvertexsampleindex.md)
  The index the Metal device object should use to store GPU counters when ending the render pass’s vertex stage.
- [var startOfFragmentSampleIndex: Int](mtlrenderpasssamplebufferattachmentdescriptor/startoffragmentsampleindex.md)
  The index the Metal device object should use to store GPU counters when starting the render pass’s fragment stage.
- [var endOfFragmentSampleIndex: Int](mtlrenderpasssamplebufferattachmentdescriptor/endoffragmentsampleindex.md)
  The index the Metal device object should use to store GPU counters when ending the render pass’s fragment stage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpasssamplebufferattachmentdescriptor/samplebuffer)*