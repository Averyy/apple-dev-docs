# AudioQueuePause(_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Pauses audio playback or recording.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioQueuePause(_ inAQ: AudioQueueRef) -> OSStatus
```

```c
extern OSStatus AudioQueuePause(AudioQueueRef inAQ);
```

## Return Value

A result code. See Result Codes.

## Discussion

Pausing an audio queue does not affect buffers or reset the audio queue. To resume playback or recording, call [`AudioQueueStart(_:_:)`](./audioqueuestart%28_,_%29.md).

## Parameters

- `inAQ`: The audio queue to pause.

## See Also

### Controlling Audio Queues
- [func AudioQueueStart(AudioQueueRef, UnsafePointer<AudioTimeStamp>?) -> OSStatus](./audioqueuestart%28_,_%29.md)
  Begins playing or recording audio.
- [func AudioQueuePrime(AudioQueueRef, UInt32, UnsafeMutablePointer<UInt32>?) -> OSStatus](./audioqueueprime%28_,_,_%29.md)
  Decodes enqueued buffers in preparation for playback.
- [func AudioQueueFlush(AudioQueueRef) -> OSStatus](./audioqueueflush%28_%29.md)
  Resets an audio queue’s decoder state.
- [func AudioQueueStop(AudioQueueRef, Bool) -> OSStatus](./audioqueuestop%28_,_%29.md)
  Stops playing or recording audio.
- [func AudioQueueReset(AudioQueueRef) -> OSStatus](./audioqueuereset%28_%29.md)
  Resets an audio queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueuepause(_:))*