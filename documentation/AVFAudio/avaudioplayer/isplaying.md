# isPlaying

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the player is currently playing audio.

**Availability**:
- iOS 2.2+
- iPadOS 2.2+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var isPlaying: Bool { get }
```

```objc
@property (readonly, getter=isPlaying) BOOL playing;
```

## See Also

### Controlling playback
- [func prepareToPlay() -> Bool](./preparetoplay%28%29.md)
  Prepares the player for audio playback.
- [func play() -> Bool](./play%28%29.md)
  Plays audio asynchronously.
- [func play(atTime: TimeInterval) -> Bool](./play%28attime%29.md)
  Plays audio asynchronously, starting at a specified point in the audio output device’s timeline.
- [func pause()](./pause%28%29.md)
  Pauses audio playback.
- [func stop()](./stop%28%29.md)
  Stops playback and undoes the setup the system requires for playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayer/isplaying)*