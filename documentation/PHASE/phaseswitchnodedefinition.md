# PHASESwitchNodeDefinition

**Framework**: PHASE  
**Kind**: class

A node that passes invocation to only one of its child nodes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASESwitchNodeDefinition
```

#### Overview

A switch node takes a different path in a sound-event hierarchy depending on the value that the app supplies for the node’s switch metaparameter. You define the available paths ahead of time by calling [`addSubtree(_:switchValue:)`](phaseswitchnodedefinition/addsubtree(_:switchvalue:).md) at least twice and supplying the subtree’s unique string name as the switch value. When your app invokes a sound event at runtime, PHASE checks the value of [`switchMetaParameterDefinition`](phaseswitchnodedefinition/switchmetaparameterdefinition.md) to determine which path to take.

![Illustration of a flowchart that represents a sound event node tree. The chart contains three boxes, which represent nodes. At left, a box labeled Switch Node contains the text Input Metaparameter Terrain. An arrow flows to the right from the switch node to a box resting at the bottom of the figure that’s labeled Sampler Node Sidewalk Footstep. Another arrow flows to the right from the switch node to a box resting at the top of the figure, labeled Sampler Node Grass Footstep.](https://docs-assets.developer.apple.com/published/ca9b1fe656ec9cead83a5017abbb03c9/media-3918861%402x.png)

##### Switch Between Mulitple Node Trees

For example, the following diagram represents a node tree that plays one of three grass or sidewalk footstep sounds, depending on the app’s current state. The app sets a value for the switch-node metaparameter according to the terrain on which the player in a game currently stands.

![Illustration of a flow chart that represents a sound event node tree. At left, a box labeled Switch Node cointains the text Input Metaparameter terrain. Two arrows flow out of the node to respective boxes that are both labeled Random Node. One random node branches to two different boxes labeled Sampler Node. One sampler node contains the text Grass Footstep Variation One. The other sampler node contains the text Grass Footstep Variation Two. The other random node branches to two different boxes titled Sampler Node. One sampler node contains the text Cobblestone Footstep Variation One. The other sampler node contains the text Cobblestone Footstep Variation Two. ](https://docs-assets.developer.apple.com/published/74bd2906e5c8cd42e42a2dd07e1b55be/media-3918863%402x.png)

The following code creates a random node subtree for each terrain type and adds each one as a subtree to the switch node.

> 💡 **Tip**:  The [`metaParameters`](phasesoundevent/metaparameters.md) objects affect only one sound event. To propagate a metaparameter change to multiple sound events, register the metaparameter globally using [`registerGlobalMetaParameter(metaParameterDefinition:)`](phaseassetregistry/registerglobalmetaparameter(metaparameterdefinition:).md), and change its value through the asset registry’s [`globalMetaParameters`](phaseassetregistry/globalmetaparameters.md) dictionary.

 The [`metaParameters`](phasesoundevent/metaparameters.md) objects affect only one sound event. To propagate a metaparameter change to multiple sound events, register the metaparameter globally using [`registerGlobalMetaParameter(metaParameterDefinition:)`](phaseassetregistry/registerglobalmetaparameter(metaparameterdefinition:).md), and change its value through the asset registry’s [`globalMetaParameters`](phaseassetregistry/globalmetaparameters.md) dictionary.

## Topics

### Creating a Node
- [init(switchMetaParameterDefinition: PHASEStringMetaParameterDefinition)](phaseswitchnodedefinition/init(switchmetaparameterdefinition:).md)
  Creates a node that invokes a child node based on the value of the given parameter.
- [convenience init(switchMetaParameterDefinition: PHASEStringMetaParameterDefinition, identifier: String)](phaseswitchnodedefinition/init(switchmetaparameterdefinition:identifier:).md)
  Creates a named node that invokes a child node based on the value of the given parameter.
### Managing Child Nodes
- [var switchMetaParameterDefinition: PHASEStringMetaParameterDefinition](phaseswitchnodedefinition/switchmetaparameterdefinition.md)
  The meta parameter that holds the name of the child node to invoke.
- [func addSubtree(PHASESoundEventNodeDefinition, switchValue: String)](phaseswitchnodedefinition/addsubtree(_:switchvalue:).md)
  Adds a child node with the given switch value.

## Relationships

### Inherits From
- [PHASESoundEventNodeDefinition](phasesoundeventnodedefinition.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PHASERandomNodeDefinition](phaserandomnodedefinition.md)
  A sound event node that invokes one of its child nodes at random.
- [class PHASEBlendNodeDefinition](phaseblendnodedefinition.md)
  A node that smoothly fades between the audio of its child nodes.
- [class PHASEContainerNodeDefinition](phasecontainernodedefinition.md)
  A node that plays all its children at the same time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseswitchnodedefinition)*