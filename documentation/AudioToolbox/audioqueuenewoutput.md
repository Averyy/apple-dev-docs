# AudioQueueNewOutput(_:_:_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Creates a new playback audio queue object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioQueueNewOutput(_ inFormat: UnsafePointer<AudioStreamBasicDescription>, _ inCallbackProc: AudioQueueOutputCallback, _ inUserData: UnsafeMutableRawPointer?, _ inCallbackRunLoop: CFRunLoop?, _ inCallbackRunLoopMode: CFString?, _ inFlags: UInt32, _ outAQ: UnsafeMutablePointer<AudioQueueRef?>) -> OSStatus
```

#### Return Value

A result code. See Result Codes.

## Parameters

- `inFormat`: The data format of the audio to play. For linear PCM, only interleaved formats are supported. Compressed formats are also supported.
- `inCallbackProc`: A callback function to use with the playback audio queue. The audio queue invokes the callback when the audio queue has finished acquiring a buffer. See  .
- `inUserData`: A custom data structure for use with the callback function.
- `inCallbackRunLoop`: The event loop on which the callback function pointed to by the   parameter is to be called. If you specify  , the callback is invoked on one of the audio queue’s internal threads.
- `inCallbackRunLoopMode`: The run loop mode in which to invoke the callback function specified in the   parameter. Typically, you pass   or use  , which is equivalent. You can choose to create your own thread with your own run loops. For more information on run loops, see Run Loops and  doc://com.apple.documentation/documentation/corefoundation/cfrunloop-rht .
- `inFlags`: Reserved for future use. Must be  .
- `outAQ`: On output, the newly created playback audio queue object.

## See Also

- [func AudioQueueOfflineRender(AudioQueueRef, UnsafePointer<AudioTimeStamp>, AudioQueueBufferRef, UInt32) -> OSStatus](audioqueueofflinerender(_:_:_:_:).md)
  Exports audio to a buffer, instead of to a device, using a playback audio queue.
- [func AudioQueueNewOutputWithDispatchQueue(UnsafeMutablePointer<AudioQueueRef?>, UnsafePointer<AudioStreamBasicDescription>, UInt32, dispatch_queue_t, AudioQueueOutputCallbackBlock) -> OSStatus](audioqueuenewoutputwithdispatchqueue(_:_:_:_:_:).md)
- [func AudioQueueNewInputWithDispatchQueue(UnsafeMutablePointer<AudioQueueRef?>, UnsafePointer<AudioStreamBasicDescription>, UInt32, dispatch_queue_t, AudioQueueInputCallbackBlock) -> OSStatus](audioqueuenewinputwithdispatchqueue(_:_:_:_:_:).md)
- [func AudioQueueNewInput(UnsafePointer<AudioStreamBasicDescription>, AudioQueueInputCallback, UnsafeMutableRawPointer?, CFRunLoop?, CFString?, UInt32, UnsafeMutablePointer<AudioQueueRef?>) -> OSStatus](audioqueuenewinput(_:_:_:_:_:_:_:).md)
  Creates a new recording audio queue object.
- [func AudioQueueDispose(AudioQueueRef, Bool) -> OSStatus](audioqueuedispose(_:_:).md)
  Disposes of an audio queue.
- [typealias AudioQueueRef](audioqueueref.md)
  Defines an opaque data type that represents an audio queue.
- [typealias AudioQueueInputCallbackBlock](audioqueueinputcallbackblock.md)
- [typealias AudioQueueOutputCallbackBlock](audioqueueoutputcallbackblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueuenewoutput(_:_:_:_:_:_:_:))*