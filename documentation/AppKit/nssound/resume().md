# resume()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Resumes audio playback.

**Availability**:
- macOS

## Declaration

```swift
func resume() -> Bool
```

```objc
- (BOOL) resume;
```

## Return Value

[`true`](../../Swift/true.md) when playback is resumed, [`false`](../../Swift/false.md) when playback is in progress or when an error occurred.

## Discussion

Assumes the receiver has been previously paused by sending it [`NSSound`](../nssound.md).

## See Also

### Playing Sounds
- [static func beep()](./beep%28%29.md)
  Plays the system beep.
- [var isPlaying: Bool](./isplaying.md)
  A Boolean that indicates whether the sound is playing its audio data.
- [func pause() -> Bool](./pause%28%29.md)
  Pauses audio playback.
- [func play() -> Bool](./play%28%29.md)
  Initiates audio playback.
- [func stop() -> Bool](./stop%28%29.md)
  Concludes audio playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssound/resume())*