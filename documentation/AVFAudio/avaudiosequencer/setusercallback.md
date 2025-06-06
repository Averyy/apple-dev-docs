# setUserCallback(_:)

**Framework**: AVFAudio  
**Kind**: method

Adds a callback that the sequencer calls each time it encounters a user event during playback.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func setUserCallback(_ userCallback: AVAudioSequencerUserCallback?)
```

#### Discussion

The system calls the same callback for events that occur on any track in the sequencer. Set the callback to `nil` to disable it.

## Parameters

- `userCallback`: The user callback that the system calls.

## See Also

- [typealias AVAudioSequencerUserCallback](avaudiosequencerusercallback.md)
  A callback the sequencer calls asynchronously during playback when it encounters a user event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosequencer/setusercallback(_:))*