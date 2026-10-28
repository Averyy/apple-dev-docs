# play()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Initiates audio playback.

**Availability**:
- macOS

## Declaration

```swift
func play() -> Bool
```

```objc
- (BOOL) play;
```

## Return Value

[`true`](../../Swift/true.md) when playback is initiated, [`false`](../../Swift/false.md) when playback is already in progress or when an error occurred.

## Discussion

This method initiates playback asynchronously and returns control to your application. Therefore, your application can continue doing work while the audio is playing.

## See Also

### Playing Sounds
- [static func beep()](./beep%28%29.md)
  Plays the system beep.
- [var isPlaying: Bool](./isplaying.md)
  A Boolean that indicates whether the sound is playing its audio data.
- [func pause() -> Bool](./pause%28%29.md)
  Pauses audio playback.
- [func resume() -> Bool](./resume%28%29.md)
  Resumes audio playback.
- [func stop() -> Bool](./stop%28%29.md)
  Concludes audio playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssound/play())*