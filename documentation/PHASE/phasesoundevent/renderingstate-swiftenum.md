# PHASESoundEvent.RenderingState

**Framework**: PHASE  
**Kind**: enum

The playback status of audio.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
enum RenderingState
```

#### Overview

This enumeration defines the possible values of:

- A sound event’s [`renderingState`](phasesoundevent/renderingstate-swift.property.md) property
- The engine’s [`renderingState`](phaseengine/renderingstate.md) property

## Topics

### States
- [PHASESoundEvent.RenderingState.paused](phasesoundevent/renderingstate-swift.enum/paused.md)
  A state in which sound event playback pauses.
- [PHASESoundEvent.RenderingState.started](phasesoundevent/renderingstate-swift.enum/started.md)
  A state in which sound event playback starts.
- [PHASESoundEvent.RenderingState.stopped](phasesoundevent/renderingstate-swift.enum/stopped.md)
  A state in which sound event playback stops.
### Initializers
- [init?(rawValue: Int)](phasesoundevent/renderingstate-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class PHASESoundAsset](phasesoundasset.md)
  A sound resource stored in the asset registry.
- [class PHASESoundEvent](phasesoundevent.md)
  An object that determines which audio to play.
- [class PHASESoundEventNodeDefinition](phasesoundeventnodedefinition.md)
  A base class for sound event nodes that connect to form a node hierarchy.
- [class PHASESoundEventNodeAsset](phasesoundeventnodeasset.md)
  A template object for sounds that can play in reaction to environmental state.
- [class PHASEAsset](phaseasset.md)
  A base class that adds a name to framework assets.
- [Sound Event Nodes](sound-event-nodes.md)
  Objects that connect to form a hierarchical tree of audio actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesoundevent/renderingstate-swift.enum)*