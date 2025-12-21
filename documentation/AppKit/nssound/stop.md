# stop()

**Framework**: AppKit  
**Kind**: method

Concludes audio playback.

**Availability**:
- macOS ?+

## Declaration

```swift
func stop() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) when playback is concluded successfully or if it’s paused, [`false`](https://developer.apple.com/documentation/Swift/false) otherwise.

## See Also

- [func sound(NSSound, didFinishPlaying: Bool)](nssounddelegate/sound(_:didfinishplaying:).md)
  This delegate method is called when an `NSSound` instance has completed playback of its sound data.
- [static func beep()](nssound/beep.md)
  Plays the system beep.
- [var isPlaying: Bool](nssound/isplaying.md)
  A Boolean that indicates whether the sound is playing its audio data.
- [func pause() -> Bool](nssound/pause.md)
  Pauses audio playback.
- [func play() -> Bool](nssound/play.md)
  Initiates audio playback.
- [func resume() -> Bool](nssound/resume.md)
  Resumes audio playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssound/stop())*