# activeClipNodes

**Framework**: RealityKit  
**Kind**: property

The animation clip nodes that were active during the most recent graph evaluation tick.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var activeClipNodes: [AnimationGraphComponent.ActiveClipNode] { get }
```

#### Discussion

This is the typed view of [`activeNodes`](animationgraphcomponent/activenodes.md) filtered to [`AnimationGraphComponent.ActiveClipNode`](animationgraphcomponent/activeclipnode.md).

## See Also

- [var activeNodes: [any AnimationGraphComponent.ActiveNode]](animationgraphcomponent/activenodes.md)
  Every node that contributed to the most recent graph evaluation tick.
- [AnimationGraphComponent.ActiveNode](animationgraphcomponent/activenode.md)
  Common debug information for any node that was active during the most recent graph evaluation tick.
- [AnimationGraphComponent.ActiveClipNode](animationgraphcomponent/activeclipnode.md)
  Debug information for an active animation clip node within the graph.
- [var activeStateMachineNodes: [AnimationGraphComponent.ActiveStateMachineNode]](animationgraphcomponent/activestatemachinenodes.md)
  The state machine nodes that were active during the most recent graph evaluation tick.
- [AnimationGraphComponent.ActiveStateMachineNode](animationgraphcomponent/activestatemachinenode.md)
  Debug information for an active state machine node within the graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationgraphcomponent/activeclipnodes)*