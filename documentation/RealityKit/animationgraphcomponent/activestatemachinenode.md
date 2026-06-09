# AnimationGraphComponent.ActiveStateMachineNode

**Framework**: RealityKit  
**Kind**: struct

Contains state machine debug information for an active state machine node within a compiled animation graph, used for inspection and debugging.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ActiveStateMachineNode
```

## Topics

### Identifying the node
- [let id: Int](animationgraphcomponent/activestatemachinenode/id.md)
  Returns the id of the node.
### Inspecting the node state
- [var currentState: Int](animationgraphcomponent/activestatemachinenode/currentstate.md)
  The ID of the current state.
- [var previousState: Int](animationgraphcomponent/activestatemachinenode/previousstate.md)
  The ID of the previous state.
- [var lastTransition: Int](animationgraphcomponent/activestatemachinenode/lasttransition.md)
  The ID of the last active transition.
- [var wasReset: Bool](animationgraphcomponent/activestatemachinenode/wasreset.md)
  Returns `true` if the node was reset during the last tick.
### Instance Properties
- [let name: String](animationgraphcomponent/activestatemachinenode/name.md)
  Returns the name of the node.

## Relationships

### Conforms To
- [AnimationGraphComponent.ActiveNode](animationgraphcomponent/activenode.md)
- [Equatable](../Swift/Equatable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var activeNodes: [any AnimationGraphComponent.ActiveNode]](animationgraphcomponent/activenodes.md)
  All nodes that were active during the last graph evaluation tick.
- [AnimationGraphComponent.ActiveNode](animationgraphcomponent/activenode.md)
  A protocol providing common debug information for any active node within a compiled animation graph.
- [var activeClipNodes: [AnimationGraphComponent.ActiveClipNode]](animationgraphcomponent/activeclipnodes.md)
  The animation clip nodes that were active during the last graph evaluation tick.
- [AnimationGraphComponent.ActiveClipNode](animationgraphcomponent/activeclipnode.md)
  Contains clip debug information for an active animation clip node within a compiled animation graph, used for inspection and debugging.
- [var activeStateMachineNodes: [AnimationGraphComponent.ActiveStateMachineNode]](animationgraphcomponent/activestatemachinenodes.md)
  The state machine nodes that were active during the last graph evaluation tick.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationgraphcomponent/activestatemachinenode)*