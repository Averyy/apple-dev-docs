# AVAudioSourceNode

**Framework**: AVFAudio  
**Kind**: class

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

#### Overview

The `AVAudioSourceNode` class allows for supplying audio data for rendering through [`AVAudioSourceNodeRenderBlock`](avaudiosourcenoderenderblock.md). It’s a convenient method for delievering audio data instead of setting the input callback on an audio unit with `kAudioUnitProperty_SetRenderCallback`.

## Topics

### Creating an Audio Source Node
- [typealias AVAudioSourceNodeRenderBlock](avaudiosourcenoderenderblock.md)
  A block that supplies audio data to an audio source node.
- [init(renderBlock: AVAudioSourceNodeRenderBlock)](avaudiosourcenode/init(renderblock:).md)
  Creates an audio source node with a block that supplies audio data.
- [init(format: AVAudioFormat, renderBlock: AVAudioSourceNodeRenderBlock)](avaudiosourcenode/init(format:renderblock:).md)
  Creates an audio source node with the audio format and a block that supplies audio data.

## Relationships

### Inherits From
- [AVAudioNode](avaudionode.md)
### Conforms To
- [AVAudio3DMixing](avaudio3dmixing.md)
- [AVAudioMixing](avaudiomixing.md)
- [AVAudioStereoMixing](avaudiostereomixing.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Building a signal generator](building-a-signal-generator.md)
  Use an audio source node and a custom render callback to generate audio signals.
- [Performing offline audio processing](performing-offline-audio-processing.md)
  Add offline audio processing features to your app by enabling offline manual rendering mode.
- [class AVAudioSinkNode](avaudiosinknode.md)
  An object that receives audio data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosourcenode)*