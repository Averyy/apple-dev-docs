# endOfFragmentSampleIndex

**Framework**: Metal  
**Kind**: property

The index the Metal device object should use to store GPU counters when ending the render pass’s fragment stage.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var endOfFragmentSampleIndex: Int { get set }
```

## Mentions

- [Sampling GPU Data into Counter Sample Buffers](sampling-gpu-data-into-counter-sample-buffers.md)
- [Creating a Counter Sample Buffer to Store a GPU’s Counter Data During a Pass](creating-a-counter-sample-buffer-to-store-a-gpus-counter-data-during-a-pass.md)

#### Discussion

Specify [`MTLCounterDontSample`](mtlcounterdontsample.md) if you don’t want to sample GPU counters at the end of the fragment stage. Otherwise, specify an index within the sample buffer where you want the GPU to write the sample data.

On devices that don’t support [`MTLCounterSamplingPoint.atStageBoundary`](mtlcountersamplingpoint/atstageboundary.md) you must set the value to [`MTLCounterDontSample`](mtlcounterdontsample.md).

## See Also

- [var sampleBuffer: (any MTLCounterSampleBuffer)?](mtlrenderpasssamplebufferattachmentdescriptor/samplebuffer.md)
  A specialized memory buffer that the GPU uses to store its counter data during the render pass.
- [var startOfVertexSampleIndex: Int](mtlrenderpasssamplebufferattachmentdescriptor/startofvertexsampleindex.md)
  The index the Metal device object should use to store GPU counters when starting the render pass’s vertex stage.
- [var endOfVertexSampleIndex: Int](mtlrenderpasssamplebufferattachmentdescriptor/endofvertexsampleindex.md)
  The index the Metal device object should use to store GPU counters when ending the render pass’s vertex stage.
- [var startOfFragmentSampleIndex: Int](mtlrenderpasssamplebufferattachmentdescriptor/startoffragmentsampleindex.md)
  The index the Metal device object should use to store GPU counters when starting the render pass’s fragment stage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpasssamplebufferattachmentdescriptor/endoffragmentsampleindex)*