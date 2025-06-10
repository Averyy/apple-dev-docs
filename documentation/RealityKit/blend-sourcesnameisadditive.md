# blend(sources:name:isAdditive:)

**Framework**: RealityKit  
**Kind**: func

Combines the animations that result from the individual blend-tree nodes of the given array to a single blend-tree node.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
func blend(sources: [any BlendTreeNode], name: String = "", isAdditive: Bool = false) -> any BlendTreeNode
```

#### Return Value

A blend-tree node that combines the given animations.

## Parameters

- `sources`: The blend-tree nodes to combine.
- `name`: A unique name for the combined node.
- `isAdditive`: A Boolean value that indicates whether the animation builds on   the current state of the target entity, or resets the state before running.

## See Also

- [func blend(any BlendTreeNode, any BlendTreeNode, name: String, isAdditive: Bool) -> any BlendTreeNode](blend(_:_:name:isadditive:).md)
  Combines the animations that result from two blend-tree nodes into a single blend-tree node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/blend(sources:name:isadditive:))*