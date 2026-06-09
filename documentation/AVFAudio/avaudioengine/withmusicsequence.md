# withMusicSequence(_:)

**Framework**: AVFAudio  
**Kind**: method

Provides scoped access to the AVAudioEngine’s MusicSequence

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func withMusicSequence<R, E>(_ body: (borrowing MusicSequence?) throws(E) -> R) throws(E) -> R where E : Error
```

#### Return Value

The value returned by the closure

#### Discussion

This method provides thread-safe, scoped access to the MusicSequence. The MusicSequence reference is only valid within the closure and must not be retained or accessed outside of it.

> **Note**: Rethrows any error thrown by the closure

## Parameters

- `body`: A closure that receives a MusicSequence

## See Also

- [func prepare()](avaudioengine/prepare.md)
  Prepares the audio engine for starting.
- [func start() throws](avaudioengine/start.md)
  Starts the audio engine.
- [var isRunning: Bool](avaudioengine/isrunning.md)
  A Boolean value that indicates whether the audio engine is running.
- [func pause()](avaudioengine/pause.md)
  Pauses the audio engine.
- [func stop()](avaudioengine/stop.md)
  Stops the audio engine and releases any previously prepared resources.
- [func reset()](avaudioengine/reset.md)
  Resets all audio nodes in the audio engine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioengine/withmusicsequence(_:))*