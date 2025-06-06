# AVAudioStereoMixing

**Framework**: AVFAudio  
**Kind**: protocol

A protocol that defines stereo mixing properties a mixer uses.

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
protocol AVAudioStereoMixing : NSObjectProtocol
```

#### Overview

> ❗ **Important**:  The [`AVAudioMixing`](avaudiomixing.md) protocol adopts this protocol. As a result, many classes also inherit this protocol by adopting `AVAudioMixing`.

 The [`AVAudioMixing`](avaudiomixing.md) protocol adopts this protocol. As a result, many classes also inherit this protocol by adopting `AVAudioMixing`.

## Topics

### Getting and Setting the Stereo Panning
- [var pan: Float](avaudiostereomixing/pan.md)
  The bus’s stereo pan.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [AVAudioMixing](avaudiomixing.md)
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

- [protocol AVAudio3DMixing](avaudio3dmixing.md)
  A collection of properties that define 3D mixing properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiostereomixing)*