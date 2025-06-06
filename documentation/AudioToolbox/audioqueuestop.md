# AudioQueueStop(_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Stops playing or recording audio.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioQueueStop(_ inAQ: AudioQueueRef, _ inImmediate: Bool) -> OSStatus
```

#### Return Value

A result code. See Result Codes.

#### Discussion

This function resets an audio queue, stops the audio hardware associated with the queue if it is not in use by other audio services, and stops the audio queue. When recording, this function is typically invoked by a user. When playing back, a playback audio queue callback should call this function when there is no more audio to play.

## Parameters

- `inAQ`: The audio queue to stop.
- `inImmediate`: If you pass  , stopping occurs immediately (that is,  ). If you pass  , the function returns immediately, but the audio queue does not stop until its queued buffers are played or recorded (that is, the stop occurs  ). Audio queue callbacks are invoked as necessary until the queue actually stops.

## See Also

- [func AudioQueueStart(AudioQueueRef, UnsafePointer<AudioTimeStamp>?) -> OSStatus](audioqueuestart(_:_:).md)
  Begins playing or recording audio.
- [func AudioQueuePrime(AudioQueueRef, UInt32, UnsafeMutablePointer<UInt32>?) -> OSStatus](audioqueueprime(_:_:_:).md)
  Decodes enqueued buffers in preparation for playback.
- [func AudioQueueFlush(AudioQueueRef) -> OSStatus](audioqueueflush(_:).md)
  Resets an audio queue’s decoder state.
- [func AudioQueuePause(AudioQueueRef) -> OSStatus](audioqueuepause(_:).md)
  Pauses audio playback or recording.
- [func AudioQueueReset(AudioQueueRef) -> OSStatus](audioqueuereset(_:).md)
  Resets an audio queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueuestop(_:_:))*