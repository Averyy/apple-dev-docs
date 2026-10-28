# AudioQueueDispose(_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

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

```c
extern OSStatus AudioQueueDispose(AudioQueueRef inAQ, Boolean inImmediate);
```

## Return Value

A result code. See Result Codes.

## Discussion

Disposing of an audio queue also disposes of its resources, including its buffers. After you call this function, you can no longer interact with the audio queue. In addition, the audio queue no longer invokes any callbacks.

## Parameters

- `inAQ`: The audio queue you want to dispose of.
- `inImmediate`: If you pass `true`, the audio queue is disposed of immediately (that is, synchronously). If you pass `false`, disposal does not take place until all enqueued buffers are processed (that is, asynchronously).

## See Also

### Related Documentation
- [func AudioQueueFlush(AudioQueueRef) -> OSStatus](./audioqueueflush%28_%29.md)
  Resets an audio queue’s decoder state.
### Creating and Disposing of Audio Queues
- [func AudioQueueNewOutputWithDispatchQueue(UnsafeMutablePointer<AudioQueueRef?>, UnsafePointer<AudioStreamBasicDescription>, UInt32, dispatch_queue_t, AudioQueueOutputCallbackBlock) -> OSStatus](./audioqueuenewoutputwithdispatchqueue%28_,_,_,_,_%29.md)
- [func AudioQueueNewInputWithDispatchQueue(UnsafeMutablePointer<AudioQueueRef?>, UnsafePointer<AudioStreamBasicDescription>, UInt32, dispatch_queue_t, AudioQueueInputCallbackBlock) -> OSStatus](./audioqueuenewinputwithdispatchqueue%28_,_,_,_,_%29.md)
- [func AudioQueueNewOutput(UnsafePointer<AudioStreamBasicDescription>, AudioQueueOutputCallback, UnsafeMutableRawPointer?, CFRunLoop?, CFString?, UInt32, UnsafeMutablePointer<AudioQueueRef?>) -> OSStatus](./audioqueuenewoutput%28_,_,_,_,_,_,_%29.md)
  Creates a new playback audio queue object.
- [func AudioQueueNewInput(UnsafePointer<AudioStreamBasicDescription>, AudioQueueInputCallback, UnsafeMutableRawPointer?, CFRunLoop?, CFString?, UInt32, UnsafeMutablePointer<AudioQueueRef?>) -> OSStatus](./audioqueuenewinput%28_,_,_,_,_,_,_%29.md)
  Creates a new recording audio queue object.
- [typealias AudioQueueRef](./audioqueueref.md)
  Defines an opaque data type that represents an audio queue.
- [typealias AudioQueueInputCallbackBlock](./audioqueueinputcallbackblock.md)
- [typealias AudioQueueOutputCallbackBlock](./audioqueueoutputcallbackblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueuedispose(_:_:))*