# stop()

**Framework**: AVFAudio  
**Kind**: method

Stops the audio engine and releases any previously prepared resources.

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
func stop()
```

#### Discussion

This method stops the audio engine and the audio hardware, and releases any allocated resources for the [`prepare()`](avaudioengine/prepare().md) method. When your app doesn’t need to play audio, consider pausing or stopping the engine to minimize power consumption.

## See Also

- [func prepare()](avaudioengine/prepare.md)
  Prepares the audio engine for starting.
- [func start() throws](avaudioengine/start.md)
  Starts the audio engine.
- [var isRunning: Bool](avaudioengine/isrunning.md)
  A Boolean value that indicates whether the audio engine is running.
- [func pause()](avaudioengine/pause.md)
  Pauses the audio engine.
- [func reset()](avaudioengine/reset.md)
  Resets all audio nodes in the audio engine.
- [var musicSequence: MusicSequence?](avaudioengine/musicsequence.md)
  The music sequence instance that you attach to the audio engine, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioengine/stop())*