# AVAudioSourceNode

**Framework**: AVFAudio  
**Kind**: class  
**Role**: Class

An object that supplies audio data.

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
class AVAudioSourceNode
```

```objc
@interface AVAudioSourceNode : AVAudioNode
```

#### Overview

The `AVAudioSourceNode` class allows for supplying audio data for rendering through [`AVAudioSourceNodeRenderBlock`](./avaudiosourcenoderenderblock.md). It’s a convenient method for delievering audio data instead of setting the input callback on an audio unit with `kAudioUnitProperty_SetRenderCallback`.

## Topics

### Creating an audio source node
- [typealias AVAudioSourceNodeRenderBlock](./avaudiosourcenoderenderblock.md)
  A block that supplies audio data to an audio source node.
- [init(renderBlock: AVAudioSourceNodeRenderBlock)](./avaudiosourcenode/init%28renderblock%29.md)
  Creates an audio source node with a block that supplies audio data.
- [init(format: AVAudioFormat, renderBlock: AVAudioSourceNodeRenderBlock)](./avaudiosourcenode/init%28format,renderblock%29.md)
  Creates an audio source node with the audio format and a block that supplies audio data.
- [- initWithRealtimeSafeRenderBlock:](./avaudiosourcenode/initwithrealtimesaferenderblock_.md)
- [- initWithFormat:realtimeSafeRenderBlock:](./avaudiosourcenode/initwithformat_realtimesaferenderblock_.md)

## Relationships

### Inherits From
- [AVAudioNode](./avaudionode.md)
### Conforms To
- [AVAudio3DMixing](./avaudio3dmixing.md)
- [AVAudioMixing](./avaudiomixing.md)
- [AVAudioStereoMixing](./avaudiostereomixing.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Custom and offline rendering
- [Building a signal generator](./building-a-signal-generator.md)
  Generate audio signals using an audio source node and a custom render callback.
- [Performing offline audio processing](./performing-offline-audio-processing.md)
  Add offline audio processing features to your app by enabling offline manual rendering mode.
- [class AVAudioSinkNode](./avaudiosinknode.md)
  An object that receives audio data.
- [AVAudioSourceNodeRenderBlockRealtimeSafe](./avaudiosourcenoderenderblockrealtimesafe.md)
- [AVAudioSinkNodeReceiverBlockRealtimeSafe](./avaudiosinknodereceiverblockrealtimesafe.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosourcenode)*