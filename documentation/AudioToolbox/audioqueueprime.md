# AudioQueuePrime(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Decodes enqueued buffers in preparation for playback.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioQueuePrime(_ inAQ: AudioQueueRef, _ inNumberOfFramesToPrepare: UInt32, _ outNumberOfFramesPrepared: UnsafeMutablePointer<UInt32>?) -> OSStatus
```

#### Return Value

A result code. See Result Codes.

#### Discussion

This function decodes enqueued buffers in preparation for playback. It returns when at least the number of audio sample frames specified in `inNumberOfFramesToPrepare` are decoded and ready to play, or (if you pass `0` for the `inNumberOfFramesToPrepare` parameter), when all enqueued buffers are decoded.

To make a buffer of audio data ready to play, use [`AudioQueuePrime(_:_:_:)`](audioqueueprime(_:_:_:).md) as follows:

1. Call [`AudioQueueEnqueueBuffer(_:_:_:_:)`](audioqueueenqueuebuffer(_:_:_:_:).md).
2. Call [`AudioQueuePrime(_:_:_:)`](audioqueueprime(_:_:_:).md).
3. Call [`AudioQueueStart(_:_:)`](audioqueuestart(_:_:).md).

## Parameters

- `inAQ`: The audio queue to be primed.
- `inNumberOfFramesToPrepare`: The number of frames to decode before returning. Pass   to decode all enqueued buffers.
- `outNumberOfFramesPrepared`: On output, the number of frames actually decoded and prepared for playback. Pass   on input if you you are not interested in this information.

## See Also

- [func AudioQueueStart(AudioQueueRef, UnsafePointer<AudioTimeStamp>?) -> OSStatus](audioqueuestart(_:_:).md)
  Begins playing or recording audio.
- [func AudioQueueFlush(AudioQueueRef) -> OSStatus](audioqueueflush(_:).md)
  Resets an audio queue’s decoder state.
- [func AudioQueueStop(AudioQueueRef, Bool) -> OSStatus](audioqueuestop(_:_:).md)
  Stops playing or recording audio.
- [func AudioQueuePause(AudioQueueRef) -> OSStatus](audioqueuepause(_:).md)
  Pauses audio playback or recording.
- [func AudioQueueReset(AudioQueueRef) -> OSStatus](audioqueuereset(_:).md)
  Resets an audio queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueueprime(_:_:_:))*