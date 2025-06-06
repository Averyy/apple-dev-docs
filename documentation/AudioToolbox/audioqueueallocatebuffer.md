# AudioQueueAllocateBuffer(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Asks an audio queue object to allocate an audio queue buffer.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioQueueAllocateBuffer(_ inAQ: AudioQueueRef, _ inBufferByteSize: UInt32, _ outBuffer: UnsafeMutablePointer<AudioQueueBufferRef?>) -> OSStatus
```

#### Return Value

A result code. See Result Codes.

#### Discussion

Once allocated, the pointer to the audio queue buffer and the buffer’s capacity cannot be changed. The buffer’s size field, `mAudioDataByteSize`, which indicates the amount of valid data, is initially set to 0.

## Parameters

- `inAQ`: The audio queue you want to allocate a buffer.
- `inBufferByteSize`: The desired capacity of the new buffer, in bytes. Appropriate capacity depends on the processing you will perform on the data as well as on the audio data format.
- `outBuffer`: On output, points to the newly allocated audio queue buffer.

## See Also

- [func AudioQueueAllocateBufferWithPacketDescriptions(AudioQueueRef, UInt32, UInt32, UnsafeMutablePointer<AudioQueueBufferRef?>) -> OSStatus](audioqueueallocatebufferwithpacketdescriptions(_:_:_:_:).md)
  Asks an audio queue object to allocate an audio queue buffer with space for packet descriptions.
- [func AudioQueueFreeBuffer(AudioQueueRef, AudioQueueBufferRef) -> OSStatus](audioqueuefreebuffer(_:_:).md)
  Asks an audio queue to dispose of an audio queue buffer.
- [func AudioQueueEnqueueBuffer(AudioQueueRef, AudioQueueBufferRef, UInt32, UnsafePointer<AudioStreamPacketDescription>?) -> OSStatus](audioqueueenqueuebuffer(_:_:_:_:).md)
  Adds a buffer to the buffer queue of a recording or playback audio queue.
- [func AudioQueueEnqueueBufferWithParameters(AudioQueueRef, AudioQueueBufferRef, UInt32, UnsafePointer<AudioStreamPacketDescription>?, UInt32, UInt32, UInt32, UnsafePointer<AudioQueueParameterEvent>?, UnsafePointer<AudioTimeStamp>?, UnsafeMutablePointer<AudioTimeStamp>?) -> OSStatus](audioqueueenqueuebufferwithparameters(_:_:_:_:_:_:_:_:_:_:).md)
  Adds a buffer to the buffer queue of a playback audio queue object, specifying start time and other settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueueallocatebuffer(_:_:_:))*