# activeStateMachineNodes

**Framework**: RealityKit  
**Kind**: property

The state machine nodes that were active during the last graph evaluation tick.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var activeStateMachineNodes: [AnimationGraphComponent.ActiveStateMachineNode] { get }
```

## See Also

- [var activeNodes: [any AnimationGraphComponent.ActiveNode]](animationgraphcomponent/activenodes.md)
  All nodes that were active during the last graph evaluation tick.
- [AnimationGraphComponent.ActiveNode](animationgraphcomponent/activenode.md)
  A protocol providing common debug information for any active node within a compiled animation graph.
- [var activeClipNodes: [AnimationGraphComponent.ActiveClipNode]](animationgraphcomponent/activeclipnodes.md)
  The animation clip nodes that were active during the last graph evaluation tick.
- [AnimationGraphComponent.ActiveClipNode](animationgraphcomponent/activeclipnode.md)
  Contains clip debug information for an active animation clip node within a compiled animation graph, used for inspection and debugging.
- [AnimationGraphComponent.ActiveStateMachineNode](animationgraphcomponent/activestatemachinenode.md)
  Contains state machine debug information for an active state machine node within a compiled animation graph, used for inspection and debugging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationgraphcomponent/activestatemachinenodes)*