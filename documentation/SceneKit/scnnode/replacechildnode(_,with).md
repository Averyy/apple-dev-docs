# replaceChildNode(_:with:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Removes a child from the node’s array of children and inserts another node in its place.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
func replaceChildNode(_ oldChild: SCNNode, with newChild: SCNNode)
```

```objc
- (void) replaceChildNode:(SCNNode *) oldChild with:(SCNNode *) newChild;
```

## Discussion

If both the `oldChild` and `newChild` nodes are children of the node, calling this method swaps their positions in the array. Note that removing a node from the node hierarchy may result in it being deallocated.

Calling this method results in undefined behavior if the `oldChild` parameter doesn’t refer to a child of this node.

## Parameters

- `oldChild`: The existing child node to be replaced.
- `newChild`: The node with which to replace the child node.

  > ❗ **Important**:  Raises an exception ([`invalidArgumentException`](../../Foundation/nsexceptionname/invalidargumentexception.md)) if `newChild` is `nil`.

## See Also

### Managing the Node Hierarchy
- [var parent: SCNNode?](./parent.md)
  The node’s parent in the scene graph hierarchy.
- [var childNodes: [SCNNode]](./childnodes.md)
  An array of the node’s children in the scene graph hierarchy.
- [func addChildNode(SCNNode)](./addchildnode%28_%29.md)
  Adds a node to the node’s array of children.
- [func insertChildNode(SCNNode, at: Int)](./insertchildnode%28_,at%29.md)
  Adds a node to the node’s array of children at a specified index.
- [func removeFromParentNode()](./removefromparentnode%28%29.md)
  Removes the node from its parent’s array of child nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/replacechildnode(_:with:))*