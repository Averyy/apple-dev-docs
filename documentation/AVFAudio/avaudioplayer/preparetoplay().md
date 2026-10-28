# prepareToPlay()

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Prepares the player for audio playback.

**Availability**:
- iOS 2.2+
- iPadOS 2.2+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func prepareToPlay() -> Bool
```

```objc
- (BOOL) prepareToPlay;
```

## Return Value

[`true`](../../Swift/true.md) if the system successfully prepares the player; otherwise, [`false`](../../Swift/false.md).

## Discussion

Calling this method preloads audio buffers and acquires the audio hardware necessary for playback. This method activates the audio session, so pass [`false`](../../Swift/false.md) to [`setActive:error:`](../avaudiosession/setactive_error_.md) if immediate playback isn’t necessary. For example, when using the category option [`duckOthers`](../avaudiosession/categoryoptions-swift.struct/duckothers.md), this method lowers the audio outside of the app.

The system calls this method when using the method [`play()`](./play%28%29.md), but calling it in advance minimizes the delay between calling `play()` and the start of sound output.

Calling [`stop()`](./stop%28%29.md), or allowing a sound to finish playing, undoes this setup.

## See Also

### Controlling playback
- [func play() -> Bool](./play%28%29.md)
  Plays audio asynchronously.
- [func play(atTime: TimeInterval) -> Bool](./play%28attime%29.md)
  Plays audio asynchronously, starting at a specified point in the audio output device’s timeline.
- [func pause()](./pause%28%29.md)
  Pauses audio playback.
- [func stop()](./stop%28%29.md)
  Stops playback and undoes the setup the system requires for playback.
- [var isPlaying: Bool](./isplaying.md)
  A Boolean value that indicates whether the player is currently playing audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayer/preparetoplay())*