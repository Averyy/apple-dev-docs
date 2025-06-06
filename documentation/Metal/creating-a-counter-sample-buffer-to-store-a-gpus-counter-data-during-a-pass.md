# Creating a Counter Sample Buffer to Store a GPU’s Counter Data During a Pass

**Framework**: Metal

Make a buffer that provides a place for a GPU to save its runtime performance metrics as it runs a pass.

#### Overview

You can create and use an [`MTLCounterSampleBuffer`](mtlcountersamplebuffer.md) instance to store information from a GPU counter. To check whether a GPU produces data for a specific counter, see [`Confirming which Counters and Counter Sets a GPU Supports`](confirming-which-counters-and-counter-sets-a-gpu-supports.md). Each  represents memory that a GPU uses to save data from the counter as it runs a pass. Counter sample buffers provide the GPU a place to temporarily store sample data, which avoids the need to synchronize data with the CPU. However, your app has the option to  the sample data with the CPU after the pass completes. See [`Converting a GPU’s Counter Data into a Readable Format`](converting-a-gpus-counter-data-into-a-readable-format.md) for more information about resolving sample data.

Create a counter sample buffer for a GPU by:

1. Confirming a GPU device supports the counter set you want to sample
2. Retrieving the GPU’s instance of that counter set
3. Creating an [`MTLCounterSampleBufferDescriptor`](mtlcountersamplebufferdescriptor.md) instance and configuring its properties for the counter set
4. Passing the descriptor to the GPU device’s [`makeCounterSampleBuffer(descriptor:)`](mtldevice/makecountersamplebuffer(descriptor:).md) factory method

The code example above gives the CPU access to the counter sample buffer by configuring the descriptor’s [`storageMode`](mtlcountersamplebufferdescriptor/storagemode.md) property to [`MTLStorageMode.shared`](mtlstoragemode/shared.md). Alternatively, you can set this property to [`MTLStorageMode.private`](mtlstoragemode/private.md) if your app only uses the GPU to access its data. The example also sets the descriptor’s [`sampleCount`](mtlcountersamplebufferdescriptor/samplecount.md) property to `4` to store the starting and completion timestamps for both the vertex and the fragment stages. The value for the descriptor’s sample count in this example is directly related to the following four properties of the [`MTLRenderPassSampleBufferAttachmentDescriptor`](mtlrenderpasssamplebufferattachmentdescriptor.md) type:

- [`startOfVertexSampleIndex`](mtlrenderpasssamplebufferattachmentdescriptor/startofvertexsampleindex.md)
- [`endOfVertexSampleIndex`](mtlrenderpasssamplebufferattachmentdescriptor/endofvertexsampleindex.md)
- [`startOfFragmentSampleIndex`](mtlrenderpasssamplebufferattachmentdescriptor/startoffragmentsampleindex.md)
- [`endOfFragmentSampleIndex`](mtlrenderpasssamplebufferattachmentdescriptor/endoffragmentsampleindex.md)

> **Note**:  The value you set for [`sampleCount`](mtlcountersamplebufferdescriptor/samplecount.md) depends on the type of data you sample and the number of passes you sample that data from.

When your app has a counter sample buffer, it can then instruct the GPU to save its counter sample data to it during a pass. See [`Sampling GPU Data into Counter Sample Buffers`](sampling-gpu-data-into-counter-sample-buffers.md) for more information.

## See Also

- [class MTLCounterSampleBufferDescriptor](mtlcountersamplebufferdescriptor.md)
  A group of properties that configures the counter sample buffers you create with it.
- [protocol MTLCounterSampleBuffer](mtlcountersamplebuffer.md)
  A specialized memory buffer that stores a GPU’s counter set data.
- [Sampling GPU Data into Counter Sample Buffers](sampling-gpu-data-into-counter-sample-buffers.md)
  Retrieve a GPU’s counter data at a time the GPU supports.
- [var MTLCounterDontSample: Int](mtlcounterdontsample.md)
  A sentinel value that instructs an encoder to skip sampling a counter as the GPU runs the encoder’s pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Metal/creating-a-counter-sample-buffer-to-store-a-gpus-counter-data-during-a-pass)*