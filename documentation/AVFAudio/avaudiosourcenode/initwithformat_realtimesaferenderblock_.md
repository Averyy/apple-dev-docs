# initWithFormat:realtimeSafeRenderBlock:

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```objc
- (instancetype) initWithFormat:(AVAudioFormat *) format realtimeSafeRenderBlock:(AVAudioSourceNodeRenderBlockRealtimeSafe) block;
```

## Discussion

Identical to initWithFormat:renderBlock:, but requires a realtime-safe block. When the the engine is configured for realtime use (rendering to a device, or using `AVAudioEngineManualRenderingModeRealtime`) this initializer is preferred.

## See Also

### Creating an audio source node
- [typealias AVAudioSourceNodeRenderBlock](../avaudiosourcenoderenderblock.md)
  A block that supplies audio data to an audio source node.
- [init(renderBlock: AVAudioSourceNodeRenderBlock)](./init%28renderblock%29.md)
  Creates an audio source node with a block that supplies audio data.
- [init(format: AVAudioFormat, renderBlock: AVAudioSourceNodeRenderBlock)](./init%28format,renderblock%29.md)
  Creates an audio source node with the audio format and a block that supplies audio data.
- [- initWithRealtimeSafeRenderBlock:](./initwithrealtimesaferenderblock_.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosourcenode/initwithformat:realtimesaferenderblock:)*