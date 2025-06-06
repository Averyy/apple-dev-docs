# AudioQueueDispose(_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Disposes of an audio queue.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioQueueDispose(_ inAQ: AudioQueueRef, _ inImmediate: Bool) -> OSStatus
```

#### Return Value

A result code. See Result Codes.

#### Discussion

Disposing of an audio queue also disposes of its resources, including its buffers. After you call this function, you can no longer interact with the audio queue. In addition, the audio queue no longer invokes any callbacks.

## Parameters

- `inAQ`: The audio queue you want to dispose of.
- `inImmediate`: If you pass  , the audio queue is disposed of immediately (that is, synchronously). If you pass  , disposal does not take place until all enqueued buffers are processed (that is, asynchronously).

## See Also

- [func AudioQueueFlush(AudioQueueRef) -> OSStatus](audioqueueflush(_:).md)
  Resets an audio queue’s decoder state.
- [func AudioQueueNewOutputWithDispatchQueue(UnsafeMutablePointer<AudioQueueRef?>, UnsafePointer<AudioStreamBasicDescription>, UInt32, dispatch_queue_t, AudioQueueOutputCallbackBlock) -> OSStatus](audioqueuenewoutputwithdispatchqueue(_:_:_:_:_:).md)
- [func AudioQueueNewInputWithDispatchQueue(UnsafeMutablePointer<AudioQueueRef?>, UnsafePointer<AudioStreamBasicDescription>, UInt32, dispatch_queue_t, AudioQueueInputCallbackBlock) -> OSStatus](audioqueuenewinputwithdispatchqueue(_:_:_:_:_:).md)
- [func AudioQueueNewOutput(UnsafePointer<AudioStreamBasicDescription>, AudioQueueOutputCallback, UnsafeMutableRawPointer?, CFRunLoop?, CFString?, UInt32, UnsafeMutablePointer<AudioQueueRef?>) -> OSStatus](audioqueuenewoutput(_:_:_:_:_:_:_:).md)
  Creates a new playback audio queue object.
- [func AudioQueueNewInput(UnsafePointer<AudioStreamBasicDescription>, AudioQueueInputCallback, UnsafeMutableRawPointer?, CFRunLoop?, CFString?, UInt32, UnsafeMutablePointer<AudioQueueRef?>) -> OSStatus](audioqueuenewinput(_:_:_:_:_:_:_:).md)
  Creates a new recording audio queue object.
- [typealias AudioQueueRef](audioqueueref.md)
  Defines an opaque data type that represents an audio queue.
- [typealias AudioQueueInputCallbackBlock](audioqueueinputcallbackblock.md)
- [typealias AudioQueueOutputCallbackBlock](audioqueueoutputcallbackblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueuedispose(_:_:))*