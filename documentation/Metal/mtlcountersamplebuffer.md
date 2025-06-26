# MTLCounterSampleBuffer

**Framework**: Metal  
**Kind**: protocol

A specialized memory buffer that stores a GPU’s counter set data.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
protocol MTLCounterSampleBuffer : NSObjectProtocol
```

## Mentions

- [Converting a GPU’s Counter Data into a Readable Format](converting-a-gpus-counter-data-into-a-readable-format.md)
- [Creating a Counter Sample Buffer to Store a GPU’s Counter Data During a Pass](creating-a-counter-sample-buffer-to-store-a-gpus-counter-data-during-a-pass.md)
- [Converting GPU Timestamps into CPU Time](converting-gpu-timestamps-into-cpu-time.md)
- [Confirming which Counters and Counter Sets a GPU Supports](confirming-which-counters-and-counter-sets-a-gpu-supports.md)
- [Sampling GPU Data into Counter Sample Buffers](sampling-gpu-data-into-counter-sample-buffers.md)

#### Overview

Create a counter sample buffer by calling an [`MTLDevice`](mtldevice.md) instance’s [`makeCounterSampleBuffer(descriptor:)`](mtldevice/makecountersamplebuffer(descriptor:).md) method. See [`Creating a Counter Sample Buffer to Store a GPU’s Counter Data During a Pass`](creating-a-counter-sample-buffer-to-store-a-gpus-counter-data-during-a-pass.md).

You can store a GPU device’s counter set data only with an [`MTLCounterSampleBuffer`](mtlcountersamplebuffer.md) instance that you create from the same device. See [`Sampling GPU Data into Counter Sample Buffers`](sampling-gpu-data-into-counter-sample-buffers.md) for information about storing counter sample data in a counter sample buffer.

## Topics

### Resolving the Counter Sample Buffer’s Data
- [func resolveCounterRange(Range<Int>) throws -> Data?](mtlcountersamplebuffer/resolvecounterrange(_:).md)
  Transforms samples of a GPU’s counter set from the driver’s internal format to a standard Metal data structure.
### Inspecting the Counter Sample Buffer’s Configuration
- [var label: String](mtlcountersamplebuffer/label.md)
  A string that identifies the counter sample buffer.
- [var device: any MTLDevice](mtlcountersamplebuffer/device.md)
  The GPU device instance that owns the counter sample buffer.
- [var sampleCount: Int](mtlcountersamplebuffer/samplecount.md)
  The number of samples in the buffer.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Creating a Counter Sample Buffer to Store a GPU’s Counter Data During a Pass](creating-a-counter-sample-buffer-to-store-a-gpus-counter-data-during-a-pass.md)
  Make a buffer that provides a place for a GPU to save its runtime performance metrics as it runs a pass.
- [class MTLCounterSampleBufferDescriptor](mtlcountersamplebufferdescriptor.md)
  A group of properties that configures the counter sample buffers you create with it.
- [Sampling GPU Data into Counter Sample Buffers](sampling-gpu-data-into-counter-sample-buffers.md)
  Retrieve a GPU’s counter data at a time the GPU supports.
- [var MTLCounterDontSample: Int](mtlcounterdontsample.md)
  A sentinel value that instructs an encoder to skip sampling a counter as the GPU runs the encoder’s pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcountersamplebuffer)*