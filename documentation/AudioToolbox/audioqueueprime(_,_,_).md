# AudioQueuePrime(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

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

```c
extern OSStatus AudioQueuePrime(AudioQueueRef inAQ, UInt32 inNumberOfFramesToPrepare, UInt32 *outNumberOfFramesPrepared);
```

#### Return Value

A result code. See Result Codes.

#### Discussion

This function decodes enqueued buffers in preparation for playback. It returns when at least the number of audio sample frames specified in `inNumberOfFramesToPrepare` are decoded and ready to play, or (if you pass `0` for the `inNumberOfFramesToPrepare` parameter), when all enqueued buffers are decoded.

To make a buffer of audio data ready to play, use [`AudioQueuePrime(_:_:_:)`](./audioqueueprime%28_,_,_%29.md) as follows:

1. Call [`AudioQueueEnqueueBuffer(_:_:_:_:)`](./audioqueueenqueuebuffer%28_,_,_,_%29.md).
2. Call [`AudioQueuePrime(_:_:_:)`](./audioqueueprime%28_,_,_%29.md).
3. Call [`AudioQueueStart(_:_:)`](./audioqueuestart%28_,_%29.md).

## Parameters

- `inAQ`: The audio queue to be primed.
- `inNumberOfFramesToPrepare`: The number of frames to decode before returning. Pass `0` to decode all enqueued buffers.
- `outNumberOfFramesPrepared`: On output, the number of frames actually decoded and prepared for playback. Pass `NULL` on input if you you are not interested in this information.

## See Also

### Controlling Audio Queues
- [func AudioQueueStart(AudioQueueRef, UnsafePointer<AudioTimeStamp>?) -> OSStatus](./audioqueuestart%28_,_%29.md)
  Begins playing or recording audio.
- [func AudioQueueFlush(AudioQueueRef) -> OSStatus](./audioqueueflush%28_%29.md)
  Resets an audio queue’s decoder state.
- [func AudioQueueStop(AudioQueueRef, Bool) -> OSStatus](./audioqueuestop%28_,_%29.md)
  Stops playing or recording audio.
- [func AudioQueuePause(AudioQueueRef) -> OSStatus](./audioqueuepause%28_%29.md)
  Pauses audio playback or recording.
- [func AudioQueueReset(AudioQueueRef) -> OSStatus](./audioqueuereset%28_%29.md)
  Resets an audio queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueueprime(_:_:_:))*