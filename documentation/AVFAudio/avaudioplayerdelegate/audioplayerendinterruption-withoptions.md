# audioPlayerEndInterruption(_:withOptions:)

**Framework**: AVFAudio  
**Kind**: method

Tells the delegate when the audio session interruption ends with options.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func audioPlayerEndInterruption(_ player: AVAudioPlayer, withOptions flags: Int)
```

## Parameters

- `player`: The audio player with the interruption that ends.
- `flags`: The options that indicate the state of the audio session.

## See Also

- [func audioPlayerBeginInterruption(AVAudioPlayer)](avaudioplayerdelegate/audioplayerbegininterruption(_:).md)
  Tells the delegate when the system interrupts the audio player’s playback.
- [func audioPlayerEndInterruption(AVAudioPlayer)](avaudioplayerdelegate/audioplayerendinterruption(_:).md)
  Tells the delegate when the audio session interruption ends.
- [func audioPlayerEndInterruption(AVAudioPlayer, withFlags: Int)](avaudioplayerdelegate/audioplayerendinterruption(_:withflags:).md)
  Tells the delegate when the audio session interruption ends with flags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayerdelegate/audioplayerendinterruption(_:withoptions:))*