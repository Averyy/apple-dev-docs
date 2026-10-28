# AVAudioIONodeInputBlockRealtimeSafe

**Framework**: AVFAudio  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```c
typedef const struct AudioBufferList *(^)(unsigned int) __attribute__((nonblocking)) AVAudioIONodeInputBlockRealtimeSafe;
```

## Discussion

Identical to AVAudioIONodeInputBlock, with the addition of a realtime-safety guarantee. When the engine is configured to operate in `AVAudioEngineManualRenderingModeRealtime`, use of this block is preferred.

## See Also

### Engine and nodes
- [Using voice processing](./using-voice-processing.md)
  Add voice-processing capabilities to your app by using audio engine.
- [class AVAudioEngine](./avaudioengine.md)
  An object that manages a graph of audio nodes, controls playback, and configures real-time rendering constraints.
- [class AVAudioInputNode](./avaudioinputnode.md)
  An object that connects to the system’s audio input.
- [class AVAudioOutputNode](./avaudiooutputnode.md)
  An object that connects to the system’s audio output.
- [class AVAudioIONode](./avaudioionode.md)
  An object that performs audio input or output in the engine.
- [class AVAudioNode](./avaudionode.md)
  An object you use for audio generation, processing, or an I/O block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioionodeinputblockrealtimesafe)*