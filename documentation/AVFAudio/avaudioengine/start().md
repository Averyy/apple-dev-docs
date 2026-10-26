# start()

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Starts the audio engine.

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
func start() throws
```

```objc
- (BOOL) startAndReturnError:(NSError **) outError;
```

#### Discussion

This method calls the [`prepare()`](./prepare%28%29.md) method if you don’t call it after invoking [`stop()`](./stop%28%29.md). It then starts the audio hardware through the [`AVAudioInputNode`](../avaudioinputnode.md) and [`AVAudioOutputNode`](../avaudiooutputnode.md) instances in the audio engine. This method throws an error when:

- There’s a problem in the structure of the graph, such as the input can’t route to an output or to a recording tap through converter nodes.
- An [`AVAudioSession`](../avaudiosession.md) error occurs.
- The driver fails to start the hardware.

## See Also

### Playing audio
- [func prepare()](./prepare%28%29.md)
  Prepares the audio engine for starting.
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
- [musicSequence](./musicsequence-3u74x.md)
  The music sequence instance that you attach to the audio engine, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioengine/start())*