# AudioQueueNewOutputWithDispatchQueue(_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func AudioQueueNewOutputWithDispatchQueue(_ outAQ: UnsafeMutablePointer<AudioQueueRef?>, _ inFormat: UnsafePointer<AudioStreamBasicDescription>, _ inFlags: UInt32, _ inCallbackDispatchQueue: dispatch_queue_t, _ inCallbackBlock: @escaping AudioQueueOutputCallbackBlock) -> OSStatus
```

```c
extern OSStatus AudioQueueNewOutputWithDispatchQueue(AudioQueueRef*outAQ, const AudioStreamBasicDescription *inFormat, UInt32 inFlags, dispatch_queue_t inCallbackDispatchQueue, AudioQueueOutputCallbackBlock inCallbackBlock);
```

## See Also

### Creating and Disposing of Audio Queues
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
- [typealias AudioQueueOutputCallbackBlock](./audioqueueoutputcallbackblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueuenewoutputwithdispatchqueue(_:_:_:_:_:))*