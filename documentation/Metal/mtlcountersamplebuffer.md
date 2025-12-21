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

- [Converting a GPU’s counter data into a readable format](converting-a-gpus-counter-data-into-a-readable-format.md)
- [Confirming which counters and counter sets a GPU supports](confirming-which-counters-and-counter-sets-a-gpu-supports.md)
- [Converting GPU timestamps into CPU time](converting-gpu-timestamps-into-cpu-time.md)
- [Creating a counter sample buffer to store a GPU’s counter data during a pass](creating-a-counter-sample-buffer-to-store-a-gpus-counter-data-during-a-pass.md)
- [Sampling GPU data into counter sample buffers](sampling-gpu-data-into-counter-sample-buffers.md)

#### Overview

Create a counter sample buffer by calling an [`MTLDevice`](mtldevice.md) instance’s [`makeCounterSampleBuffer(descriptor:)`](mtldevice/makecountersamplebuffer(descriptor:).md) method. See [`Creating a counter sample buffer to store a GPU’s counter data during a pass`](creating-a-counter-sample-buffer-to-store-a-gpus-counter-data-during-a-pass.md).

You can store a GPU device’s counter set data only with an [`MTLCounterSampleBuffer`](mtlcountersamplebuffer.md) instance that you create from the same device. See [`Sampling GPU data into counter sample buffers`](sampling-gpu-data-into-counter-sample-buffers.md) for information about storing counter sample data in a counter sample buffer.

## Topics

### Resolving the counter sample buffer’s data
- [func resolveCounterRange(Range<Int>) throws -> Data?](mtlcountersamplebuffer/resolvecounterrange(_:).md)
  Transforms samples of a GPU’s counter set from the driver’s internal format to a standard Metal data structure.
### Inspecting the counter sample buffer’s configuration
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

- [Creating a counter sample buffer to store a GPU’s counter data during a pass](creating-a-counter-sample-buffer-to-store-a-gpus-counter-data-during-a-pass.md)
  Make a buffer that provides a place for a GPU to save its runtime performance metrics as it runs a pass.
- [class MTLCounterSampleBufferDescriptor](mtlcountersamplebufferdescriptor.md)
  A group of properties that configures the counter sample buffers you create with it.
- [Sampling GPU data into counter sample buffers](sampling-gpu-data-into-counter-sample-buffers.md)
  Retrieve a GPU’s counter data at a time the GPU supports.
- [var MTLCounterDontSample: Int](mtlcounterdontsample.md)
  A sentinel value that instructs an encoder to skip sampling a counter as the GPU runs the encoder’s pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcountersamplebuffer)*