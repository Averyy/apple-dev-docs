# PHASEGeneratorNodeDefinition

**Framework**: PHASE  
**Kind**: class

A base class for nodes that provide audio data to generate sound.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASEGeneratorNodeDefinition
```

#### Overview

This class encapsulates shared logic for subclasses that provide audio data to a mixer for sound output, namely [`PHASESamplerNodeDefinition`](phasesamplernodedefinition.md) and [`PHASEPushStreamNodeDefinition`](phasepushstreamnodedefinition.md).

## Topics

### Calibrating Loudness
- [func setCalibrationMode(calibrationMode: PHASECalibrationMode, level: Double)](phasegeneratornodedefinition/setcalibrationmode(calibrationmode:level:).md)
  Selects a loudness correction strategy and reference level.
- [var calibrationMode: PHASECalibrationMode](phasegeneratornodedefinition/calibrationmode.md)
  A sound pressure level strategy for loudness correction.
- [var level: Double](phasegeneratornodedefinition/level.md)
  The node’s loudness.
### Defining an Output Strategy
- [var mixerDefinition: PHASEMixerDefinition](phasegeneratornodedefinition/mixerdefinition.md)
  An object that combines audio layers for the node’s output.
### Joining a Group
- [var group: PHASEGroup?](phasegeneratornodedefinition/group.md)
  A group this node conforms to for gain and rate control.
### Controlling Audio Playback
- [var rate: Double](phasegeneratornodedefinition/rate.md)
  A playback speed for the node’s audio.
- [var rateMetaParameterDefinition: PHASENumberMetaParameterDefinition?](phasegeneratornodedefinition/ratemetaparameterdefinition.md)
  A meta parameter that dynamically changes the audio’s rate.
- [var gainMetaParameterDefinition: PHASENumberMetaParameterDefinition?](phasegeneratornodedefinition/gainmetaparameterdefinition.md)
  A meta parameter that dynamically changes the audio’s loudness.

## Relationships

### Inherits From
- [PHASESoundEventNodeDefinition](phasesoundeventnodedefinition.md)
### Inherited By
- [PHASEPullStreamNodeDefinition](phasepullstreamnodedefinition.md)
- [PHASEPushStreamNodeDefinition](phasepushstreamnodedefinition.md)
- [PHASESamplerNodeDefinition](phasesamplernodedefinition.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

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
- [enum PHASECalibrationMode](phasecalibrationmode.md)
  Calibration options for sound pressure level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasegeneratornodedefinition)*