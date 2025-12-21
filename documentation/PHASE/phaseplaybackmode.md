# PHASEPlaybackMode

**Framework**: PHASE  
**Kind**: enum

Loop options for audio playback.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum PHASEPlaybackMode
```

#### Overview

This class defines the options for a sampler node’s [`playbackMode`](phasesamplernodedefinition/playbackmode.md). These options control whether the node’s sound event automatically plays back its audio asset from the beginning after finishing.

## Topics

### Playback Modes
- [PHASEPlaybackMode.oneShot](phaseplaybackmode/oneshot.md)
  An option that plays a sound only once.
- [PHASEPlaybackMode.looping](phaseplaybackmode/looping.md)
  An option that restarts a sound from the begining after it finishes.
### Initializers
- [init?(rawValue: Int)](phaseplaybackmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class PHASESamplerNodeDefinition](phasesamplernodedefinition.md)
  A node that plays complete audio data.
- [class PHASEPushStreamNodeDefinition](phasepushstreamnodedefinition.md)
  A node that plays a sequence of audio buffers.
- [class PHASEPushStreamNode](phasepushstreamnode.md)
  An audio stream you manage to provide a sound buffer data.
- [struct PHASEPushStreamBufferOptions](phasepushstreambufferoptions.md)
  Options that inform PHASE of an audio-stream buffer’s playback priority.
- [enum PHASECalibrationMode](phasecalibrationmode.md)
  Calibration options for sound pressure level.
- [class PHASEGeneratorNodeDefinition](phasegeneratornodedefinition.md)
  A base class for nodes that provide audio data to generate sound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseplaybackmode)*