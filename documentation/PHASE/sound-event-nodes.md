# Sound Event Nodes

**Framework**: PHASE

Objects that connect to form a hierarchical tree of audio actions.

#### Overview

To play sound, your app assembles a hieararchical structure of audio  that determine which sound to play at the moment. A tree with two sampler nodes branching from a switch node plays only one sampler, depending on your app’s state. You set the control logic in advance that specifies the conditions upon which the switch node toggles. To play the same audio consistently, create a tree with a single sampler node.

To invoke the tree, create a sound event that references the tree and call [`start(completion:)`](phasesoundevent/start(completion:).md) on the sound event.

## Topics

### Audio-Providing Nodes
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
- [class PHASEGeneratorNodeDefinition](phasegeneratornodedefinition.md)
  A base class for nodes that provide audio data to generate sound.
### Control Nodes
- [class PHASESwitchNodeDefinition](phaseswitchnodedefinition.md)
  A node that passes invocation to only one of its child nodes.
- [class PHASERandomNodeDefinition](phaserandomnodedefinition.md)
  A sound event node that invokes one of its child nodes at random.
- [class PHASEBlendNodeDefinition](phaseblendnodedefinition.md)
  A node that smoothly fades between the audio of its child nodes.
- [class PHASEContainerNodeDefinition](phasecontainernodedefinition.md)
  A node that plays all its children at the same time.

## See Also

- [class PHASESoundAsset](phasesoundasset.md)
  A sound resource stored in the asset registry.
- [class PHASESoundEvent](phasesoundevent.md)
  An object that determines which audio to play.
- [PHASESoundEvent.RenderingState](phasesoundevent/renderingstate-swift.enum.md)
  The playback status of audio.
- [class PHASESoundEventNodeDefinition](phasesoundeventnodedefinition.md)
  A base class for sound event nodes that connect to form a node hierarchy.
- [class PHASESoundEventNodeAsset](phasesoundeventnodeasset.md)
  A template object for sounds that can play in reaction to environmental state.
- [class PHASEAsset](phaseasset.md)
  A base class that adds a name to framework assets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/sound-event-nodes)*