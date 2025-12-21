# sources

**Framework**: RealityKit  
**Kind**: property

The nodes that branch from a node to form part of a blend tree.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
var sources: [any BlendTreeNode]
```

#### Discussion

This node combines the animations of each member of this array to a single animation that represents a  of the sources. If a source is a [`BlendTreeSourceNode`](blendtreesourcenode.md), this structure blends its animation into the output. If a source is a [`BlendTreeBlendNode`](blendtreeblendnode.md), this structure blends the output of its sources into this structure’s output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/blendtreeblendnode/sources)*