# PHASESamplerNodeDefinition

**Framework**: PHASE  
**Kind**: class  
**Role**: Class

A node that plays complete audio data.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASESamplerNodeDefinition
```

```objc
@interface PHASESamplerNodeDefinition : PHASEGeneratorNodeDefinition
```

#### Overview

Generate sound events from this node to play audio data that your app loads completely, either from disk or from memory.

## Topics

### Creating a Sampler Node
- [init(soundAssetIdentifier: String, mixerDefinition: PHASEMixerDefinition)](./phasesamplernodedefinition/init%28soundassetidentifier,mixerdefinition%29.md)
  Creates a sampler node with the given sound asset and mixer.
- [convenience init(soundAssetIdentifier: String, mixerDefinition: PHASEMixerDefinition, identifier: String)](./phasesamplernodedefinition/init%28soundassetidentifier,mixerdefinition,identifier%29.md)
  Creates a named sampler node with the given sound asset and mixer.
### Identifying the Audio
- [var assetIdentifier: String](./phasesamplernodedefinition/assetidentifier.md)
  The name of the audio this node plays.
### Defining Cull Behavior
- [var cullOption: PHASECullOption](./phasesamplernodedefinition/culloption.md)
  The action the engine performs after it temporarily removes the node’s sound from the audio output.
- [enum PHASECullOption](./phaseculloption.md)
  The actions the engine takes when it culls sound.
### Looping the Audio
- [var playbackMode: PHASEPlaybackMode](./phasesamplernodedefinition/playbackmode.md)
  An option that determines whether the node’s audio plays in a loop.

## Relationships

### Inherits From
- [PHASEGeneratorNodeDefinition](./phasegeneratornodedefinition.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Audio-Providing Nodes
- [enum PHASEPlaybackMode](./phaseplaybackmode.md)
  Loop options for audio playback.
- [class PHASEPushStreamNodeDefinition](./phasepushstreamnodedefinition.md)
  A node that plays a sequence of audio buffers.
- [class PHASEPushStreamNode](./phasepushstreamnode.md)
  An audio stream you manage to provide a sound buffer data.
- [struct PHASEPushStreamBufferOptions](./phasepushstreambufferoptions.md)
  Options that inform PHASE of an audio-stream buffer’s playback priority.
- [enum PHASECalibrationMode](./phasecalibrationmode.md)
  Calibration options for sound pressure level.
- [class PHASEGeneratorNodeDefinition](./phasegeneratornodedefinition.md)
  A base class for nodes that provide audio data to generate sound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesamplernodedefinition)*