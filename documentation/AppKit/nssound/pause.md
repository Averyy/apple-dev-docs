# pause()

**Framework**: AppKit  
**Kind**: method

Pauses audio playback.

**Availability**:
- macOS ?+

## Declaration

```swift
func pause() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) when playback is paused successfully, [`false`](https://developer.apple.com/documentation/swift/false) when playback is already paused or when an error occurred.

## See Also

- [static func beep()](nssound/beep.md)
  Plays the system beep.
- [var isPlaying: Bool](nssound/isplaying.md)
  A Boolean that indicates whether the sound is playing its audio data.
- [func play() -> Bool](nssound/play.md)
  Initiates audio playback.
- [func resume() -> Bool](nssound/resume.md)
  Resumes audio playback.
- [func stop() -> Bool](nssound/stop.md)
  Concludes audio playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssound/pause())*