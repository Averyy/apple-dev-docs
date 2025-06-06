# AudioQueueInputCallback

**Framework**: Audio Toolbox  
**Kind**: typealias

Called by the system when a recording audio queue has finished filling an audio queue buffer.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias AudioQueueInputCallback = (UnsafeMutableRawPointer?, AudioQueueRef, AudioQueueBufferRef, UnsafePointer<AudioTimeStamp>, UInt32, UnsafePointer<AudioStreamPacketDescription>?) -> Void
```

#### Discussion

If you name your callback function `MyAudioQueueInputCallback`, you would declare it like this:

##### Discussion

You specify a recording audio queue callback when calling the [`AudioQueueNewInput(_:_:_:_:_:_:_:)`](audioqueuenewinput(_:_:_:_:_:_:_:).md) function. The callback is invoked each time its recording audio queue has filled an audio queue buffer with fresh audio data. Typically, your callback writes the data to a file or other buffer, and then reenqueues the audio queue buffer to receive more data.

## Parameters

- `inUserData`: The custom data you’ve specified in the   parameter of the   function. Typically, this includes format and state information for the audio queue.
- `inAQ`: The recording audio queue that invoked the callback.
- `inBuffer`: An audio queue buffer, newly filled by the recording audio queue, containing the new audio data your callback needs to write.
- `inStartTime`: The sample time for the start of the audio queue buffer. This parameter is not used in basic recording.
- `inNumberPacketDescriptions`: The number of packets of audio data sent to the callback in the   parameter. When recording in a constant bit rate (CBR) format, the audio queue sets this parameter to  .
- `inPacketDescs`: For compressed formats that require packet descriptions, the set of packet descriptions produced by the encoder for audio data in the   parameter. When recording in a CBR format, the audio queue sets this parameter to  .

## See Also

- [typealias AudioQueueOutputCallback](audioqueueoutputcallback.md)
  Called by the system when an audio queue buffer is available for reuse.
- [typealias AudioQueuePropertyListenerProc](audioqueuepropertylistenerproc.md)
  Called by the system when a specified audio queue property changes value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueueinputcallback)*