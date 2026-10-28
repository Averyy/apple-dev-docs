# play(atTime:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Plays audio asynchronously, starting at a specified point in the audio output device’s timeline.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func play(atTime time: TimeInterval) -> Bool
```

```objc
- (BOOL) playAtTime:(NSTimeInterval) time;
```

## Return Value

[`true`](../../Swift/true.md) if playback starts successfully; otherwise, [`false`](../../Swift/false.md).

## Discussion

Use this method to precisely synchronize the playback of two or more audio player objects as the following example shows:

```swift
func startSynchronizedPlayback() {
    // Create a time offset relative to the current device time.
    let timeOffset = playerOne.deviceCurrentTime + 0.01
    
    // Start playback of both players at the same time.
    playerOne.play(atTime: timeOffset)
    playerTwo.play(atTime: timeOffset)
}
```

Calling this method implicitly calls [`prepareToPlay()`](./preparetoplay%28%29.md) if the audio player is unprepared for playback.

## Parameters

- `time`: The audio device time to begin playback. This time must be later than the device’s current time.

## See Also

### Controlling playback
- [func prepareToPlay() -> Bool](./preparetoplay%28%29.md)
  Prepares the player for audio playback.
- [func play() -> Bool](./play%28%29.md)
  Plays audio asynchronously.
- [func pause()](./pause%28%29.md)
  Pauses audio playback.
- [func stop()](./stop%28%29.md)
  Stops playback and undoes the setup the system requires for playback.
- [var isPlaying: Bool](./isplaying.md)
  A Boolean value that indicates whether the player is currently playing audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayer/play(attime:))*