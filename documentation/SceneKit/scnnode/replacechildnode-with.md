# replaceChildNode(_:with:)

**Framework**: SceneKit  
**Kind**: method

Removes a child from the node’s array of children and inserts another node in its place.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func replaceChildNode(_ oldChild: SCNNode, with newChild: SCNNode)
```

#### Discussion

If both the `oldChild` and `newChild` nodes are children of the node, calling this method swaps their positions in the array. Note that removing a node from the node hierarchy may result in it being deallocated.

Calling this method results in undefined behavior if the `oldChild` parameter doesn’t refer to a child of this node.

## Parameters

- `oldChild`: The existing child node to be replaced.
- `newChild`: The node with which to replace the child node.

## See Also

- [var parent: SCNNode?](scnnode/parent.md)
  The node’s parent in the scene graph hierarchy.
- [var childNodes: [SCNNode]](scnnode/childnodes.md)
  An array of the node’s children in the scene graph hierarchy.
- [func addChildNode(SCNNode)](scnnode/addchildnode(_:).md)
  Adds a node to the node’s array of children.
- [func insertChildNode(SCNNode, at: Int)](scnnode/insertchildnode(_:at:).md)
  Adds a node to the node’s array of children at a specified index.
- [func removeFromParentNode()](scnnode/removefromparentnode.md)
  Removes the node from its parent’s array of child nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/replacechildnode(_:with:))*