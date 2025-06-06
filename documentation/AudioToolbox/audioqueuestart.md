# AudioQueueStart(_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Begins playing or recording audio.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioQueueStart(_ inAQ: AudioQueueRef, _ inStartTime: UnsafePointer<AudioTimeStamp>?) -> OSStatus
```

#### Return Value

A result code. See Result Codes.

#### Discussion

If the associated audio device is not already running, this function starts it.

## Parameters

- `inAQ`: The audio queue to start.
- `inStartTime`: To specify a start time relative to the timeline of the associated audio device, use the   field of the   structure. Use   to indicate that the audio queue should start as soon as possible.

## See Also

- [func AudioQueuePrime(AudioQueueRef, UInt32, UnsafeMutablePointer<UInt32>?) -> OSStatus](audioqueueprime(_:_:_:).md)
  Decodes enqueued buffers in preparation for playback.
- [func AudioQueueFlush(AudioQueueRef) -> OSStatus](audioqueueflush(_:).md)
  Resets an audio queue’s decoder state.
- [func AudioQueueStop(AudioQueueRef, Bool) -> OSStatus](audioqueuestop(_:_:).md)
  Stops playing or recording audio.
- [func AudioQueuePause(AudioQueueRef) -> OSStatus](audioqueuepause(_:).md)
  Pauses audio playback or recording.
- [func AudioQueueReset(AudioQueueRef) -> OSStatus](audioqueuereset(_:).md)
  Resets an audio queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueuestart(_:_:))*