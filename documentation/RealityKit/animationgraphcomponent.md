# AnimationGraphComponent

**Framework**: RealityKit  
**Kind**: struct

A component that drives skeletal animation on an entity using a node-based animation graph.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct AnimationGraphComponent
```

#### Overview

Animation graphs blend and transition between multiple animations at runtime using a graph of connected nodes.

Use `AnimationGraphComponent` to attach a compiled [`AnimationGraphResource`](animationgraphresource.md) to an entity. RealityKit evaluates the graph each frame and writes the resulting pose to the entity’s [`SkeletalPosesComponent`](skeletalposescomponent.md).

##### Attach a Graph to an Entity

```swift
entity.components.set(AnimationGraphComponent(resource: graphResource))
```

##### Inspect the Active Graph State

[`activeNodes`](animationgraphcomponent/activenodes.md) reflects all nodes that contributed to the current pose. Use [`activeStateMachineNodes`](animationgraphcomponent/activestatemachinenodes.md) or [`activeClipNodes`](animationgraphcomponent/activeclipnodes.md) to work directly with a specific node type.

```swift
for node in component.activeStateMachineNodes {
    print("Current state: \(node.currentState)")
}

for node in component.activeClipNodes {
    print("Current cycle: \(node.currentCycle)")
}
```

## Topics

### Creating a component
- [init(graph: AnimationGraphResource)](animationgraphcomponent/init(graph:).md)
### Accessing the graph
- [var graph: AnimationGraphResource](animationgraphcomponent/graph.md)
  Returns the animation graph resource associated with this component.
### Accessing active nodes
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
- [AnimationGraphComponent.ActiveStateMachineNode](animationgraphcomponent/activestatemachinenode.md)
  Contains state machine debug information for an active state machine node within a compiled animation graph, used for inspection and debugging.
### Accessing active tags
- [var activeTags: [AnimationGraphComponent.ActiveTag]](animationgraphcomponent/activetags.md)
  The tags that were active during the last graph evaluation tick.
- [AnimationGraphComponent.ActiveTag](animationgraphcomponent/activetag.md)
  Contains debug information of a single tag within a compiled animation graph, used for inspection and debugging.

## Relationships

### Conforms To
- [Component](component.md)

## See Also

- [class AnimationGraphResource](animationgraphresource.md)
  A compiled animation graph resource that drives skeletal animation on an entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationgraphcomponent)*