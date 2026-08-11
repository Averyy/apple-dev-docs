# audioPlayerEndInterruption(_:)

**Framework**: AVFAudio  
**Kind**: method

Tells the delegate when the audio session interruption ends.

**Availability**:
- iOS 2.2+
- iPadOS 2.2+
- Mac Catalyst 2.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func audioPlayerEndInterruption(_ player: AVAudioPlayer)
```

## Parameters

- `player`: The audio player with the interruption that ends.

## See Also

- [func audioPlayerBeginInterruption(AVAudioPlayer)](avaudioplayerdelegate/audioplayerbegininterruption(_:).md)
  Tells the delegate when the system interrupts the audio player’s playback.
- [func audioPlayerEndInterruption(AVAudioPlayer, withOptions: Int)](avaudioplayerdelegate/audioplayerendinterruption(_:withoptions:).md)
  Tells the delegate when the audio session interruption ends with options.
- [func audioPlayerEndInterruption(AVAudioPlayer, withFlags: Int)](avaudioplayerdelegate/audioplayerendinterruption(_:withflags:).md)
  Tells the delegate when the audio session interruption ends with flags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayerdelegate/audioplayerendinterruption(_:))*