# PHASESoundEventNodeDefinition

**Framework**: PHASE  
**Kind**: class

A base class for sound event nodes that connect to form a node hierarchy.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASESoundEventNodeDefinition
```

#### Overview

This class defines the base functionality for an object that, depending on the derived class’s type, either plays audio or hands off the invocation to one or more other nodes.

##### Configure a Sound Event Node to Play Audio

To play audio with this class, retrieve a sound-event node asset ([`PHASESoundEventNodeAsset`](phasesoundeventnodeasset.md)) that generates sound events by creating and registering one of the audio-providing node definitions in [`Sound Event Nodes`](sound-event-nodes.md). Call [`registerSoundEventAsset(rootNode:identifier:)`](phaseassetregistry/registersoundeventasset(rootnode:identifier:).md) and pass the node definition in the `rootNode` argument. Provide an `identifier` argument with a unique name that your app refers to later when generating a playable [`PHASESoundEvent`](phasesoundevent.md).

##### Configure a Node Hiearchy That Reacts to Your Apps State

You can create a hierarchy of nodes that blends audio based on your app’s parameters, or plays the right audio based on your app’s state. To create the hierarchy, register one of the control nodes in [`Sound Event Nodes`](sound-event-nodes.md) by calling [`registerSoundEventAsset(rootNode:identifier:)`](phaseassetregistry/registersoundeventasset(rootnode:identifier:).md), passing in a unique [`identifier`](phasedefinition/identifier.md) you define for the subclass.

The particular configuration you choose for a node hierarchy instructs PHASE on which audio to play, when to play it, or whether to hand off an invocation to one or more child nodes ([`children`](phasesoundeventnodedefinition/children.md)).

For example, if you register and invoke a [`PHASESwitchNodeDefinition`](phaseswitchnodedefinition.md) that contains two child [`PHASESamplerNodeDefinition`](phasesamplernodedefinition.md) objects, PHASE plays the audio of one of the child sampler nodes based on the current value of the switch node’s metaparameter. For more information, see [`metaParameters`](phasesoundevent/metaparameters.md).

## Topics

### Accessing Child Nodes
- [var children: [PHASESoundEventNodeDefinition]](phasesoundeventnodedefinition/children.md)
  An array of child sound event nodes.
### Identifying a Definition
- [class PHASEDefinition](phasedefinition.md)
  A base class that adds a name to framework definitions.

## Relationships

### Inherits From
- [PHASEDefinition](phasedefinition.md)
### Inherited By
- [PHASEBlendNodeDefinition](phaseblendnodedefinition.md)
- [PHASEContainerNodeDefinition](phasecontainernodedefinition.md)
- [PHASEGeneratorNodeDefinition](phasegeneratornodedefinition.md)
- [PHASERandomNodeDefinition](phaserandomnodedefinition.md)
- [PHASESwitchNodeDefinition](phaseswitchnodedefinition.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PHASESoundAsset](phasesoundasset.md)
  A sound resource stored in the asset registry.
- [class PHASESoundEvent](phasesoundevent.md)
  An object that determines which audio to play.
- [PHASESoundEvent.RenderingState](phasesoundevent/renderingstate-swift.enum.md)
  The playback status of audio.
- [class PHASESoundEventNodeAsset](phasesoundeventnodeasset.md)
  A template object for sounds that can play in reaction to environmental state.
- [class PHASEAsset](phaseasset.md)
  A base class that adds a name to framework assets.
- [Sound Event Nodes](sound-event-nodes.md)
  Objects that connect to form a hierarchical tree of audio actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesoundeventnodedefinition)*