# PHASESoundAsset

**Framework**: PHASE  
**Kind**: class

A sound resource stored in the asset registry.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASESoundAsset
```

#### Overview

This class wraps source audio data that an app intends to play. The framework requires a mixer to play a sound asset, and sound event nodes like [`PHASESamplerNodeDefinition`](phasesamplernodedefinition.md) combine the asset with a mixer. To provide a sound asset to a sound-event node, refer to the asset by the `identifier` you pass into the [`registerSoundAsset(url:identifier:assetType:channelLayout:normalizationMode:)`](phaseassetregistry/registersoundasset(url:identifier:assettype:channellayout:normalizationmode:).md) function.

## Topics

### Accessing Sound Data
- [var data: Data?](phasesoundasset/data.md)
  A storage buffer for the sound asset.
- [var url: URL?](phasesoundasset/url.md)
  The URL of the sound asset.
### Classifying an Asset
- [var type: PHASEAsset.AssetType](phasesoundasset/type.md)
  The type of sound asset.

## Relationships

### Inherits From
- [PHASEAsset](phaseasset.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

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
- [Sound Event Nodes](sound-event-nodes.md)
  Objects that connect to form a hierarchical tree of audio actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesoundasset)*