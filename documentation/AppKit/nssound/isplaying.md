# isPlaying

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the sound is playing its audio data.

**Availability**:
- macOS

## Declaration

```swift
var isPlaying: Bool { get }
```

```objc
@property (readonly, getter=isPlaying) BOOL playing;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) when the receiver is playing its audio data.

## See Also

### Playing Sounds
- [static func beep()](./beep%28%29.md)
  Plays the system beep.
- [func pause() -> Bool](./pause%28%29.md)
  Pauses audio playback.
- [func play() -> Bool](./play%28%29.md)
  Initiates audio playback.
- [func resume() -> Bool](./resume%28%29.md)
  Resumes audio playback.
- [func stop() -> Bool](./stop%28%29.md)
  Concludes audio playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssound/isplaying)*