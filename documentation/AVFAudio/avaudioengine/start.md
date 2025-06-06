# start()

**Framework**: AVFAudio  
**Kind**: method

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

#### Discussion

This method calls the [`prepare()`](avaudioengine/prepare().md) method if you don’t call it after invoking [`stop()`](avaudioengine/stop().md). It then starts the audio hardware through the [`AVAudioInputNode`](avaudioinputnode.md) and [`AVAudioOutputNode`](avaudiooutputnode.md) instances in the audio engine. This method throws an error when:

- There’s a problem in the structure of the graph, such as the input can’t route to an output or to a recording tap through converter nodes.
- An [`AVAudioSession`](avaudiosession.md) error occurs.
- The driver fails to start the hardware.

## See Also

- [func prepare()](avaudioengine/prepare.md)
  Prepares the audio engine for starting.
- [var isRunning: Bool](avaudioengine/isrunning.md)
  A Boolean value that indicates whether the audio engine is running.
- [func pause()](avaudioengine/pause.md)
  Pauses the audio engine.
- [func stop()](avaudioengine/stop.md)
  Stops the audio engine and releases any previously prepared resources.
- [func reset()](avaudioengine/reset.md)
  Resets all audio nodes in the audio engine.
- [var musicSequence: MusicSequence?](avaudioengine/musicsequence.md)
  The music sequence instance that you attach to the audio engine, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioengine/start())*