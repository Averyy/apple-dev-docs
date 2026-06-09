# AnimationGraphComponent.ActiveClipNode

**Framework**: RealityKit  
**Kind**: struct

Contains clip debug information for an active animation clip node within a compiled animation graph, used for inspection and debugging.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ActiveClipNode
```

## Topics

### Inspecting playback state
- [let id: Int](animationgraphcomponent/activeclipnode/id.md)
  Returns the id of the node.
- [var currentCycle: Float](animationgraphcomponent/activeclipnode/currentcycle.md)
  The current playback cycle.
- [var wasReset: Bool](animationgraphcomponent/activeclipnode/wasreset.md)
  Returns `true` if the node was reset during the last tick.
### Instance Properties
- [let name: String](animationgraphcomponent/activeclipnode/name.md)
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
- [var activeStateMachineNodes: [AnimationGraphComponent.ActiveStateMachineNode]](animationgraphcomponent/activestatemachinenodes.md)
  The state machine nodes that were active during the last graph evaluation tick.
- [AnimationGraphComponent.ActiveStateMachineNode](animationgraphcomponent/activestatemachinenode.md)
  Contains state machine debug information for an active state machine node within a compiled animation graph, used for inspection and debugging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationgraphcomponent/activeclipnode)*