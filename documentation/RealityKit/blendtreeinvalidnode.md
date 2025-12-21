# BlendTreeInvalidNode

**Framework**: RealityKit  
**Kind**: struct

A blend tree node that’s internal only or sources from an invalid definition.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
struct BlendTreeInvalidNode
```

#### Overview

This structure adopts [`BlendTreeNode`](blendtreenode.md) and adds the ability to detect a node that contains neither an animation nor any branches in the blend tree.

You don’t create instances of this structure. Instead, detect whether your blend-tree node matches the framework’s criteria for invalid nodes by checking the node type, as the following code demonstrates.

```swift
// Get the blend tree's root node.
guard let blendNode = blendTree.root as? BlendTreeBlendNode else { return }
for node in blendNode.sources {
    if let invalidNode = node as? BlendTreeInvalidNode {
        // Respond to invalid-node criteria.
```

## Topics

### Configuring the blend tree invalid node
- [var name: String](blendtreeinvalidnode/name.md)
  A textual name for the blend node.
- [var weight: BlendWeight](blendtreeinvalidnode/weight.md)
  The amount that an animation impacts the entity it applies to.

## Relationships

### Conforms To
- [BlendTreeNode](blendtreenode.md)

## See Also

- [struct BlendTreeAnimation](blendtreeanimation.md)
  A collection of animations on the same property that the framework blends to a single animation.
- [protocol BlendTreeNode](blendtreenode.md)
  An interface for a node that’s a member of a blend tree.
- [struct BlendTreeBlendNode](blendtreeblendnode.md)
  A source node for an animation that mixes several animations to form a single animation.
- [struct BlendTreeSourceNode](blendtreesourcenode.md)
  A blend node that contains an animation.
- [enum BlendWeight](blendweight.md)
  A numerical representation of the impact an animation has on a scene or entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/blendtreeinvalidnode)*