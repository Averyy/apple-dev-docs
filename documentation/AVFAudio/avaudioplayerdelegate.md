# AVAudioPlayerDelegate

**Framework**: AVFAudio  
**Kind**: protocol  
**Role**: Protocol

A protocol that defines the methods to respond to audio playback events and decoding errors.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
@MainActor
protocol AVAudioPlayerDelegate : NSObjectProtocol
```

```objc
@protocol AVAudioPlayerDelegate <NSObject>
```

#### Overview

All of the methods in this protocol are optional.

## Topics

### Responding to playback completion
- [func audioPlayerDidFinishPlaying(AVAudioPlayer, successfully: Bool)](./avaudioplayerdelegate/audioplayerdidfinishplaying%28_,successfully%29.md)
  Tells the delegate when the audio finishes playing.
### Responding to audio decoding errors
- [func audioPlayerDecodeErrorDidOccur(AVAudioPlayer, error: (any Error)?)](./avaudioplayerdelegate/audioplayerdecodeerrordidoccur%28_,error%29.md)
  Tells the delegate when an audio player encounters a decoding error during playback.
### Responding to audio interruptions
- [func audioPlayerBeginInterruption(AVAudioPlayer)](./avaudioplayerdelegate/audioplayerbegininterruption%28_%29.md)
  Tells the delegate when the system interrupts the audio player’s playback.
- [func audioPlayerEndInterruption(AVAudioPlayer)](./avaudioplayerdelegate/audioplayerendinterruption%28_%29.md)
  Tells the delegate when the audio session interruption ends.
- [func audioPlayerEndInterruption(AVAudioPlayer, withOptions: Int)](./avaudioplayerdelegate/audioplayerendinterruption%28_,withoptions%29.md)
  Tells the delegate when the audio session interruption ends with options.
- [func audioPlayerEndInterruption(AVAudioPlayer, withFlags: Int)](./avaudioplayerdelegate/audioplayerendinterruption%28_,withflags%29.md)
  Tells the delegate when the audio session interruption ends with flags.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Responding to player events
- [var delegate: (any AVAudioPlayerDelegate)?](./avaudioplayer/delegate.md)
  The delegate object for the audio player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayerdelegate)*