# AnimationGraphComponent.ActiveStateMachineNode

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

Debug information for an active state machine node within the graph.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct ActiveStateMachineNode
```

## Overview

Use this type to read the current and previous states of a state machine, along with the most recent transition the state machine took. The state and transition values are IDs into the graph definition rather than human-readable strings.

## Topics

### Identifying the node
- [let id: Int](./activestatemachinenode/id.md)
  The unique identifier of the node within the compiled graph.
### Inspecting the node state
- [var currentState: Int](./activestatemachinenode/currentstate.md)
  The ID of the state the state machine is currently in.
- [var previousState: Int](./activestatemachinenode/previousstate.md)
  The ID of the state the state machine was in immediately before [`currentState`](./activestatemachinenode/currentstate.md).
- [var lastTransition: Int](./activestatemachinenode/lasttransition.md)
  The ID of the most recent transition the state machine took.
- [var wasReset: Bool](./activestatemachinenode/wasreset.md)
  A Boolean value that indicates whether the node was reset during the last evaluation tick.
### Instance Properties
- [let name: String](./activestatemachinenode/name.md)
  The author-supplied name of the node from the graph definition.

## Relationships

### Conforms To
- [AnimationGraphComponent.ActiveNode](./activenode.md)
- [Equatable](../../Swift/equatable.md)
- [Identifiable](../../Swift/identifiable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing active nodes
- [var activeNodes: [any AnimationGraphComponent.ActiveNode]](./activenodes.md)
  Every node that contributed to the most recent graph evaluation tick.
- [AnimationGraphComponent.ActiveNode](./activenode.md)
  Common debug information for any node that was active during the most recent graph evaluation tick.
- [var activeClipNodes: [AnimationGraphComponent.ActiveClipNode]](./activeclipnodes.md)
  The animation clip nodes that were active during the most recent graph evaluation tick.
- [AnimationGraphComponent.ActiveClipNode](./activeclipnode.md)
  Debug information for an active animation clip node within the graph.
- [var activeStateMachineNodes: [AnimationGraphComponent.ActiveStateMachineNode]](./activestatemachinenodes.md)
  The state machine nodes that were active during the most recent graph evaluation tick.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationgraphcomponent/activestatemachinenode)*