# AnimationGraphComponent.ActiveNode

**Framework**: RealityKit  
**Kind**: protocol

A protocol providing common debug information for any active node within a compiled animation graph.

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

## Topics

### Inspecting the active node
- [var id: Int](animationgraphcomponent/activenode/id.md)
  Returns the id of the node.
- [var wasReset: Bool](animationgraphcomponent/activenode/wasreset.md)
  Returns `true` if the node was reset during the last tick.
### Instance Properties
- [var name: String](animationgraphcomponent/activenode/name.md)
  Returns the name of the node.

## Relationships

### Inherits From
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [AnimationGraphComponent.ActiveClipNode](animationgraphcomponent/activeclipnode.md)
- [AnimationGraphComponent.ActiveStateMachineNode](animationgraphcomponent/activestatemachinenode.md)

## See Also

- [var activeNodes: [any AnimationGraphComponent.ActiveNode]](animationgraphcomponent/activenodes.md)
  All nodes that were active during the last graph evaluation tick.
- [var activeClipNodes: [AnimationGraphComponent.ActiveClipNode]](animationgraphcomponent/activeclipnodes.md)
  The animation clip nodes that were active during the last graph evaluation tick.
- [AnimationGraphComponent.ActiveClipNode](animationgraphcomponent/activeclipnode.md)
  Contains clip debug information for an active animation clip node within a compiled animation graph, used for inspection and debugging.
- [var activeStateMachineNodes: [AnimationGraphComponent.ActiveStateMachineNode]](animationgraphcomponent/activestatemachinenodes.md)
  The state machine nodes that were active during the last graph evaluation tick.
- [AnimationGraphComponent.ActiveStateMachineNode](animationgraphcomponent/activestatemachinenode.md)
  Contains state machine debug information for an active state machine node within a compiled animation graph, used for inspection and debugging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationgraphcomponent/activenode)*