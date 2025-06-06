# AVAudioSinkNode

**Framework**: AVFAudio  
**Kind**: class

An object that receives audio data.

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
class AVAudioSinkNode
```

#### Overview

You use an `AVAudioSinkNode` to receive audio data through [`AVAudioSinkNodeReceiverBlock`](avaudiosinknodereceiverblock.md). You only use it in the input chain.

An audio sink node doesn’t support format conversion. When connecting, use the output format of the input for the format for the connection. The format should match the hardware input sample rate.

The voice processing I/O unit is an exception to the above because it supports sample rate conversion. The input scope format (hardware format) and output scope format (client format) of the input node can differ in that case.

An audio sink node doesn’t support manual rendering mode, and doesn’t have an output bus, so you can’t install a tap on it.

## Topics

### Creating an Audio Sink Node
- [typealias AVAudioSinkNodeReceiverBlock](avaudiosinknodereceiverblock.md)
  A block that receives audio data from an audio sink node.
- [init(receiverBlock: AVAudioSinkNodeReceiverBlock)](avaudiosinknode/init(receiverblock:).md)
  Creates an audio sink node with a block that receives audio data.

## Relationships

### Inherits From
- [AVAudioNode](avaudionode.md)
### Conforms To
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
- [class AVAudioSourceNode](avaudiosourcenode.md)
  An object that supplies audio data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosinknode)*