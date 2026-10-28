# PHASESoundEvent.RenderingState

**Framework**: PHASE  
**Kind**: enum  
**Role**: Enumeration

The playback status of audio.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
enum RenderingState
```

```c
enum PHASERenderingState : NSInteger;
```

## Overview

This enumeration defines the possible values of:

- A sound event’s [`renderingState`](./renderingstate-swift.property.md) property
- The engine’s [`renderingState`](../phaseengine/renderingstate.md) property

## Topics

### States
- [PHASESoundEvent.RenderingState.paused](./renderingstate-swift.enum/paused.md)
  A state in which sound event playback pauses.
- [PHASESoundEvent.RenderingState.started](./renderingstate-swift.enum/started.md)
  A state in which sound event playback starts.
- [PHASESoundEvent.RenderingState.stopped](./renderingstate-swift.enum/stopped.md)
  A state in which sound event playback stops.
### Initializers
- [init?(rawValue: Int)](./renderingstate-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Audio Selection and Playback
- [class PHASESoundAsset](../phasesoundasset.md)
  A sound resource stored in the asset registry.
- [class PHASESoundEvent](../phasesoundevent.md)
  An object that determines which audio to play.
- [class PHASESoundEventNodeDefinition](../phasesoundeventnodedefinition.md)
  A base class for sound event nodes that connect to form a node hierarchy.
- [class PHASESoundEventNodeAsset](../phasesoundeventnodeasset.md)
  A template object for sounds that can play in reaction to environmental state.
- [class PHASEAsset](../phaseasset.md)
  A base class that adds a name to framework assets.
- [Sound Event Nodes](../sound-event-nodes.md)
  Objects that connect to form a hierarchical tree of audio actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesoundevent/renderingstate-swift.enum)*