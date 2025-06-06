# AudioQueuePause(_:)

**Framework**: Audio Toolbox  
**Kind**: func

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

#### Return Value

A result code. See Result Codes.

#### Discussion

Pausing an audio queue does not affect buffers or reset the audio queue. To resume playback or recording, call [`AudioQueueStart(_:_:)`](audioqueuestart(_:_:).md).

## Parameters

- `inAQ`: The audio queue to pause.

## See Also

- [func AudioQueueStart(AudioQueueRef, UnsafePointer<AudioTimeStamp>?) -> OSStatus](audioqueuestart(_:_:).md)
  Begins playing or recording audio.
- [func AudioQueuePrime(AudioQueueRef, UInt32, UnsafeMutablePointer<UInt32>?) -> OSStatus](audioqueueprime(_:_:_:).md)
  Decodes enqueued buffers in preparation for playback.
- [func AudioQueueFlush(AudioQueueRef) -> OSStatus](audioqueueflush(_:).md)
  Resets an audio queue’s decoder state.
- [func AudioQueueStop(AudioQueueRef, Bool) -> OSStatus](audioqueuestop(_:_:).md)
  Stops playing or recording audio.
- [func AudioQueueReset(AudioQueueRef) -> OSStatus](audioqueuereset(_:).md)
  Resets an audio queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueuepause(_:))*