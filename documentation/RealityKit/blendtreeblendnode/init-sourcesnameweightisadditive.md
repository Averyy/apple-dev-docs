# init(sources:name:weight:isAdditive:)

**Framework**: RealityKit  
**Kind**: init

Creates a tree node made up of multiple branches.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
init(sources: [any BlendTreeNode], name: String = "", weight: BlendWeight = .value(1.0), isAdditive: Bool = false)
```

## Parameters

- `sources`: The nodes that branch from this node to form part of a blend tree.
- `name`: A textual name for the node.
- `weight`: A normalized percentage that designates how much this node’s   animation influences the tree’s blended animation.
- `isAdditive`: A Boolean value that indicates whether the animation   builds on the current state of the target entity or resets the state   before running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/blendtreeblendnode/init(sources:name:weight:isadditive:))*