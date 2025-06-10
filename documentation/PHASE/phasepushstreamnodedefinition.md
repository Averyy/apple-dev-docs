# PHASEPushStreamNodeDefinition

**Framework**: PHASE  
**Kind**: class

A node that plays a sequence of audio buffers.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASEPushStreamNodeDefinition
```

#### Overview

Use this node to create sound events for a piecemeal audio source, for example, an audio stream that your app accesses over the network or loads from a memory-mapped file on disk.

> **Note**:  To create a sound event for fully-loaded audio data instead, use [`PHASESamplerNodeDefinition`](phasesamplernodedefinition.md).

## Topics

### Creating a Node
- [init(mixerDefinition: PHASEMixerDefinition, format: AVAudioFormat)](phasepushstreamnodedefinition/init(mixerdefinition:format:).md)
  Creates a node definition for audio streams.
- [convenience init(mixerDefinition: PHASEMixerDefinition, format: AVAudioFormat, identifier: String)](phasepushstreamnodedefinition/init(mixerdefinition:format:identifier:).md)
  Creates a named node definition for audio streams.
### Observing the Format
- [var format: AVAudioFormat](phasepushstreamnodedefinition/format.md)
  The format of the audio stream data.
### Shaping Loudness
- [var normalize: Bool](phasepushstreamnodedefinition/normalize.md)
  An option that resizes loudness of the audio stream for consistency.

## Relationships

### Inherits From
- [PHASEGeneratorNodeDefinition](phasegeneratornodedefinition.md)
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
- [class PHASEPushStreamNode](phasepushstreamnode.md)
  An audio stream you manage to provide a sound buffer data.
- [struct PHASEPushStreamBufferOptions](phasepushstreambufferoptions.md)
  Options that inform PHASE of an audio-stream buffer’s playback priority.
- [enum PHASECalibrationMode](phasecalibrationmode.md)
  Calibration options for sound pressure level.
- [class PHASEGeneratorNodeDefinition](phasegeneratornodedefinition.md)
  A base class for nodes that provide audio data to generate sound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasepushstreamnodedefinition)*