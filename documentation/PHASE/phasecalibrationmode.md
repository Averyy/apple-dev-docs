# PHASECalibrationMode

**Framework**: PHASE  
**Kind**: enum

Calibration options for sound pressure level.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
enum PHASECalibrationMode
```

## Topics

### Modes
- [PHASECalibrationMode.absoluteSpl](phasecalibrationmode/absolutespl.md)
  A sound pressure level based on the current output device.
- [PHASECalibrationMode.none](phasecalibrationmode/none.md)
  An option that specifies no loudness calibration.
- [PHASECalibrationMode.relativeSpl](phasecalibrationmode/relativespl.md)
  A sound pressure level that’s tuned for the device.
### Initializers
- [init?(rawValue: Int)](phasecalibrationmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class PHASESamplerNodeDefinition](phasesamplernodedefinition.md)
  A node that plays complete audio data.
- [enum PHASEPlaybackMode](phaseplaybackmode.md)
  Loop options for audio playback.
- [class PHASEPushStreamNodeDefinition](phasepushstreamnodedefinition.md)
  A node that plays a sequence of audio buffers.
- [class PHASEPushStreamNode](phasepushstreamnode.md)
  An audio stream you manage to provide a sound buffer data.
- [struct PHASEPushStreamBufferOptions](phasepushstreambufferoptions.md)
  Options that inform PHASE of an audio-stream buffer’s playback priority.
- [class PHASEGeneratorNodeDefinition](phasegeneratornodedefinition.md)
  A base class for nodes that provide audio data to generate sound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasecalibrationmode)*