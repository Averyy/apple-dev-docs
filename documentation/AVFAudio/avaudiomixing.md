# AVAudioMixing

**Framework**: AVFAudio  
**Kind**: protocol

A collection of properties that are applicable to the input bus of a mixer node.

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
protocol AVAudioMixing : AVAudio3DMixing, AVAudioStereoMixing
```

#### Overview

Nodes that conform to the `AVAudioMixing` protocol can talk to a mixer node downstream. This is specific to the classes [`AVAudioMixerNode`](avaudiomixernode.md) and [`AVAudioEnvironmentNode`](avaudioenvironmentnode.md). Effect nodes can’t talk to their downstream mixer.

When connecting a source node, the properties that this protocol defines apply to the respective input bus of the mixer.

You can change the state of properties before connecting a source node to the mixer. The system caches your changes and applies them upon connection. It caches the properties again after disconnection.

Source nodes maintain mixing settings when switching between different mixers. For example, an [`AVAudioPlayerNode`](avaudioplayernode.md), in a gaming scenario, can set up 3D mixing settings and then move from one environment to another.

> ❗ **Important**:  Several classes adopt the `AVAudioMixing` protocol. The protocol itself conforms to [`AVAudio3DMixing`](avaudio3dmixing.md) and [`AVAudioStereoMixing`](avaudiostereomixing.md). Classes that conform to `AVAudioMixing` also conform to those protocols.

 Several classes adopt the `AVAudioMixing` protocol. The protocol itself conforms to [`AVAudio3DMixing`](avaudio3dmixing.md) and [`AVAudioStereoMixing`](avaudiostereomixing.md). Classes that conform to `AVAudioMixing` also conform to those protocols.

## Topics

### Defining Mixing Properties
- [protocol AVAudioStereoMixing](avaudiostereomixing.md)
  A protocol that defines stereo mixing properties a mixer uses.
- [protocol AVAudio3DMixing](avaudio3dmixing.md)
  A collection of properties that define 3D mixing properties.
### Getting and Setting the Destination
- [class AVAudioMixingDestination](avaudiomixingdestination.md)
  An object that represents a connection to a mixer node from a node that conforms to the audio mixing protocol.
- [func destination(forMixer: AVAudioNode, bus: AVAudioNodeBus) -> AVAudioMixingDestination?](avaudiomixing/destination(formixer:bus:).md)
  Gets the audio mixing destination object that corresponds to the specified mixer node and input bus.
### Getting and Setting the Bus Volume
- [var volume: Float](avaudiomixing/volume.md)
  The bus’s input volume.

## Relationships

### Inherits From
- [AVAudio3DMixing](avaudio3dmixing.md)
- [AVAudioStereoMixing](avaudiostereomixing.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [AVAudioEnvironmentNode](avaudioenvironmentnode.md)
- [AVAudioInputNode](avaudioinputnode.md)
- [AVAudioMixerNode](avaudiomixernode.md)
- [AVAudioMixingDestination](avaudiomixingdestination.md)
- [AVAudioPlayerNode](avaudioplayernode.md)
- [AVAudioSourceNode](avaudiosourcenode.md)
- [AVAudioUnitGenerator](avaudiounitgenerator.md)
- [AVAudioUnitMIDIInstrument](avaudiounitmidiinstrument.md)
- [AVAudioUnitSampler](avaudiounitsampler.md)

## See Also

- [class AVAudioMixerNode](avaudiomixernode.md)
  An object that takes any number of inputs and converts them into a single output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiomixing)*