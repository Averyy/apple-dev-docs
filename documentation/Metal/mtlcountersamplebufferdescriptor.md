# MTLCounterSampleBufferDescriptor

**Framework**: Metal  
**Kind**: class  
**Role**: Class

A group of properties that configures the counter sample buffers you create with it.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class MTLCounterSampleBufferDescriptor
```

```objc
@interface MTLCounterSampleBufferDescriptor : NSObject
```

## Mentions

- [Creating a counter sample buffer to store a GPU’s counter data during a pass](./creating-a-counter-sample-buffer-to-store-a-gpus-counter-data-during-a-pass.md)

## Overview

To create a new counter sample buffer, create and configure an [`MTLCounterSampleBufferDescriptor`](./mtlcountersamplebufferdescriptor.md) instance, and then call an [`MTLDevice`](./mtldevice.md) instance’s [`makeCounterSampleBuffer(descriptor:)`](./mtldevice/makecountersamplebuffer%28descriptor%29.md) method. See [Creating a counter sample buffer to store a GPU’s counter data during a pass](./creating-a-counter-sample-buffer-to-store-a-gpus-counter-data-during-a-pass.md).

Each new sample counter buffer inherits the values of the descriptor’s properties when you create it. You can modify a descriptor and reuse it to create other counter sample buffers, which has no effect on existing counter sample buffers.

## Topics

### Configuring a descriptor for a counter sample buffer
- [var counterSet: (any MTLCounterSet)?](./mtlcountersamplebufferdescriptor/counterset.md)
  A GPU device’s counter set instance that you want to sample.
- [var label: String](./mtlcountersamplebufferdescriptor/label.md)
  The name for the counter sample buffer you create with the descriptor.
- [var sampleCount: Int](./mtlcountersamplebufferdescriptor/samplecount.md)
  The number of instances of a counter set’s data that a counter sample buffer can store.
- [var storageMode: MTLStorageMode](./mtlcountersamplebufferdescriptor/storagemode.md)
  The memory storage mode for the counter sample buffers you create with the descriptor.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Counter sample buffers
- [Creating a counter sample buffer to store a GPU’s counter data during a pass](./creating-a-counter-sample-buffer-to-store-a-gpus-counter-data-during-a-pass.md)
  Make a buffer that provides a place for a GPU to save its runtime performance metrics as it runs a pass.
- [protocol MTLCounterSampleBuffer](./mtlcountersamplebuffer.md)
  A specialized memory buffer that stores a GPU’s counter set data.
- [Sampling GPU data into counter sample buffers](./sampling-gpu-data-into-counter-sample-buffers.md)
  Retrieve a GPU’s counter data at a time the GPU supports.
- [var MTLCounterDontSample: Int](./mtlcounterdontsample.md)
  A sentinel value that instructs an encoder to skip sampling a counter as the GPU runs the encoder’s pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcountersamplebufferdescriptor)*