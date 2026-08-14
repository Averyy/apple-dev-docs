# resume()

**Framework**: AppKit  
**Kind**: method

Resumes audio playback.

**Availability**:
- macOS ?+

## Declaration

```swift
func resume() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) when playback is resumed, [`false`](https://developer.apple.com/documentation/swift/false) when playback is in progress or when an error occurred.

#### Discussion

Assumes the receiver has been previously paused by sending it [`NSSound`](nssound.md).

## See Also

- [static func beep()](nssound/beep.md)
  Plays the system beep.
- [var isPlaying: Bool](nssound/isplaying.md)
  A Boolean that indicates whether the sound is playing its audio data.
- [func pause() -> Bool](nssound/pause.md)
  Pauses audio playback.
- [func play() -> Bool](nssound/play.md)
  Initiates audio playback.
- [func stop() -> Bool](nssound/stop.md)
  Concludes audio playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssound/resume())*