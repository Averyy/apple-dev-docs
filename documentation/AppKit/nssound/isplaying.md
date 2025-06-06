# isPlaying

**Framework**: AppKit  
**Kind**: property

A Boolean that indicates whether the sound is playing its audio data.

**Availability**:
- macOS ?+

## Declaration

```swift
var isPlaying: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) when the receiver is playing its audio data.

## See Also

- [static func beep()](nssound/beep.md)
  Plays the system beep.
- [func pause() -> Bool](nssound/pause.md)
  Pauses audio playback.
- [func play() -> Bool](nssound/play.md)
  Initiates audio playback.
- [func resume() -> Bool](nssound/resume.md)
  Resumes audio playback.
- [func stop() -> Bool](nssound/stop.md)
  Concludes audio playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssound/isplaying)*