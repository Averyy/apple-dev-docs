# AudioQueueOutputCallbackBlock

**Framework**: Audio Toolbox  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
typealias AudioQueueOutputCallbackBlock = (AudioQueueRef, AudioQueueBufferRef) -> Void
```

```c
typedef void (^)(struct OpaqueAudioQueue *, struct AudioQueueBuffer *) AudioQueueOutputCallbackBlock;
```

## See Also

### Creating and Disposing of Audio Queues
- [func AudioQueueNewOutputWithDispatchQueue(UnsafeMutablePointer<AudioQueueRef?>, UnsafePointer<AudioStreamBasicDescription>, UInt32, dispatch_queue_t, AudioQueueOutputCallbackBlock) -> OSStatus](./audioqueuenewoutputwithdispatchqueue%28_,_,_,_,_%29.md)
- [func AudioQueueNewInputWithDispatchQueue(UnsafeMutablePointer<AudioQueueRef?>, UnsafePointer<AudioStreamBasicDescription>, UInt32, dispatch_queue_t, AudioQueueInputCallbackBlock) -> OSStatus](./audioqueuenewinputwithdispatchqueue%28_,_,_,_,_%29.md)
- [func AudioQueueNewOutput(UnsafePointer<AudioStreamBasicDescription>, AudioQueueOutputCallback, UnsafeMutableRawPointer?, CFRunLoop?, CFString?, UInt32, UnsafeMutablePointer<AudioQueueRef?>) -> OSStatus](./audioqueuenewoutput%28_,_,_,_,_,_,_%29.md)
  Creates a new playback audio queue object.
- [func AudioQueueNewInput(UnsafePointer<AudioStreamBasicDescription>, AudioQueueInputCallback, UnsafeMutableRawPointer?, CFRunLoop?, CFString?, UInt32, UnsafeMutablePointer<AudioQueueRef?>) -> OSStatus](./audioqueuenewinput%28_,_,_,_,_,_,_%29.md)
  Creates a new recording audio queue object.
- [func AudioQueueDispose(AudioQueueRef, Bool) -> OSStatus](./audioqueuedispose%28_,_%29.md)
  Disposes of an audio queue.
- [typealias AudioQueueRef](./audioqueueref.md)
  Defines an opaque data type that represents an audio queue.
- [typealias AudioQueueInputCallbackBlock](./audioqueueinputcallbackblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueueoutputcallbackblock)*