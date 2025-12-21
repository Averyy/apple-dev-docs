# Sampling GPU data into counter sample buffers

**Framework**: Metal

Retrieve a GPU’s counter data at a time the GPU supports.

#### Overview

You can sample a GPU device’s performance counter data at different times, including:

- At pipeline stage boundaries
- Between different Metal commands

Typically, a GPU supports one of these boundary types. For example, Apple silicon supports sampling at the stage boundary because it processes fragments after processing every primitive for a render pass. However, a typical immediate-mode GPU supports sampling between commands.

Before you can sample a GPU counter, implement the following prerequisite steps:

1. Identify which counters you can sample from an [`MTLDevice`](mtldevice.md) instance (see [`Confirming which counters and counter sets a GPU supports`](confirming-which-counters-and-counter-sets-a-gpu-supports.md)).
2. Make an [`MTLCounterSampleBuffer`](mtlcountersamplebuffer.md) instance to store the counter’s data (see [`Creating a counter sample buffer to store a GPU’s counter data during a pass`](creating-a-counter-sample-buffer-to-store-a-gpus-counter-data-during-a-pass.md)).

The sections below explain how to identify when you can sample a GPU’s counters, and how to encode commands to retrieve their data.

Each GPU vendor defines its own private data format for its counter sample buffers, which means your app can’t read the contents of each buffer directly. Instead, your app can transform the data from the vendor’s internal format to the standard Metal formats by  each sample buffer. See [`Converting a GPU’s counter data into a readable format`](converting-a-gpus-counter-data-into-a-readable-format.md) for the next steps that resolve the data within a counter sample buffer.

##### Check Which Boundaries a Gpu Supports

You can inspect a GPU device instance to see whether it supports a specific sample boundary by calling its [`supportsCounterSampling(_:)`](mtldevice/supportscountersampling(_:).md) method with each [`MTLCounterSamplingPoint`](mtlcountersamplingpoint.md) case.

This method checks for multiple sample boundaries and returns those the GPU supports in an array.

##### Sample Counters at Stage Boundaries

For a GPU device that can sample counters at stage boundaries ( [`MTLCounterSamplingPoint.atStageBoundary`](mtlcountersamplingpoint/atstageboundary.md)), you can sample its counters between the stages of a pass. When the GPU starts or finishes a stage, it samples the counters and copies the results into a counter sample buffer.

> **Note**:  By default, a pass doesn’t sample any GPU counters.

You tell the GPU which counters to sample by configuring a pass descriptor’s [`sampleBufferAttachments`](mtlcomputepassdescriptor/samplebufferattachments.md) property. For example, you can sample the timestamp counters before and after the vertex and fragment stages by configuring an [`MTLRenderPassDescriptor`](mtlrenderpassdescriptor.md) instance’s [`sampleBufferAttachments`](mtlrenderpassdescriptor/samplebufferattachments.md) property.

Each index value tells the GPU where to put a specific counter value within a counter sample buffer. You can skip specific counters by setting an index to [`MTLCounterDontSample`](mtlcounterdontsample.md). For example, you can alter the code example above so that the GPU only samples before and after a fragment stage.

```swift
    ...
    sampleAttachment.sampleBuffer = self.counterSampleBuffer;
    sampleAttachment.startOfVertexSampleIndex = MTLCounterDontSample;
    sampleAttachment.endOfVertexSampleIndex = MTLCounterDontSample;
    sampleAttachment.startOfFragmentSampleIndex = 2;
    sampleAttachment.endOfFragmentSampleIndex = 3;
}
```

This example still stores the fragment counter data in the third and fourth positions within the counter sample buffer (at indexes 2 and 3, respectively). However, it doesn’t sample the vertex stage timestamps, which leaves that part of the counter sample buffer unaltered.

Each type of pass has different boundary types and corresponding properties in their descriptor types.

| Pass descriptor type | Attachment type | Attachment descriptor properties |
| --- | --- | --- |
| [`MTLRenderPassDescriptor`](mtlrenderpassdescriptor.md) | [`MTLRenderPassSampleBufferAttachmentDescriptor`](mtlrenderpasssamplebufferattachmentdescriptor.md) | [`sampleBuffer`](mtlrenderpasssamplebufferattachmentdescriptor/samplebuffer.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`startOfVertexSampleIndex`](mtlrenderpasssamplebufferattachmentdescriptor/startofvertexsampleindex.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`endOfVertexSampleIndex`](mtlrenderpasssamplebufferattachmentdescriptor/endofvertexsampleindex.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`startOfFragmentSampleIndex`](mtlrenderpasssamplebufferattachmentdescriptor/startoffragmentsampleindex.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`endOfFragmentSampleIndex`](mtlrenderpasssamplebufferattachmentdescriptor/endoffragmentsampleindex.md) |
| [`MTLAccelerationStructurePassDescriptor`](mtlaccelerationstructurepassdescriptor.md) | [`MTLAccelerationStructurePassSampleBufferAttachmentDescriptor`](mtlaccelerationstructurepasssamplebufferattachmentdescriptor.md) | [`sampleBuffer`](mtlaccelerationstructurepasssamplebufferattachmentdescriptor/samplebuffer.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`startOfEncoderSampleIndex`](mtlaccelerationstructurepasssamplebufferattachmentdescriptor/startofencodersampleindex.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`endOfEncoderSampleIndex`](mtlaccelerationstructurepasssamplebufferattachmentdescriptor/endofencodersampleindex.md) |
| [`MTLComputePassDescriptor`](mtlcomputepassdescriptor.md) | [`MTLComputePassSampleBufferAttachmentDescriptor`](mtlcomputepasssamplebufferattachmentdescriptor.md) | [`sampleBuffer`](mtlcomputepasssamplebufferattachmentdescriptor/samplebuffer.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`startOfEncoderSampleIndex`](mtlcomputepasssamplebufferattachmentdescriptor/startofencodersampleindex.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`endOfEncoderSampleIndex`](mtlcomputepasssamplebufferattachmentdescriptor/endofencodersampleindex.md) |
| [`MTLBlitPassDescriptor`](mtlblitpassdescriptor.md) | [`MTLBlitPassSampleBufferAttachmentDescriptor`](mtlblitpasssamplebufferattachmentdescriptor.md) | [`sampleBuffer`](mtlblitpasssamplebufferattachmentdescriptor/samplebuffer.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`startOfEncoderSampleIndex`](mtlblitpasssamplebufferattachmentdescriptor/startofencodersampleindex.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`endOfEncoderSampleIndex`](mtlblitpasssamplebufferattachmentdescriptor/endofencodersampleindex.md) |
| [`MTLResourceStatePassDescriptor`](mtlresourcestatepassdescriptor.md) | [`MTLResourceStatePassSampleBufferAttachmentDescriptor`](mtlresourcestatepasssamplebufferattachmentdescriptor.md) | [`sampleBuffer`](mtlresourcestatepasssamplebufferattachmentdescriptor/samplebuffer.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`startOfEncoderSampleIndex`](mtlresourcestatepasssamplebufferattachmentdescriptor/startofencodersampleindex.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`endOfEncoderSampleIndex`](mtlresourcestatepasssamplebufferattachmentdescriptor/endofencodersampleindex.md) |

##### Sample Counters at Command Boundaries

You can encode specific commands to sample a counter’s data during a pass for a GPU that supports any of the following boundaries:

- [`MTLCounterSamplingPoint.atDrawBoundary`](mtlcountersamplingpoint/atdrawboundary.md)
- [`MTLCounterSamplingPoint.atDispatchBoundary`](mtlcountersamplingpoint/atdispatchboundary.md)
- [`MTLCounterSamplingPoint.atBlitBoundary`](mtlcountersamplingpoint/atblitboundary.md)
- [`MTLCounterSamplingPoint.atTileDispatchBoundary`](mtlcountersamplingpoint/attiledispatchboundary.md)

You do this by calling an encoder’s [`sampleCounters(sampleBuffer:sampleIndex:barrier:)`](mtlrendercommandencoder/samplecounters(samplebuffer:sampleindex:barrier:).md) method.

The code example above encodes a sample command between two draw commands. When the GPU reaches the sample command, it samples the counters and copies the results into a counter sample buffer.

Each pass encoder type has its own version of the method.

| Pass encoder type | Sample method |
| --- | --- |
| [`MTLRenderCommandEncoder`](mtlrendercommandencoder.md) | [`sampleCounters(sampleBuffer:sampleIndex:barrier:)`](mtlrendercommandencoder/samplecounters(samplebuffer:sampleindex:barrier:).md) |
| [`MTLAccelerationStructureCommandEncoder`](mtlaccelerationstructurecommandencoder.md) | [`sampleCounters(sampleBuffer:sampleIndex:barrier:)`](mtlaccelerationstructurecommandencoder/samplecounters(samplebuffer:sampleindex:barrier:).md) |
| [`MTLComputeCommandEncoder`](mtlcomputecommandencoder.md) | [`sampleCounters(sampleBuffer:sampleIndex:barrier:)`](mtlcomputecommandencoder/samplecounters(samplebuffer:sampleindex:barrier:).md) |
| [`MTLBlitCommandEncoder`](mtlblitcommandencoder.md) | [`sampleCounters(sampleBuffer:sampleIndex:barrier:)`](mtlblitcommandencoder/samplecounters(samplebuffer:sampleindex:barrier:).md) |

The `barrier` parameter for these methods controls whether the pass waits for the GPU to complete all the previous commands in the buffer before sampling the counters (see [`Resource synchronization`](resource-synchronization.md)). Each barrier typically reduces performance, but can be useful during development to get accurate and consistent data across multiple runs.

## See Also

- [Creating a counter sample buffer to store a GPU’s counter data during a pass](creating-a-counter-sample-buffer-to-store-a-gpus-counter-data-during-a-pass.md)
  Make a buffer that provides a place for a GPU to save its runtime performance metrics as it runs a pass.
- [class MTLCounterSampleBufferDescriptor](mtlcountersamplebufferdescriptor.md)
  A group of properties that configures the counter sample buffers you create with it.
- [protocol MTLCounterSampleBuffer](mtlcountersamplebuffer.md)
  A specialized memory buffer that stores a GPU’s counter set data.
- [var MTLCounterDontSample: Int](mtlcounterdontsample.md)
  A sentinel value that instructs an encoder to skip sampling a counter as the GPU runs the encoder’s pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/sampling-gpu-data-into-counter-sample-buffers)*