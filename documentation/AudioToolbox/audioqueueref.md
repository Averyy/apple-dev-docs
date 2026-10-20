# AudioQueueRef

**Framework**: Audio Toolbox  
**Kind**: typealias  
**Role**: Type Alias

Defines an opaque data type that represents an audio queue.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
typealias AudioQueueRef = OpaquePointer
```

```c
typedef struct OpaqueAudioQueue * AudioQueueRef;
```

#### Discussion

An audio queue is a software object you use for recording or playing audio in macOS. It does the work of:

- Connecting to audio hardware
- Managing memory
- Employing codecs, as needed, for compressed audio formats
- Mediating recording or playback

You create, use, and dispose of audio queues using the functions described in [Audio Queue Services](./audio-queue-services.md).

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
- [typealias AudioQueueInputCallbackBlock](./audioqueueinputcallbackblock.md)
- [typealias AudioQueueOutputCallbackBlock](./audioqueueoutputcallbackblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueueref)*