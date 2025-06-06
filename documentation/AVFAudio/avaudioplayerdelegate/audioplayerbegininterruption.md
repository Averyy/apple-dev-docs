# audioPlayerBeginInterruption(_:)

**Framework**: AVFAudio  
**Kind**: method

Tells the delegate when the system interrupts the audio player’s playback.

**Availability**:
- iOS 2.2+
- iPadOS 2.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func audioPlayerBeginInterruption(_ player: AVAudioPlayer)
```

## Parameters

- `player`: The interrupted audio player.

## See Also

- [func audioPlayerEndInterruption(AVAudioPlayer)](avaudioplayerdelegate/audioplayerendinterruption(_:).md)
  Tells the delegate when the audio session interruption ends.
- [func audioPlayerEndInterruption(AVAudioPlayer, withOptions: Int)](avaudioplayerdelegate/audioplayerendinterruption(_:withoptions:).md)
  Tells the delegate when the audio session interruption ends with options.
- [func audioPlayerEndInterruption(AVAudioPlayer, withFlags: Int)](avaudioplayerdelegate/audioplayerendinterruption(_:withflags:).md)
  Tells the delegate when the audio session interruption ends with flags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayerdelegate/audioplayerbegininterruption(_:))*