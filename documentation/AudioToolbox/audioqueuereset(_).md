# AudioQueueReset(_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Resets an audio queue.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioQueueReset(_ inAQ: AudioQueueRef) -> OSStatus
```

```c
extern OSStatus AudioQueueReset(AudioQueueRef inAQ);
```

#### Return Value

A result code. See Result Codes.

#### Discussion

This function immediately resets an audio queue, flushes any queued buffers (invoking callbacks as necessary), removes all buffers from previously scheduled use, and resets decoder and digital signal processing (DSP) state.

If you queue buffers after calling this function, processing does not begin until the decoder and DSP state of the audio queue are reset. This might create an audible discontinuity (or “glitch”).

This function is called automatically when you call [`AudioQueueStop(_:_:)`](./audioqueuestop%28_,_%29.md).

## Parameters

- `inAQ`: The audio queue to reset.

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
- [func AudioQueuePause(AudioQueueRef) -> OSStatus](./audioqueuepause%28_%29.md)
  Pauses audio playback or recording.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueuereset(_:))*