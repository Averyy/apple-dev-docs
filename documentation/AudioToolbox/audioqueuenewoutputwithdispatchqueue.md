# AudioQueueNewOutputWithDispatchQueue(_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

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

## See Also

- [func AudioQueueNewInputWithDispatchQueue(UnsafeMutablePointer<AudioQueueRef?>, UnsafePointer<AudioStreamBasicDescription>, UInt32, dispatch_queue_t, AudioQueueInputCallbackBlock) -> OSStatus](audioqueuenewinputwithdispatchqueue(_:_:_:_:_:).md)
- [func AudioQueueNewOutput(UnsafePointer<AudioStreamBasicDescription>, AudioQueueOutputCallback, UnsafeMutableRawPointer?, CFRunLoop?, CFString?, UInt32, UnsafeMutablePointer<AudioQueueRef?>) -> OSStatus](audioqueuenewoutput(_:_:_:_:_:_:_:).md)
  Creates a new playback audio queue object.
- [func AudioQueueNewInput(UnsafePointer<AudioStreamBasicDescription>, AudioQueueInputCallback, UnsafeMutableRawPointer?, CFRunLoop?, CFString?, UInt32, UnsafeMutablePointer<AudioQueueRef?>) -> OSStatus](audioqueuenewinput(_:_:_:_:_:_:_:).md)
  Creates a new recording audio queue object.
- [func AudioQueueDispose(AudioQueueRef, Bool) -> OSStatus](audioqueuedispose(_:_:).md)
  Disposes of an audio queue.
- [typealias AudioQueueRef](audioqueueref.md)
  Defines an opaque data type that represents an audio queue.
- [typealias AudioQueueInputCallbackBlock](audioqueueinputcallbackblock.md)
- [typealias AudioQueueOutputCallbackBlock](audioqueueoutputcallbackblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueuenewoutputwithdispatchqueue(_:_:_:_:_:))*