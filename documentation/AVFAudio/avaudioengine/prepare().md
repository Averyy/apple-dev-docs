# prepare()

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Prepares the audio engine for starting.

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
func prepare()
```

```objc
- (void) prepare;
```

#### Discussion

This method preallocates many resources the audio engine requires to start. Use it to responsively start audio input or output.

## See Also

### Playing audio
- [func start() throws](./start%28%29.md)
  Starts the audio engine.
- [var isRunning: Bool](./isrunning.md)
  A Boolean value that indicates whether the audio engine is running.
- [func pause()](./pause%28%29.md)
  Pauses the audio engine.
- [func stop()](./stop%28%29.md)
  Stops the audio engine and releases any previously prepared resources.
- [func reset()](./reset%28%29.md)
  Resets all audio nodes in the audio engine.
- [func withMusicSequence<R, E>((borrowing MusicSequence?) throws(E) -> R) throws(E) -> R](./withmusicsequence%28_%29.md)
  Provides scoped access to the AVAudioEngine’s MusicSequence
- [var musicSequence: MusicSequence?](./musicsequence-1z47z.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioengine/prepare())*