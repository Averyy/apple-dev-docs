# audioPlayerEndInterruption(_:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when the audio session interruption ends.

**Availability**:
- iOS 2.2+ - Deprecated in 6.0
- iPadOS 2.2+ - Deprecated in 6.0
- Mac Catalyst 2.2+ - Deprecated in 6.0
- tvOS 9.0+
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Observe audio session interruption notifications instead. See [Handling audio interruptions](../handling-audio-interruptions.md) for more information.

## Declaration

```swift
optional func audioPlayerEndInterruption(_ player: AVAudioPlayer)
```

```objc
- (void) audioPlayerEndInterruption:(AVAudioPlayer *) player;
```

## Parameters

- `player`: The audio player with the interruption that ends.

## See Also

### Responding to audio interruptions
- [func audioPlayerBeginInterruption(AVAudioPlayer)](./audioplayerbegininterruption%28_%29.md)
  Tells the delegate when the system interrupts the audio player’s playback.
- [func audioPlayerEndInterruption(AVAudioPlayer, withOptions: Int)](./audioplayerendinterruption%28_,withoptions%29.md)
  Tells the delegate when the audio session interruption ends with options.
- [func audioPlayerEndInterruption(AVAudioPlayer, withFlags: Int)](./audioplayerendinterruption%28_,withflags%29.md)
  Tells the delegate when the audio session interruption ends with flags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayerdelegate/audioplayerendinterruption(_:))*