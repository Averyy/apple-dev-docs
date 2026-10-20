# play()

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Plays audio asynchronously.

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
func play() -> Bool
```

```objc
- (BOOL) play;
```

#### Return Value

[`true`](../../Swift/true.md) if playback starts successfully; otherwise, [`false`](../../Swift/false.md).

#### Discussion

Calling this method implicitly calls [`prepareToPlay()`](./preparetoplay%28%29.md) if the audio player is unprepared for playback.

## See Also

### Controlling playback
- [func prepareToPlay() -> Bool](./preparetoplay%28%29.md)
  Prepares the player for audio playback.
- [func play(atTime: TimeInterval) -> Bool](./play%28attime%29.md)
  Plays audio asynchronously, starting at a specified point in the audio output device’s timeline.
- [func pause()](./pause%28%29.md)
  Pauses audio playback.
- [func stop()](./stop%28%29.md)
  Stops playback and undoes the setup the system requires for playback.
- [var isPlaying: Bool](./isplaying.md)
  A Boolean value that indicates whether the player is currently playing audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayer/play())*