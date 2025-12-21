# BlendTreeSourceNode

**Framework**: RealityKit  
**Kind**: struct

A blend node that contains an animation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
struct BlendTreeSourceNode
```

#### Overview

This structure adopts [`BlendTreeNode`](blendtreenode.md) and adds the ability to store a single animation. A complete [`BlendTreeAnimation`](blendtreeanimation.md) represents a mix of all the animations that its source nodes contain. Each source node defines a [`weight`](blendtreesourcenode/weight.md) that determines how much effect the source’s animation has in the blend tree’s resulting, mixed animation. To define the source’s animation, set this structure’s [`source`](blendtreesourcenode/source.md) property.

##### Access a Source Node of a Blend Tree

A source may exist in any leaf-node position in the blend animation’s tree. The following code checks the root node for a source. If instead the root node is a branch, the code begins checking the branches sources.

```swift
// Check if the root node is a source.
if let blendNode = blendTree.root as? BlendTreeSourceNode {
    // Found a source.

// Check if the root node is a branch.
} else if let source = blendTree.root as? BlendTreeBlendNode {

        // Check for a source in the branch's sources.
        if let source = blendNode.sources[0] as? BlendTreeSourceNode {
            // Found a source.
        }
    }
}
```

## Topics

### Creating a blend tree animation node
- [init(source: any AnimationDefinition, name: String, weight: BlendWeight)](blendtreesourcenode/init(source:name:weight:).md)
  Creates a node that defines an animation within a tree of other blend nodes.
### Configuring a blend tree animation node
- [var name: String](blendtreesourcenode/name.md)
  A textual name for the blend node.
- [var source: (any AnimationDefinition)?](blendtreesourcenode/source.md)
  The blend node’s animation.
- [var weight: BlendWeight](blendtreesourcenode/weight.md)
  A normalized percentage that designates how much effect this node has compared to peer nodes.

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
- [struct BlendTreeInvalidNode](blendtreeinvalidnode.md)
  A blend tree node that’s internal only or sources from an invalid definition.
- [enum BlendWeight](blendweight.md)
  A numerical representation of the impact an animation has on a scene or entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/blendtreesourcenode)*