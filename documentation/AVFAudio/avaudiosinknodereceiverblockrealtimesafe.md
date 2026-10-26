# AVAudioSinkNodeReceiverBlockRealtimeSafe

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
typedef int (^)(const struct AudioTimeStamp *, unsigned int, const struct AudioBufferList *) __attribute__((nonblocking)) AVAudioSinkNodeReceiverBlockRealtimeSafe;
```

#### Discussion

Identical to AVAudioSinkNodeReceiverBlock, with the addition of a realtime-safety guarantee.

## See Also

### Custom and offline rendering
- [Building a signal generator](./building-a-signal-generator.md)
  Generate audio signals using an audio source node and a custom render callback.
- [Performing offline audio processing](./performing-offline-audio-processing.md)
  Add offline audio processing features to your app by enabling offline manual rendering mode.
- [class AVAudioSourceNode](./avaudiosourcenode.md)
  An object that supplies audio data.
- [AVAudioSourceNodeRenderBlockRealtimeSafe](./avaudiosourcenoderenderblockrealtimesafe.md)
- [class AVAudioSinkNode](./avaudiosinknode.md)
  An object that receives audio data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosinknodereceiverblockrealtimesafe)*