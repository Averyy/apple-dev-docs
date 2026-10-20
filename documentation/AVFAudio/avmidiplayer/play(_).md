# play(_:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

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
func play(_ completionHandler: (@Sendable () -> Void)? = nil)
```

```swift
func play() async
```

```objc
- (void) play:(AVMIDIPlayerCompletionHandler) completionHandler;
```

## Parameters

- `completionHandler`: A closure the system calls when playback completes.

## Topics

### Completion handler
- [typealias AVMIDIPlayerCompletionHandler](../avmidiplayercompletionhandler.md)
  A callback the system invokes when MIDI playback completes.

## See Also

### Controlling playback
- [func prepareToPlay()](./preparetoplay%28%29.md)
  Prepares the player to play the sequence by prerolling all events.
- [typealias AVMIDIPlayerCompletionHandler](../avmidiplayercompletionhandler.md)
  A callback the system invokes when MIDI playback completes.
- [func stop()](./stop%28%29.md)
  Stops playing the sequence.
- [var isPlaying: Bool](./isplaying.md)
  A Boolean value that indicates whether the sequence is playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmidiplayer/play(_:))*