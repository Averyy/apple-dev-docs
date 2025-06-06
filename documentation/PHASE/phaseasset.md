# PHASEAsset

**Framework**: PHASE  
**Kind**: class

A base class that adds a name to framework assets.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASEAsset
```

#### Overview

Through inheritance, this class adds a string [`identifier`](phaseasset/identifier.md) to subclasses, for example, [`PHASESoundAsset`](phasesoundasset.md) and [`PHASESoundEventNodeAsset`](phasesoundeventnodeasset.md).

PHASE generates objects of this type based on template [`PHASEDefinition`](phasedefinition.md) subclasses. For example, PHASE gives you a [`PHASESoundEventNodeAsset`](phasesoundeventnodeasset.md) when you register a [`PHASESoundEventNodeDefinition`](phasesoundeventnodedefinition.md) with the asset registry via [`registerSoundEventAsset(rootNode:identifier:)`](phaseassetregistry/registersoundeventasset(rootnode:identifier:).md).

## Topics

### Identifying an Asset
- [var identifier: String](phaseasset/identifier.md)
  A unique name for the asset.
### Classifying an Asset
- [PHASEAsset.AssetType](phaseasset/assettype.md)
  Options that determine how PHASE manages sound assets in memory.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [PHASEGlobalMetaParameterAsset](phaseglobalmetaparameterasset.md)
- [PHASESoundAsset](phasesoundasset.md)
- [PHASESoundEventNodeAsset](phasesoundeventnodeasset.md)
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
- [class PHASESoundEventNodeDefinition](phasesoundeventnodedefinition.md)
  A base class for sound event nodes that connect to form a node hierarchy.
- [class PHASESoundEventNodeAsset](phasesoundeventnodeasset.md)
  A template object for sounds that can play in reaction to environmental state.
- [Sound Event Nodes](sound-event-nodes.md)
  Objects that connect to form a hierarchical tree of audio actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseasset)*