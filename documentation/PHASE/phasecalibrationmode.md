# PHASECalibrationMode

**Framework**: PHASE  
**Kind**: enum  
**Role**: Enumeration

Calibration options for sound pressure level.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
enum PHASECalibrationMode
```

```c
enum PHASECalibrationMode : NSInteger;
```

## Topics

### Modes
- [PHASECalibrationMode.absoluteSpl](./phasecalibrationmode/absolutespl.md)
  A sound pressure level based on the current output device.
- [PHASECalibrationMode.none](./phasecalibrationmode/none.md)
  An option that specifies no loudness calibration.
- [PHASECalibrationMode.relativeSpl](./phasecalibrationmode/relativespl.md)
  A sound pressure level that’s tuned for the device.
### Initializers
- [init?(rawValue: Int)](./phasecalibrationmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Audio-Providing Nodes
- [class PHASESamplerNodeDefinition](./phasesamplernodedefinition.md)
  A node that plays complete audio data.
- [enum PHASEPlaybackMode](./phaseplaybackmode.md)
  Loop options for audio playback.
- [class PHASEPushStreamNodeDefinition](./phasepushstreamnodedefinition.md)
  A node that plays a sequence of audio buffers.
- [class PHASEPushStreamNode](./phasepushstreamnode.md)
  An audio stream you manage to provide a sound buffer data.
- [struct PHASEPushStreamBufferOptions](./phasepushstreambufferoptions.md)
  Options that inform PHASE of an audio-stream buffer’s playback priority.
- [class PHASEGeneratorNodeDefinition](./phasegeneratornodedefinition.md)
  A base class for nodes that provide audio data to generate sound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasecalibrationmode)*