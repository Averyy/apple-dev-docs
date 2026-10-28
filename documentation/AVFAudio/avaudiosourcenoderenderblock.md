# AVAudioSourceNodeRenderBlock

**Framework**: AVFAudio  
**Kind**: typealias  
**Role**: Type Alias

A block that supplies audio data to an audio source node.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
typealias AVAudioSourceNodeRenderBlock = (UnsafeMutablePointer<ObjCBool>, UnsafePointer<AudioTimeStamp>, AVAudioFrameCount, UnsafeMutablePointer<AudioBufferList>) -> OSStatus
```

```c
typedef int (^)(_Bool *, const struct AudioTimeStamp *, unsigned int, struct AudioBufferList *) AVAudioSourceNodeRenderBlock;
```

## Return Value

An `OSStatus` result code. When returning an error, consider the audio data invalid.

## Parameters

- `isSilence`: The Boolean value that indicates whether the buffer contains only silence.
- `timestamp`: The HAL time the audio data renders.
- `frameCount`: The number of sample frames of audio data the engine requests.
- `outputData`: The output data.

## See Also

### Creating an audio source node
- [init(renderBlock: AVAudioSourceNodeRenderBlock)](./avaudiosourcenode/init%28renderblock%29.md)
  Creates an audio source node with a block that supplies audio data.
- [init(format: AVAudioFormat, renderBlock: AVAudioSourceNodeRenderBlock)](./avaudiosourcenode/init%28format,renderblock%29.md)
  Creates an audio source node with the audio format and a block that supplies audio data.
- [- initWithRealtimeSafeRenderBlock:](./avaudiosourcenode/initwithrealtimesaferenderblock_.md)
- [- initWithFormat:realtimeSafeRenderBlock:](./avaudiosourcenode/initwithformat_realtimesaferenderblock_.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosourcenoderenderblock)*