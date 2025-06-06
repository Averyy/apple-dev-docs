# AudioQueueBuffer

**Framework**: Audio Toolbox  
**Kind**: struct

Defines an audio queue buffer.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct AudioQueueBuffer
```

#### Overview

Each audio queue has an associated set of audio queue buffers.  To allocate a buffer, call the [`AudioQueueAllocateBuffer(_:_:_:)`](audioqueueallocatebuffer(_:_:_:).md) function. To dispose of a buffer, call the [`AudioQueueFreeBuffer(_:_:)`](audioqueuefreebuffer(_:_:).md) function.

If using a VBR compressed audio data format, you may want to instead use the `AudioQueueAllocateBufferWithPacketDescriptions` function. This function allocates a buffer with additional space for packet descriptions. The `mPacketDescriptionCapacity`, `mPacketDescriptions`, and `mPacketDescriptionCount` fields may only be used with buffers allocated with `AudioQueueAllocateBufferWithPacketDescriptions`.

## Topics

### Initializers
- [init(mAudioDataBytesCapacity: UInt32, mAudioData: UnsafeMutableRawPointer, mAudioDataByteSize: UInt32, mUserData: UnsafeMutableRawPointer?, mPacketDescriptionCapacity: UInt32, mPacketDescriptions: UnsafeMutablePointer<AudioStreamPacketDescription>?, mPacketDescriptionCount: UInt32)](audioqueuebuffer/init(maudiodatabytescapacity:maudiodata:maudiodatabytesize:muserdata:mpacketdescriptioncapacity:mpacketdescriptions:mpacketdescriptioncount:).md)
### Instance Properties
- [var mAudioData: UnsafeMutableRawPointer](audioqueuebuffer/maudiodata.md)
  The audio data owned the audio queue buffer. The buffer address cannot be changed.
- [var mAudioDataByteSize: UInt32](audioqueuebuffer/maudiodatabytesize.md)
  The number of bytes of valid audio data in the audio queue buffer’s `mAudioData` field, initially set to `0`. Your callback must set this value for a playback audio queue; for recording, the recording audio queue sets the value.
- [var mAudioDataBytesCapacity: UInt32](audioqueuebuffer/maudiodatabytescapacity.md)
  The size of the audio queue buffer, in bytes. This size is set when a buffer is allocated and cannot be changed.
- [var mPacketDescriptionCapacity: UInt32](audioqueuebuffer/mpacketdescriptioncapacity.md)
  The maximum number of packet descriptions that can be stored in the `mPacketDescriptions` field.
- [var mPacketDescriptionCount: UInt32](audioqueuebuffer/mpacketdescriptioncount.md)
  The number of valid packet descriptions in the buffer. You set this value when providing buffers for playback. The audio queue sets this value when returning buffers from a recording queue.
- [var mPacketDescriptions: UnsafeMutablePointer<AudioStreamPacketDescription>?](audioqueuebuffer/mpacketdescriptions.md)
  An array of `AudioStreamPacketDescription` structures for the buffer.
- [var mUserData: UnsafeMutableRawPointer?](audioqueuebuffer/muserdata.md)
  The custom data structure you specify, for use by your callback function, when creating a recording or playback audio queue.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct AudioQueueChannelAssignment](audioqueuechannelassignment.md)
- [struct AudioQueueProcessingTapFlags](audioqueueprocessingtapflags.md)
- [typealias AudioQueueBufferRef](audioqueuebufferref.md)
  A pointer to an audio queue buffer.
- [struct AudioQueueLevelMeterState](audioqueuelevelmeterstate.md)
  Specifies the current level metering information for one channel of an audio queue.
- [struct AudioQueueParameterEvent](audioqueueparameterevent.md)
  Specifies an audio queue parameter and associated value.
- [typealias AudioQueueParameterID](audioqueueparameterid.md)
  A `UInt32` value that uniquely identifies an audio queue parameter.
- [typealias AudioQueueParameterValue](audioqueueparametervalue.md)
  A `Float32` value for an audio queue parameter.
- [typealias AudioQueueProcessingTapCallback](audioqueueprocessingtapcallback.md)
- [typealias AudioQueueProcessingTapRef](audioqueueprocessingtapref.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueuebuffer)*