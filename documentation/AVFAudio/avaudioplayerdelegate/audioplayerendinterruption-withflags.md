# audioPlayerEndInterruption(_:withFlags:)

**Framework**: AVFAudio  
**Kind**: method

Tells the delegate when the audio session interruption ends with flags.

**Availability**:
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func audioPlayerEndInterruption(_ player: AVAudioPlayer, withFlags flags: Int)
```

## Parameters

- `player`: The audio player with the interruption that ends.
- `flags`: The flags that indicate the state of the audio session.

## See Also

- [func audioPlayerBeginInterruption(AVAudioPlayer)](avaudioplayerdelegate/audioplayerbegininterruption(_:).md)
  Tells the delegate when the system interrupts the audio player’s playback.
- [func audioPlayerEndInterruption(AVAudioPlayer)](avaudioplayerdelegate/audioplayerendinterruption(_:).md)
  Tells the delegate when the audio session interruption ends.
- [func audioPlayerEndInterruption(AVAudioPlayer, withOptions: Int)](avaudioplayerdelegate/audioplayerendinterruption(_:withoptions:).md)
  Tells the delegate when the audio session interruption ends with options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayerdelegate/audioplayerendinterruption(_:withflags:))*