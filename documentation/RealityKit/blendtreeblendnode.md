# BlendTreeBlendNode

**Framework**: RealityKit  
**Kind**: struct

A source node for an animation that mixes several animations to form a single animation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
struct BlendTreeBlendNode
```

#### Overview

A  mixes multiple animations to form a single animation. The [`BlendTreeBlendNode`](blendtreeblendnode.md) structure adopts the [`BlendTreeNode`](blendtreenode.md) protocol, which specifies the behavior of animations that make up a blend tree animation. This structure adds the ability to branch a blend tree at any point. Each member of this property’s [`sources`](blendtreeblendnode/sources.md) array represents a branch in the tree. For more information about blend trees, see [`BlendTreeAnimation`](blendtreeanimation.md).

## Topics

### Creating a blend-tree blend node
- [init(sources: [any BlendTreeNode], name: String, weight: BlendWeight, isAdditive: Bool)](blendtreeblendnode/init(sources:name:weight:isadditive:).md)
  Creates a tree node made up of multiple branches.
### Configuring the node
- [var name: String](blendtreeblendnode/name.md)
  A textual name for the blend node.
- [var weight: BlendWeight](blendtreeblendnode/weight.md)
  A normalized percentage that designates how much effect this node has compared to peer nodes.
- [var isAdditive: Bool](blendtreeblendnode/isadditive.md)
  A Boolean value that indicates whether the animation builds on the current state of the target entity or resets the state before running.
### Configuring child nodes
- [var sources: [any BlendTreeNode]](blendtreeblendnode/sources.md)
  The nodes that branch from a node to form part of a blend tree.

## Relationships

### Conforms To
- [BlendTreeNode](blendtreenode.md)

## See Also

- [struct BlendTreeAnimation](blendtreeanimation.md)
  A collection of animations on the same property that the framework blends to a single animation.
- [protocol BlendTreeNode](blendtreenode.md)
  An interface for a node that’s a member of a blend tree.
- [struct BlendTreeSourceNode](blendtreesourcenode.md)
  A blend node that contains an animation.
- [struct BlendTreeInvalidNode](blendtreeinvalidnode.md)
  A blend tree node that’s internal only or sources from an invalid definition.
- [enum BlendWeight](blendweight.md)
  A numerical representation of the impact an animation has on a scene or entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/blendtreeblendnode)*