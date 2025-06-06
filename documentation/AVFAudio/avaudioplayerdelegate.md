# AVAudioPlayerDelegate

**Framework**: AVFAudio  
**Kind**: protocol

A protocol that defines the methods to respond to audio playback events and decoding errors.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS 3.0+

## Declaration

```swift
protocol AVAudioPlayerDelegate : NSObjectProtocol
```

#### Overview

All of the methods in this protocol are optional.

## Topics

### Responding to Playback Completion
- [func audioPlayerDidFinishPlaying(AVAudioPlayer, successfully: Bool)](avaudioplayerdelegate/audioplayerdidfinishplaying(_:successfully:).md)
  Tells the delegate when the audio finishes playing.
### Responding to Audio Decoding Errors
- [func audioPlayerDecodeErrorDidOccur(AVAudioPlayer, error: (any Error)?)](avaudioplayerdelegate/audioplayerdecodeerrordidoccur(_:error:).md)
  Tells the delegate when an audio player encounters a decoding error during playback.
### Responding to Audio Interruptions
- [func audioPlayerBeginInterruption(AVAudioPlayer)](avaudioplayerdelegate/audioplayerbegininterruption(_:).md)
  Tells the delegate when the system interrupts the audio player’s playback.
- [func audioPlayerEndInterruption(AVAudioPlayer)](avaudioplayerdelegate/audioplayerendinterruption(_:).md)
  Tells the delegate when the audio session interruption ends.
- [func audioPlayerEndInterruption(AVAudioPlayer, withOptions: Int)](avaudioplayerdelegate/audioplayerendinterruption(_:withoptions:).md)
  Tells the delegate when the audio session interruption ends with options.
- [func audioPlayerEndInterruption(AVAudioPlayer, withFlags: Int)](avaudioplayerdelegate/audioplayerendinterruption(_:withflags:).md)
  Tells the delegate when the audio session interruption ends with flags.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any AVAudioPlayerDelegate)?](avaudioplayer/delegate.md)
  The delegate object for the audio player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayerdelegate)*