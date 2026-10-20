# AnimationGraphComponent.ActiveNode

**Framework**: RealityKit  
**Kind**: protocol  
**Role**: Protocol

Common debug information for any node that was active during the most recent graph evaluation tick.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
protocol ActiveNode : Identifiable, Sendable
```

#### Overview

`AnimationGraphComponent` reports active nodes through this protocol so that tools can iterate every node uniformly. To inspect node-kind-specific state, downcast to [`AnimationGraphComponent.ActiveStateMachineNode`](./activestatemachinenode.md) or [`AnimationGraphComponent.ActiveClipNode`](./activeclipnode.md), or iterate the typed accessors [`activeStateMachineNodes`](./activestatemachinenodes.md) and [`activeClipNodes`](./activeclipnodes.md) directly.

## Topics

### Inspecting the active node
- [var id: Int](./activenode/id.md)
  The unique identifier of the node within the compiled graph.
- [var wasReset: Bool](./activenode/wasreset.md)
  A Boolean value that indicates whether the node was reset during the last evaluation tick.
### Instance Properties
- [var name: String](./activenode/name.md)
  The author-supplied name of the node from the graph definition.

## Relationships

### Inherits From
- [Identifiable](../../Swift/identifiable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
### Conforming Types
- [AnimationGraphComponent.ActiveClipNode](./activeclipnode.md)
- [AnimationGraphComponent.ActiveStateMachineNode](./activestatemachinenode.md)

## See Also

### Accessing active nodes
- [var activeNodes: [any AnimationGraphComponent.ActiveNode]](./activenodes.md)
  Every node that contributed to the most recent graph evaluation tick.
- [var activeClipNodes: [AnimationGraphComponent.ActiveClipNode]](./activeclipnodes.md)
  The animation clip nodes that were active during the most recent graph evaluation tick.
- [AnimationGraphComponent.ActiveClipNode](./activeclipnode.md)
  Debug information for an active animation clip node within the graph.
- [var activeStateMachineNodes: [AnimationGraphComponent.ActiveStateMachineNode]](./activestatemachinenodes.md)
  The state machine nodes that were active during the most recent graph evaluation tick.
- [AnimationGraphComponent.ActiveStateMachineNode](./activestatemachinenode.md)
  Debug information for an active state machine node within the graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationgraphcomponent/activenode)*