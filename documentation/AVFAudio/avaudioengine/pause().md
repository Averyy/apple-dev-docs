# pause()

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Pauses the audio engine.

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
func pause()
```

```objc
- (void) pause;
```

## Discussion

This method stops the audio engine and the audio hardware, but doesn’t deallocate the resources for the [`prepare()`](./prepare%28%29.md) method. When your app doesn’t need to play audio, consider pausing or stopping the engine to minimize power consumption.

You resume the audio engine by invoking [`start()`](./start%28%29.md).

## See Also

### Playing audio
- [func prepare()](./prepare%28%29.md)
  Prepares the audio engine for starting.
- [func start() throws](./start%28%29.md)
  Starts the audio engine.
- [var isRunning: Bool](./isrunning.md)
  A Boolean value that indicates whether the audio engine is running.
- [func stop()](./stop%28%29.md)
  Stops the audio engine and releases any previously prepared resources.
- [func reset()](./reset%28%29.md)
  Resets all audio nodes in the audio engine.
- [func withMusicSequence<R, E>((borrowing MusicSequence?) throws(E) -> R) throws(E) -> R](./withmusicsequence%28_%29.md)
  Provides scoped access to the AVAudioEngine’s MusicSequence
- [var musicSequence: MusicSequence?](./musicsequence-1z47z.md)
- [musicSequence](./musicsequence-3u74x.md)
  The music sequence instance that you attach to the audio engine, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioengine/pause())*