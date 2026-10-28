# pause()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Pauses audio playback.

**Availability**:
- macOS

## Declaration

```swift
func pause() -> Bool
```

```objc
- (BOOL) pause;
```

## Return Value

[`true`](../../Swift/true.md) when playback is paused successfully, [`false`](../../Swift/false.md) when playback is already paused or when an error occurred.

## See Also

### Playing Sounds
- [static func beep()](./beep%28%29.md)
  Plays the system beep.
- [var isPlaying: Bool](./isplaying.md)
  A Boolean that indicates whether the sound is playing its audio data.
- [func play() -> Bool](./play%28%29.md)
  Initiates audio playback.
- [func resume() -> Bool](./resume%28%29.md)
  Resumes audio playback.
- [func stop() -> Bool](./stop%28%29.md)
  Concludes audio playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssound/pause())*