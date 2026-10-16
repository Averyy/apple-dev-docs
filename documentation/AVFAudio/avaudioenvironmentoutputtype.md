# AVAudioEnvironmentOutputType

**Framework**: AVFAudio  
**Kind**: enum

The output types for using with the automatic 3D mixing rendering algorithm.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
enum AVAudioEnvironmentOutputType
```

#### Overview

The output type determines the rendering method for any input bus using [`AVAudio3DMixingRenderingAlgorithm.auto`](avaudio3dmixingrenderingalgorithm/auto.md). To configure the output type, set [`outputType`](avaudioenvironmentnode/outputtype.md) on [`AVAudioEnvironmentNode`](avaudioenvironmentnode.md).

## Topics

### Creating an output type
- [init?(rawValue: Int)](avaudioenvironmentoutputtype/init(rawvalue:).md)
### Choosing an output type
- [AVAudioEnvironmentOutputType.auto](avaudioenvironmentoutputtype/auto.md)
  Automatically detects the playback route and picks the correct output.
- [AVAudioEnvironmentOutputType.headphones](avaudioenvironmentoutputtype/headphones.md)
  Renders the audio output for headphones.
- [AVAudioEnvironmentOutputType.builtInSpeakers](avaudioenvironmentoutputtype/builtinspeakers.md)
  Renders the audio output for built-in speakers on the current hardware.
- [AVAudioEnvironmentOutputType.externalSpeakers](avaudioenvironmentoutputtype/externalspeakers.md)
  Renders the audio output for external speakers according to the audio environment node’s output channel layout.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var outputVolume: Float](avaudioenvironmentnode/outputvolume.md)
  The mixer’s output volume.
- [var outputType: AVAudioEnvironmentOutputType](avaudioenvironmentnode/outputtype.md)
  The type of output hardware.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioenvironmentoutputtype)*