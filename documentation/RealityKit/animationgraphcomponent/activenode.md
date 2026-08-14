# AnimationGraphComponent.ActiveNode

**Framework**: RealityKit  
**Kind**: protocol

Common debug information for any node that was active during the most recent graph evaluation tick.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol ActiveNode : Identifiable, Sendable
```

#### Overview

`AnimationGraphComponent` reports active nodes through this protocol so that tools can iterate every node uniformly. To inspect node-kind-specific state, downcast to [`AnimationGraphComponent.ActiveStateMachineNode`](animationgraphcomponent/activestatemachinenode.md) or [`AnimationGraphComponent.ActiveClipNode`](animationgraphcomponent/activeclipnode.md), or iterate the typed accessors [`activeStateMachineNodes`](animationgraphcomponent/activestatemachinenodes.md) and [`activeClipNodes`](animationgraphcomponent/activeclipnodes.md) directly.

## Topics

### Inspecting the active node
- [var id: Int](animationgraphcomponent/activenode/id.md)
  The unique identifier of the node within the compiled graph.
- [var wasReset: Bool](animationgraphcomponent/activenode/wasreset.md)
  A Boolean value that indicates whether the node was reset during the last evaluation tick.
### Instance Properties
- [var name: String](animationgraphcomponent/activenode/name.md)
  The author-supplied name of the node from the graph definition.

## Relationships

### Inherits From
- [Identifiable](../swift/identifiable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
### Conforming Types
- [AnimationGraphComponent.ActiveClipNode](animationgraphcomponent/activeclipnode.md)
- [AnimationGraphComponent.ActiveStateMachineNode](animationgraphcomponent/activestatemachinenode.md)

## See Also

- [var activeNodes: [any AnimationGraphComponent.ActiveNode]](animationgraphcomponent/activenodes.md)
  Every node that contributed to the most recent graph evaluation tick.
- [var activeClipNodes: [AnimationGraphComponent.ActiveClipNode]](animationgraphcomponent/activeclipnodes.md)
  The animation clip nodes that were active during the most recent graph evaluation tick.
- [AnimationGraphComponent.ActiveClipNode](animationgraphcomponent/activeclipnode.md)
  Debug information for an active animation clip node within the graph.
- [var activeStateMachineNodes: [AnimationGraphComponent.ActiveStateMachineNode]](animationgraphcomponent/activestatemachinenodes.md)
  The state machine nodes that were active during the most recent graph evaluation tick.
- [AnimationGraphComponent.ActiveStateMachineNode](animationgraphcomponent/activestatemachinenode.md)
  Debug information for an active state machine node within the graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationgraphcomponent/activenode)*