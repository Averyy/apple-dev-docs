# audioPlayerEndInterruption(_:withOptions:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when the audio session interruption ends with options.

**Availability**:
- iOS 6.0+ - Deprecated in 8.0
- iPadOS 6.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS 9.0+
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Observe audio session interruption notifications instead. See [Handling audio interruptions](../handling-audio-interruptions.md) for more information.

## Declaration

```swift
optional func audioPlayerEndInterruption(_ player: AVAudioPlayer, withOptions flags: Int)
```

```objc
- (void) audioPlayerEndInterruption:(AVAudioPlayer *) player withOptions:(NSUInteger) flags;
```

## Parameters

- `player`: The audio player with the interruption that ends.
- `flags`: The options that indicate the state of the audio session.

## See Also

### Responding to audio interruptions
- [func audioPlayerBeginInterruption(AVAudioPlayer)](./audioplayerbegininterruption%28_%29.md)
  Tells the delegate when the system interrupts the audio player’s playback.
- [func audioPlayerEndInterruption(AVAudioPlayer)](./audioplayerendinterruption%28_%29.md)
  Tells the delegate when the audio session interruption ends.
- [func audioPlayerEndInterruption(AVAudioPlayer, withFlags: Int)](./audioplayerendinterruption%28_,withflags%29.md)
  Tells the delegate when the audio session interruption ends with flags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayerdelegate/audioplayerendinterruption(_:withoptions:))*