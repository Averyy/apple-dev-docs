# AudioBuffer

**Framework**: Core Audio Types  
**Kind**: struct

A structure that holds a buffer of audio data.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
struct AudioBuffer
```

#### Overview

An audio buffer holds a single buffer of audio data in its [`mData`](audiobuffer/mdata.md) field. The buffer can represent two types of audio:

- A single, monophonic, noninterleaved channel of audio
- Interleaved audio with the number of channels set by the [`mNumberChannels`](audiobuffer/mnumberchannels.md) field

> **Note**:  The [`mDataByteSize`](audiostreampacketdescription/mdatabytesize.md) and [`mNumberChannels`](audiobuffer/mnumberchannels.md) parameters needs to match the memory layout of [`mData`](audiobuffer/mdata.md), so update the size and number of channels when you update the data field.

 The [`mDataByteSize`](audiostreampacketdescription/mdatabytesize.md) and [`mNumberChannels`](audiobuffer/mnumberchannels.md) parameters needs to match the memory layout of [`mData`](audiobuffer/mdata.md), so update the size and number of channels when you update the data field.

## Topics

### Creating a Buffer
- [init()](audiobuffer/init.md)
  Creates an empty audio buffer.
- [init(mNumberChannels: UInt32, mDataByteSize: UInt32, mData: UnsafeMutableRawPointer?)](audiobuffer/init(mnumberchannels:mdatabytesize:mdata:).md)
  Creates an audio buffer with audio data.
### Accessing the Audio
- [var mNumberChannels: UInt32](audiobuffer/mnumberchannels.md)
  The number of interleaved channels in the buffer.
- [var mDataByteSize: UInt32](audiobuffer/mdatabytesize.md)
  The number of bytes in the buffer.
- [var mData: UnsafeMutableRawPointer?](audiobuffer/mdata.md)
  A pointer to a buffer of audio data.
### Initializers
- [init<Element>(UnsafeMutableBufferPointer<Element>, numberOfChannels: Int)](audiobuffer/init(_:numberofchannels:).md)
  Initialize an `AudioBuffer` from an `UnsafeMutableBufferPointer<Element>`.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct AudioBufferList](audiobufferlist.md)
  A structure that stores a variable-length array of audio buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audiobuffer)*