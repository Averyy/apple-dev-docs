# activeNodes

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

Every node that contributed to the most recent graph evaluation tick.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var activeNodes: [any AnimationGraphComponent.ActiveNode] { get }
```

#### Discussion

The returned array is a snapshot — its element type is `any` [`AnimationGraphComponent.ActiveNode`](./activenode.md), so each entry exposes only the fields common to all node kinds. To inspect node-kind- specific state, downcast each element to [`AnimationGraphComponent.ActiveStateMachineNode`](./activestatemachinenode.md) or [`AnimationGraphComponent.ActiveClipNode`](./activeclipnode.md), or iterate [`activeStateMachineNodes`](./activestatemachinenodes.md) or [`activeClipNodes`](./activeclipnodes.md) for the same view filtered to a single kind.

## See Also

### Accessing active nodes
- [AnimationGraphComponent.ActiveNode](./activenode.md)
  Common debug information for any node that was active during the most recent graph evaluation tick.
- [var activeClipNodes: [AnimationGraphComponent.ActiveClipNode]](./activeclipnodes.md)
  The animation clip nodes that were active during the most recent graph evaluation tick.
- [AnimationGraphComponent.ActiveClipNode](./activeclipnode.md)
  Debug information for an active animation clip node within the graph.
- [var activeStateMachineNodes: [AnimationGraphComponent.ActiveStateMachineNode]](./activestatemachinenodes.md)
  The state machine nodes that were active during the most recent graph evaluation tick.
- [AnimationGraphComponent.ActiveStateMachineNode](./activestatemachinenode.md)
  Debug information for an active state machine node within the graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationgraphcomponent/activenodes)*