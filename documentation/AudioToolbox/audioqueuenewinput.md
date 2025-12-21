# AudioQueueNewInput(_:_:_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Creates a new recording audio queue object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioQueueNewInput(_ inFormat: UnsafePointer<AudioStreamBasicDescription>, _ inCallbackProc: AudioQueueInputCallback, _ inUserData: UnsafeMutableRawPointer?, _ inCallbackRunLoop: CFRunLoop?, _ inCallbackRunLoopMode: CFString?, _ inFlags: UInt32, _ outAQ: UnsafeMutablePointer<AudioQueueRef?>) -> OSStatus
```

#### Return Value

A result code. See Result Codes.

## Parameters

- `inFormat`: The compressed or uncompressed audio data format to record to. When recording to linear PCM, only interleaved formats are supported.
- `inCallbackProc`: A callback function to use with the recording audio queue. The audio queue calls this function when the audio queue has finished filling a buffer. See  .
- `inUserData`: A custom data structure for use with the callback function.
- `inCallbackRunLoop`: The event loop on which the callback function pointed to by the    parameter is to be called. If you specify  , the callback is called on one of the audio queue’s internal threads.
- `inCallbackRunLoopMode`: The run loop mode in which to invoke the callback function specified in the   parameter. Typically, you pass   or use  , which is equivalent. You can choose to create your own thread with your own run loops. For more information on run loops, see Run Loops and  .
- `inFlags`: Reserved for future use. Must be  .
- `outAQ`: On output, the newly created recording audio queue.

## See Also

- [func AudioQueueSetOfflineRenderFormat(AudioQueueRef, UnsafePointer<AudioStreamBasicDescription>?, UnsafePointer<AudioChannelLayout>?) -> OSStatus](audioqueuesetofflinerenderformat(_:_:_:).md)
  Sets the rendering mode and audio format for a playback audio queue.
- [func AudioQueueNewOutputWithDispatchQueue(UnsafeMutablePointer<AudioQueueRef?>, UnsafePointer<AudioStreamBasicDescription>, UInt32, dispatch_queue_t, AudioQueueOutputCallbackBlock) -> OSStatus](audioqueuenewoutputwithdispatchqueue(_:_:_:_:_:).md)
- [func AudioQueueNewInputWithDispatchQueue(UnsafeMutablePointer<AudioQueueRef?>, UnsafePointer<AudioStreamBasicDescription>, UInt32, dispatch_queue_t, AudioQueueInputCallbackBlock) -> OSStatus](audioqueuenewinputwithdispatchqueue(_:_:_:_:_:).md)
- [func AudioQueueNewOutput(UnsafePointer<AudioStreamBasicDescription>, AudioQueueOutputCallback, UnsafeMutableRawPointer?, CFRunLoop?, CFString?, UInt32, UnsafeMutablePointer<AudioQueueRef?>) -> OSStatus](audioqueuenewoutput(_:_:_:_:_:_:_:).md)
  Creates a new playback audio queue object.
- [func AudioQueueDispose(AudioQueueRef, Bool) -> OSStatus](audioqueuedispose(_:_:).md)
  Disposes of an audio queue.
- [typealias AudioQueueRef](audioqueueref.md)
  Defines an opaque data type that represents an audio queue.
- [typealias AudioQueueInputCallbackBlock](audioqueueinputcallbackblock.md)
- [typealias AudioQueueOutputCallbackBlock](audioqueueoutputcallbackblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueuenewinput(_:_:_:_:_:_:_:))*