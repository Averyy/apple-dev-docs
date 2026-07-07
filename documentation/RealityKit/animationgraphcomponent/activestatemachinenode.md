# AnimationGraphComponent.ActiveStateMachineNode

**Framework**: RealityKit  
**Kind**: struct

Debug information for an active state machine node within the graph.

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

#### Overview

Use this type to read the current and previous states of a state machine, along with the most recent transition the state machine took. The state and transition values are IDs into the graph definition rather than human-readable strings.

## Topics

### Identifying the node
- [let id: Int](animationgraphcomponent/activestatemachinenode/id.md)
  The unique identifier of the node within the compiled graph.
### Inspecting the node state
- [var currentState: Int](animationgraphcomponent/activestatemachinenode/currentstate.md)
  The ID of the state the state machine is currently in.
- [var previousState: Int](animationgraphcomponent/activestatemachinenode/previousstate.md)
  The ID of the state the state machine was in immediately before [`currentState`](animationgraphcomponent/activestatemachinenode/currentstate.md).
- [var lastTransition: Int](animationgraphcomponent/activestatemachinenode/lasttransition.md)
  The ID of the most recent transition the state machine took.
- [var wasReset: Bool](animationgraphcomponent/activestatemachinenode/wasreset.md)
  A Boolean value that indicates whether the node was reset during the last evaluation tick.
### Instance Properties
- [let name: String](animationgraphcomponent/activestatemachinenode/name.md)
  The author-supplied name of the node from the graph definition.

## Relationships

### Conforms To
- [AnimationGraphComponent.ActiveNode](animationgraphcomponent/activenode.md)
- [Equatable](../Swift/Equatable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var activeNodes: [any AnimationGraphComponent.ActiveNode]](animationgraphcomponent/activenodes.md)
  Every node that contributed to the most recent graph evaluation tick.
- [AnimationGraphComponent.ActiveNode](animationgraphcomponent/activenode.md)
  Common debug information for any node that was active during the most recent graph evaluation tick.
- [var activeClipNodes: [AnimationGraphComponent.ActiveClipNode]](animationgraphcomponent/activeclipnodes.md)
  The animation clip nodes that were active during the most recent graph evaluation tick.
- [AnimationGraphComponent.ActiveClipNode](animationgraphcomponent/activeclipnode.md)
  Debug information for an active animation clip node within the graph.
- [var activeStateMachineNodes: [AnimationGraphComponent.ActiveStateMachineNode]](animationgraphcomponent/activestatemachinenodes.md)
  The state machine nodes that were active during the most recent graph evaluation tick.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationgraphcomponent/activestatemachinenode)*