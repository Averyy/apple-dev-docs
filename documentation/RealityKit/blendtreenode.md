# BlendTreeNode

**Framework**: Realitykit  
**Kind**: protocol

An interface for a node that’s a member of a blend tree.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
protocol BlendTreeNode
```

#### Overview

This protocol specifies the common functionality for the animations that compose a [`BlendTreeAnimation`](blendtreeanimation.md). The animation defines a [`root`](blendtreeanimation/root.md) node of this type. To define the tree, you assign the root node one of the follow structures that adopt this protocol:

- [`BlendTreeBlendNode`](blendtreeblendnode.md), which branches the tree for every element in [`sources`](blendtreeblendnode/sources.md).
- [`BlendTreeSourceNode`](blendtreesourcenode.md), which defines an animation to blend with its [`source`](blendtreesourcenode/source.md) property.

> **Note**: A node in the tree may be of type [`BlendTreeInvalidNode`](blendtreeinvalidnode.md), which neither specifies a list of sources nor an animation.

Each node type supplies a name and weight, which you can set during or after initialization.

```swift
let animation1 = FromToByAnimation(...)

let blendNode = BlendTreeSourceNode(
    source: animation1,
    name: "Anim1",
    weight: .value(0.25))
```

## Topics

### Configuring the blend tree node
- [var name: String](blendtreenode/name.md)
  A textual name for the blend node.
- [var weight: BlendWeight](blendtreenode/weight.md)
  A normalized percentage that designates how much effect this node has relative to peer nodes.
### Blending animations
- [func blend(sources: [any BlendTreeNode], name: String, isAdditive: Bool) -> any BlendTreeNode](blend(sources:name:isadditive:).md)
  Combines the animations that result from the individual blend-tree nodes of the given array to a single blend-tree node.
- [func blend(any BlendTreeNode, any BlendTreeNode, name: String, isAdditive: Bool) -> any BlendTreeNode](blend(_:_:name:isadditive:).md)
  Combines the animations that result from two blend-tree nodes into a single blend-tree node.

## Relationships

### Conforming Types
- [BlendTreeBlendNode](blendtreeblendnode.md)
- [BlendTreeInvalidNode](blendtreeinvalidnode.md)
- [BlendTreeSourceNode](blendtreesourcenode.md)

## See Also

- [struct BlendTreeAnimation](blendtreeanimation.md)
  A collection of animations on the same property that the framework blends to a single animation.
- [struct BlendTreeBlendNode](blendtreeblendnode.md)
  A source node for an animation that mixes several animations to form a single animation.
- [struct BlendTreeSourceNode](blendtreesourcenode.md)
  A blend node that contains an animation.
- [struct BlendTreeInvalidNode](blendtreeinvalidnode.md)
  A blend tree node that’s internal only or sources from an invalid definition.
- [enum BlendWeight](blendweight.md)
  A numerical representation of the impact an animation has on a scene or entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/RealityKit/blendtreenode)*