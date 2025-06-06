# AudioQueueReset(_:)

**Framework**: Audio Toolbox  
**Kind**: func

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

#### Return Value

A result code. See Result Codes.

#### Discussion

This function immediately resets an audio queue, flushes any queued buffers (invoking callbacks as necessary), removes all buffers from previously scheduled use, and resets decoder and digital signal processing (DSP) state.

If you queue buffers after calling this function, processing does not begin until the decoder and DSP state of the audio queue are reset. This might create an audible discontinuity (or “glitch”).

This function is called automatically when you call [`AudioQueueStop(_:_:)`](audioqueuestop(_:_:).md).

## Parameters

- `inAQ`: The audio queue to reset.

## See Also

- [func AudioQueueStart(AudioQueueRef, UnsafePointer<AudioTimeStamp>?) -> OSStatus](audioqueuestart(_:_:).md)
  Begins playing or recording audio.
- [func AudioQueuePrime(AudioQueueRef, UInt32, UnsafeMutablePointer<UInt32>?) -> OSStatus](audioqueueprime(_:_:_:).md)
  Decodes enqueued buffers in preparation for playback.
- [func AudioQueueFlush(AudioQueueRef) -> OSStatus](audioqueueflush(_:).md)
  Resets an audio queue’s decoder state.
- [func AudioQueueStop(AudioQueueRef, Bool) -> OSStatus](audioqueuestop(_:_:).md)
  Stops playing or recording audio.
- [func AudioQueuePause(AudioQueueRef) -> OSStatus](audioqueuepause(_:).md)
  Pauses audio playback or recording.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueuereset(_:))*