# stop()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Concludes audio playback.

**Availability**:
- macOS

## Declaration

```swift
func stop() -> Bool
```

```objc
- (BOOL) stop;
```

#### Return Value

[`true`](../../Swift/true.md) when playback is concluded successfully or if it’s paused, [`false`](../../Swift/false.md) otherwise.

## See Also

### Related Documentation
- [func sound(NSSound, didFinishPlaying: Bool)](../nssounddelegate/sound%28_,didfinishplaying%29.md)
  This delegate method is called when an `NSSound` instance has completed playback of its sound data.
### Playing Sounds
- [static func beep()](./beep%28%29.md)
  Plays the system beep.
- [var isPlaying: Bool](./isplaying.md)
  A Boolean that indicates whether the sound is playing its audio data.
- [func pause() -> Bool](./pause%28%29.md)
  Pauses audio playback.
- [func play() -> Bool](./play%28%29.md)
  Initiates audio playback.
- [func resume() -> Bool](./resume%28%29.md)
  Resumes audio playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssound/stop())*