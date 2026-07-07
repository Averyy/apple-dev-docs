# AnimationGraphComponent

**Framework**: RealityKit  
**Kind**: struct

A component that drives skeletal animation on an entity using an animation graph.

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

[`AnimationGraphComponent`](animationgraphcomponent.md) attaches a compiled [`AnimationGraphResource`](animationgraphresource.md) to an entity. The component evaluates the graph each frame, computes a skeletal pose by blending and transitioning between animation clips, and applies the resulting pose to the entity’s [`SkeletalPosesComponent`](skeletalposescomponent.md).

Multiple components in the same scene can reference the same resource, which lets a single graph drive many entities without duplicating its underlying data. Each component keeps its own per-instance evaluation state — animation timing, state-machine progress, and parameter values — so characters that share a graph stay independent.

##### Attach a Graph to an Entity

```swift
entity.components.set(AnimationGraphComponent(graph: graphResource))
```

##### Inspect the Active Graph State

The component exposes the graph’s runtime state for debugging and for building tools that visualize what a character is doing. [`activeNodes`](animationgraphcomponent/activenodes.md) returns every node that contributed to the most recent pose. To work with a single kind of node, iterate [`activeStateMachineNodes`](animationgraphcomponent/activestatemachinenodes.md) or [`activeClipNodes`](animationgraphcomponent/activeclipnodes.md) instead — those collections return the narrower [`AnimationGraphComponent.ActiveStateMachineNode`](animationgraphcomponent/activestatemachinenode.md) and [`AnimationGraphComponent.ActiveClipNode`](animationgraphcomponent/activeclipnode.md) types, which expose only the fields that apply to that node kind.

```swift
for node in component.activeStateMachineNodes {
    print("\(node.name): state \(node.currentState)")
}

for node in component.activeClipNodes {
    print("\(node.name): cycle \(node.currentCycle)")
}
```

To observe outputs the graph emits back to the rest of the application, read [`activeTags`](animationgraphcomponent/activetags.md). Tags are graph-level signals that the graph raises while certain states are active.

## Topics

### Creating a component
- [init(graph: AnimationGraphResource)](animationgraphcomponent/init(graph:).md)
  Creates a component that drives skeletal animation on an entity using the supplied compiled animation graph.
### Accessing the graph
- [var graph: AnimationGraphResource](animationgraphcomponent/graph.md)
  The compiled animation graph that backs this component.
### Accessing active nodes
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
- [AnimationGraphComponent.ActiveStateMachineNode](animationgraphcomponent/activestatemachinenode.md)
  Debug information for an active state machine node within the graph.
### Accessing active tags
- [var activeTags: [AnimationGraphComponent.ActiveTag]](animationgraphcomponent/activetags.md)
  The tags that were active or fired during the most recent graph evaluation tick.
- [AnimationGraphComponent.ActiveTag](animationgraphcomponent/activetag.md)
  A graph-level signal raised by the graph while certain states are active.

## Relationships

### Conforms To
- [Component](component.md)

## See Also

- [class AnimationGraphResource](animationgraphresource.md)
  A compiled animation graph that drives skeletal animation on an entity by blending and transitioning between animation clips at runtime.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationgraphcomponent)*