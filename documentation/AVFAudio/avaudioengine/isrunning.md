# isRunning

**Framework**: AVFAudio  
**Kind**: property

A Boolean value that indicates whether the audio engine is running.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isRunning: Bool { get }
```

#### Discussion

The value is [`true`](https://developer.apple.com/documentation/swift/true) if the audio engine is in a running state; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [func prepare()](avaudioengine/prepare.md)
  Prepares the audio engine for starting.
- [func start() throws](avaudioengine/start.md)
  Starts the audio engine.
- [func pause()](avaudioengine/pause.md)
  Pauses the audio engine.
- [func stop()](avaudioengine/stop.md)
  Stops the audio engine and releases any previously prepared resources.
- [func reset()](avaudioengine/reset.md)
  Resets all audio nodes in the audio engine.
- [func withMusicSequence<R, E>((borrowing MusicSequence?) throws(E) -> R) throws(E) -> R](avaudioengine/withmusicsequence(_:).md)
  Provides scoped access to the AVAudioEngine’s MusicSequence


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioengine/isrunning)*