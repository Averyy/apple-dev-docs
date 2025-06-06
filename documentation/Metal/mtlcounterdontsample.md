# MTLCounterDontSample

**Framework**: Metal  
**Kind**: var

A sentinel value that instructs an encoder to skip sampling a counter as the GPU runs the encoder’s pass.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var MTLCounterDontSample: Int { get }
```

## Mentions

- [Sampling GPU Data into Counter Sample Buffers](sampling-gpu-data-into-counter-sample-buffers.md)

#### Discussion

You can skip sampling at specific stages by assigning this sentinel value to the following properties instead of an offset to a counter sample buffer:

| Types | Properties |
| --- | --- |
| [`MTLRenderPassSampleBufferAttachmentDescriptor`](mtlrenderpasssamplebufferattachmentdescriptor.md) | [`startOfVertexSampleIndex`](mtlrenderpasssamplebufferattachmentdescriptor/startofvertexsampleindex.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`endOfVertexSampleIndex`](mtlrenderpasssamplebufferattachmentdescriptor/endofvertexsampleindex.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`startOfFragmentSampleIndex`](mtlrenderpasssamplebufferattachmentdescriptor/startoffragmentsampleindex.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`endOfFragmentSampleIndex`](mtlrenderpasssamplebufferattachmentdescriptor/endoffragmentsampleindex.md) |
| [`MTLComputePassSampleBufferAttachmentDescriptor`](mtlcomputepasssamplebufferattachmentdescriptor.md) | [`startOfEncoderSampleIndex`](mtlcomputepasssamplebufferattachmentdescriptor/startofencodersampleindex.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`endOfEncoderSampleIndex`](mtlcomputepasssamplebufferattachmentdescriptor/endofencodersampleindex.md) |
| [`MTLBlitPassSampleBufferAttachmentDescriptor`](mtlblitpasssamplebufferattachmentdescriptor.md) | [`startOfEncoderSampleIndex`](mtlblitpasssamplebufferattachmentdescriptor/startofencodersampleindex.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`endOfEncoderSampleIndex`](mtlblitpasssamplebufferattachmentdescriptor/endofencodersampleindex.md) |
| [`MTLResourceStatePassSampleBufferAttachmentDescriptor`](mtlresourcestatepasssamplebufferattachmentdescriptor.md) | [`startOfEncoderSampleIndex`](mtlresourcestatepasssamplebufferattachmentdescriptor/startofencodersampleindex.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`endOfEncoderSampleIndex`](mtlresourcestatepasssamplebufferattachmentdescriptor/endofencodersampleindex.md) |
| [`MTLAccelerationStructurePassSampleBufferAttachmentDescriptor`](mtlaccelerationstructurepasssamplebufferattachmentdescriptor.md) | [`startOfEncoderSampleIndex`](mtlaccelerationstructurepasssamplebufferattachmentdescriptor/startofencodersampleindex.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`endOfEncoderSampleIndex`](mtlaccelerationstructurepasssamplebufferattachmentdescriptor/endofencodersampleindex.md) |

## See Also

- [Creating a Counter Sample Buffer to Store a GPU’s Counter Data During a Pass](creating-a-counter-sample-buffer-to-store-a-gpus-counter-data-during-a-pass.md)
  Make a buffer that provides a place for a GPU to save its runtime performance metrics as it runs a pass.
- [class MTLCounterSampleBufferDescriptor](mtlcountersamplebufferdescriptor.md)
  A group of properties that configures the counter sample buffers you create with it.
- [protocol MTLCounterSampleBuffer](mtlcountersamplebuffer.md)
  A specialized memory buffer that stores a GPU’s counter set data.
- [Sampling GPU Data into Counter Sample Buffers](sampling-gpu-data-into-counter-sample-buffers.md)
  Retrieve a GPU’s counter data at a time the GPU supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcounterdontsample)*