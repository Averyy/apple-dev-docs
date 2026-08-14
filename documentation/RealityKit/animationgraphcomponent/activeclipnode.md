# AnimationGraphComponent.ActiveClipNode

**Framework**: RealityKit  
**Kind**: struct

Debug information for an active animation clip node within the graph.

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

#### Overview

Use this type to read the current playback position of an animation clip the graph is sampling.

## Topics

### Inspecting playback state
- [let id: Int](animationgraphcomponent/activeclipnode/id.md)
  The unique identifier of the node within the compiled graph.
- [var currentCycle: Float](animationgraphcomponent/activeclipnode/currentcycle.md)
  The current playback cycle of the clip.
- [var wasReset: Bool](animationgraphcomponent/activeclipnode/wasreset.md)
  A Boolean value that indicates whether the node was reset during the last evaluation tick.
### Instance Properties
- [let name: String](animationgraphcomponent/activeclipnode/name.md)
  The author-supplied name of the node from the graph definition.

## Relationships

### Conforms To
- [AnimationGraphComponent.ActiveNode](animationgraphcomponent/activenode.md)
- [Equatable](../swift/equatable.md)
- [Identifiable](../swift/identifiable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var activeNodes: [any AnimationGraphComponent.ActiveNode]](animationgraphcomponent/activenodes.md)
  Every node that contributed to the most recent graph evaluation tick.
- [AnimationGraphComponent.ActiveNode](animationgraphcomponent/activenode.md)
  Common debug information for any node that was active during the most recent graph evaluation tick.
- [var activeClipNodes: [AnimationGraphComponent.ActiveClipNode]](animationgraphcomponent/activeclipnodes.md)
  The animation clip nodes that were active during the most recent graph evaluation tick.
- [var activeStateMachineNodes: [AnimationGraphComponent.ActiveStateMachineNode]](animationgraphcomponent/activestatemachinenodes.md)
  The state machine nodes that were active during the most recent graph evaluation tick.
- [AnimationGraphComponent.ActiveStateMachineNode](animationgraphcomponent/activestatemachinenode.md)
  Debug information for an active state machine node within the graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationgraphcomponent/activeclipnode)*