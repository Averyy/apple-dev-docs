# AVMIDIPlayer

**Framework**: AVFAudio  
**Kind**: class

An object that plays MIDI data through a system sound module.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVMIDIPlayer
```

#### Overview

For more information about preparing your app to play audio, see [`Configuring your app for media playback`](https://developer.apple.com/documentation/AVFoundation/configuring-your-app-for-media-playback).

> ❗ **Important**:  For more advanced MIDI playback capabilities, like playing MIDI data through an external synthesizer or sampler, use [`AVAudioEngine`](avaudioengine.md) instead.

## Topics

### Creating a MIDI player
- [init(contentsOf: URL, soundBankURL: URL?) throws](avmidiplayer/init(contentsof:soundbankurl:).md)
  Creates a player to play a MIDI file with the specified soundbank.
- [init(data: Data, soundBankURL: URL?) throws](avmidiplayer/init(data:soundbankurl:).md)
  Creates a player to play MIDI data with the specified soundbank.
### Controlling playback
- [func prepareToPlay()](avmidiplayer/preparetoplay.md)
  Prepares the player to play the sequence by prerolling all events.
- [func play((() -> Void)?)](avmidiplayer/play(_:).md)
  Plays the MIDI sequence.
- [func stop()](avmidiplayer/stop.md)
  Stops playing the sequence.
- [var isPlaying: Bool](avmidiplayer/isplaying.md)
  A Boolean value that indicates whether the sequence is playing.
### Configuring playback settings
- [var rate: Float](avmidiplayer/rate.md)
  The playback rate of the player.
### Accessing player timing
- [var currentPosition: TimeInterval](avmidiplayer/currentposition.md)
  The current playback position, in seconds.
- [var duration: TimeInterval](avmidiplayer/duration.md)
  The duration, in seconds, of the currently loaded file.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVAudioPlayer](avaudioplayer.md)
  An object that plays audio data from a file or buffer.
- [class AVAudioRecorder](avaudiorecorder.md)
  An object that records audio data to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmidiplayer)*