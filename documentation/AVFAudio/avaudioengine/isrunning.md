# isRunning

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, getter=isRunning) BOOL running;
```

#### Discussion

The value is [`true`](../../Swift/true.md) if the audio engine is in a running state; otherwise, [`false`](../../Swift/false.md).

## See Also

### Playing audio
- [func prepare()](./prepare%28%29.md)
  Prepares the audio engine for starting.
- [func start() throws](./start%28%29.md)
  Starts the audio engine.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioengine/isrunning)*