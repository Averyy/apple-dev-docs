# AudioQueueEnqueueBuffer(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Adds a buffer to the buffer queue of a recording or playback audio queue.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioQueueEnqueueBuffer(_ inAQ: AudioQueueRef, _ inBuffer: AudioQueueBufferRef, _ inNumPacketDescs: UInt32, _ inPacketDescs: UnsafePointer<AudioStreamPacketDescription>?) -> OSStatus
```

#### Return Value

A result code. See Result Codes.

#### Discussion

Audio queue callbacks use this function to reenqueue buffers—placing them “last in line” in a buffer queue. A playback (or *output*) callback reenqueues a buffer after the buffer is filled with fresh audio data (typically from a file). A recording (or *input*) callback reenqueues a buffer after the buffer’s contents were written (typically to a file).

## Parameters

- `inAQ`: The audio queue that owns the audio queue buffer.
- `inBuffer`: The audio queue buffer to add to the buffer queue.
- `inNumPacketDescs`: The number of packets of audio data in the `inBuffer` parameter. Use a value of `0` for any of the following situations: - When playing a constant bit rate (CBR) format.
- When the audio queue is a recording (input) audio queue.
- When the buffer you are reenqueuing was allocated with the [`AudioQueueAllocateBufferWithPacketDescriptions(_:_:_:_:)`](audioqueueallocatebufferwithpacketdescriptions(_:_:_:_:).md) function. In this case, your callback should describe the buffer’s packets in the buffer’s `mPacketDescriptions` and `mPacketDescriptionCount` fields.
- `inPacketDescs`: An array of packet descriptions. Use a value of `NULL` for any of the following situations: - When playing a constant bit rate (CBR) format.
- When the audio queue is an input (recording) audio queue.
- When the buffer you are reenqueuing was allocated with the [`AudioQueueAllocateBufferWithPacketDescriptions(_:_:_:_:)`](audioqueueallocatebufferwithpacketdescriptions(_:_:_:_:).md) function. In this case, your callback should describe the buffer’s packets in the buffer’s `mPacketDescriptions` and `mPacketDescriptionCount` fields.

## See Also

- [func AudioQueueAllocateBuffer(AudioQueueRef, UInt32, UnsafeMutablePointer<AudioQueueBufferRef?>) -> OSStatus](audioqueueallocatebuffer(_:_:_:).md)
  Asks an audio queue object to allocate an audio queue buffer.
- [func AudioQueueAllocateBufferWithPacketDescriptions(AudioQueueRef, UInt32, UInt32, UnsafeMutablePointer<AudioQueueBufferRef?>) -> OSStatus](audioqueueallocatebufferwithpacketdescriptions(_:_:_:_:).md)
  Asks an audio queue object to allocate an audio queue buffer with space for packet descriptions.
- [func AudioQueueFreeBuffer(AudioQueueRef, AudioQueueBufferRef) -> OSStatus](audioqueuefreebuffer(_:_:).md)
  Asks an audio queue to dispose of an audio queue buffer.
- [func AudioQueueEnqueueBufferWithParameters(AudioQueueRef, AudioQueueBufferRef, UInt32, UnsafePointer<AudioStreamPacketDescription>?, UInt32, UInt32, UInt32, UnsafePointer<AudioQueueParameterEvent>?, UnsafePointer<AudioTimeStamp>?, UnsafeMutablePointer<AudioTimeStamp>?) -> OSStatus](audioqueueenqueuebufferwithparameters(_:_:_:_:_:_:_:_:_:_:).md)
  Adds a buffer to the buffer queue of a playback audio queue object, specifying start time and other settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueueenqueuebuffer(_:_:_:_:))*