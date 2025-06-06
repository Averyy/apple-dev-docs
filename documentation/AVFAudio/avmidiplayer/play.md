# play(_:)

**Framework**: AVFAudio  
**Kind**: method

Plays the MIDI sequence.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func play() async
```

## Parameters

- `completionHandler`: A closure the system calls when playback completes.

## Topics

### Closures
- [typealias AVMIDIPlayerCompletionHandler](avmidiplayercompletionhandler.md)
  A callback the system invokes when MIDI playback completes.

## See Also

- [func prepareToPlay()](avmidiplayer/preparetoplay.md)
  Prepares the player to play the sequence by prerolling all events.
- [func stop()](avmidiplayer/stop.md)
  Stops playing the sequence.
- [var isPlaying: Bool](avmidiplayer/isplaying.md)
  A Boolean value that indicates whether the sequence is playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmidiplayer/play(_:))*