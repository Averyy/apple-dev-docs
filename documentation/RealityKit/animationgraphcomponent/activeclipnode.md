# AnimationGraphComponent.ActiveClipNode

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

Debug information for an active animation clip node within the graph.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct ActiveClipNode
```

#### Overview

Use this type to read the current playback position of an animation clip the graph is sampling.

## Topics

### Inspecting playback state
- [let id: Int](./activeclipnode/id.md)
  The unique identifier of the node within the compiled graph.
- [var currentCycle: Float](./activeclipnode/currentcycle.md)
  The current playback cycle of the clip.
- [var wasReset: Bool](./activeclipnode/wasreset.md)
  A Boolean value that indicates whether the node was reset during the last evaluation tick.
### Instance Properties
- [let name: String](./activeclipnode/name.md)
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
- [var activeStateMachineNodes: [AnimationGraphComponent.ActiveStateMachineNode]](./activestatemachinenodes.md)
  The state machine nodes that were active during the most recent graph evaluation tick.
- [AnimationGraphComponent.ActiveStateMachineNode](./activestatemachinenode.md)
  Debug information for an active state machine node within the graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationgraphcomponent/activeclipnode)*