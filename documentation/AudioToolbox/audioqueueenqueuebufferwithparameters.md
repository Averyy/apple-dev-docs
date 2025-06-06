# AudioQueueEnqueueBufferWithParameters(_:_:_:_:_:_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Adds a buffer to the buffer queue of a playback audio queue object, specifying start time and other settings.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioQueueEnqueueBufferWithParameters(_ inAQ: AudioQueueRef, _ inBuffer: AudioQueueBufferRef, _ inNumPacketDescs: UInt32, _ inPacketDescs: UnsafePointer<AudioStreamPacketDescription>?, _ inTrimFramesAtStart: UInt32, _ inTrimFramesAtEnd: UInt32, _ inNumParamValues: UInt32, _ inParamValues: UnsafePointer<AudioQueueParameterEvent>?, _ inStartTime: UnsafePointer<AudioTimeStamp>?, _ outActualStartTime: UnsafeMutablePointer<AudioTimeStamp>?) -> OSStatus
```

#### Return Value

A result code. See Result Codes.

#### Discussion

You can exert some control over the buffer queue with this function. You can assign audio queue settings that are, in effect, carried by an audio queue buffer as you enqueue it. Hence, settings take effect when an audio queue buffer begins playing.

This function applies only to playback. Recording audio queues do not take parameters and do not support variable bit rate (VBR) formats (which might require trimming).

## Parameters

- `inAQ`: The audio queue object that owns the audio queue buffer.
- `inBuffer`: The audio queue buffer to add to the buffer queue. Before calling this function, the buffer must contain the audio data to be played.
- `inNumPacketDescs`: The number of packets of audio data in the   parameter. Use a value of   for either of the following situations:
- `inPacketDescs`: An array of packet descriptions. Use a value of   for either of the following situations:
- `inTrimFramesAtStart`: The number of priming frames to skip at the start of the buffer.
- `inTrimFramesAtEnd`: The number of frames to skip at the end of the buffer.
- `inNumParamValues`: The number of audio queue parameter values pointed to by the   parameter. If you are not setting parameters, use  .
- `inParamValues`: Assign parameter values before playback—they cannot be changed while a buffer is playing. Changes to audio queue buffer parameters take effect when the buffer starts playing.
- `inStartTime`: Buffers play in the order they are enqueued (first in, first out). If multiple buffers are queued, the start times must be in ascending order or  ; otherwise, an error occurs.  This parameter specifies when audio data is to start playing, ignoring any trim frames specified in the   parameter.
- `outActualStartTime`: On output, the time when the buffer will actually start playing.

## See Also

- [func AudioQueueAllocateBuffer(AudioQueueRef, UInt32, UnsafeMutablePointer<AudioQueueBufferRef?>) -> OSStatus](audioqueueallocatebuffer(_:_:_:).md)
  Asks an audio queue object to allocate an audio queue buffer.
- [func AudioQueueAllocateBufferWithPacketDescriptions(AudioQueueRef, UInt32, UInt32, UnsafeMutablePointer<AudioQueueBufferRef?>) -> OSStatus](audioqueueallocatebufferwithpacketdescriptions(_:_:_:_:).md)
  Asks an audio queue object to allocate an audio queue buffer with space for packet descriptions.
- [func AudioQueueFreeBuffer(AudioQueueRef, AudioQueueBufferRef) -> OSStatus](audioqueuefreebuffer(_:_:).md)
  Asks an audio queue to dispose of an audio queue buffer.
- [func AudioQueueEnqueueBuffer(AudioQueueRef, AudioQueueBufferRef, UInt32, UnsafePointer<AudioStreamPacketDescription>?) -> OSStatus](audioqueueenqueuebuffer(_:_:_:_:).md)
  Adds a buffer to the buffer queue of a recording or playback audio queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueueenqueuebufferwithparameters(_:_:_:_:_:_:_:_:_:_:))*