# AudioQueueFlush(_:)

**Framework**: Audio Toolbox  
**Kind**: func

Resets an audio queue’s decoder state.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioQueueFlush(_ inAQ: AudioQueueRef) -> OSStatus
```

#### Return Value

A result code. See Result Codes.

#### Discussion

Call [`AudioQueueFlush(_:)`](audioqueueflush(_:).md) after enqueuing the last audio queue buffer to ensure that all buffered data, as well as all audio data in the midst of processing, gets recorded or played. If you do not call this function, stale data in the audio queue’s decoder may interfere with playback or recording of the next set of buffers.

Call this function before calling [`AudioQueueStop(_:_:)`](audioqueuestop(_:_:).md) if you want to ensure that all enqueued data reaches the destination. If you call [`AudioQueueStop(_:_:)`](audioqueuestop(_:_:).md) with the `inImmediate` parameter set to `false`, calling this function does nothing; under those conditions, [`AudioQueueStop(_:_:)`](audioqueuestop(_:_:).md) calls this function.

## Parameters

- `inAQ`: The audio queue to flush.

## See Also

- [func AudioQueueDispose(AudioQueueRef, Bool) -> OSStatus](audioqueuedispose(_:_:).md)
  Disposes of an audio queue.
- [func AudioQueueStart(AudioQueueRef, UnsafePointer<AudioTimeStamp>?) -> OSStatus](audioqueuestart(_:_:).md)
  Begins playing or recording audio.
- [func AudioQueuePrime(AudioQueueRef, UInt32, UnsafeMutablePointer<UInt32>?) -> OSStatus](audioqueueprime(_:_:_:).md)
  Decodes enqueued buffers in preparation for playback.
- [func AudioQueueStop(AudioQueueRef, Bool) -> OSStatus](audioqueuestop(_:_:).md)
  Stops playing or recording audio.
- [func AudioQueuePause(AudioQueueRef) -> OSStatus](audioqueuepause(_:).md)
  Pauses audio playback or recording.
- [func AudioQueueReset(AudioQueueRef) -> OSStatus](audioqueuereset(_:).md)
  Resets an audio queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueueflush(_:))*