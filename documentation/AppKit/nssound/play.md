# play()

**Framework**: AppKit  
**Kind**: method

Initiates audio playback.

**Availability**:
- macOS ?+

## Declaration

```swift
func play() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) when playback is initiated, [`false`](https://developer.apple.com/documentation/Swift/false) when playback is already in progress or when an error occurred.

#### Discussion

This method initiates playback asynchronously and returns control to your application. Therefore, your application can continue doing work while the audio is playing.

## See Also

- [static func beep()](nssound/beep.md)
  Plays the system beep.
- [var isPlaying: Bool](nssound/isplaying.md)
  A Boolean that indicates whether the sound is playing its audio data.
- [func pause() -> Bool](nssound/pause.md)
  Pauses audio playback.
- [func resume() -> Bool](nssound/resume.md)
  Resumes audio playback.
- [func stop() -> Bool](nssound/stop.md)
  Concludes audio playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssound/play())*