# insertChildNode(_:at:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Adds a node to the node’s array of children at a specified index.

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
func insertChildNode(_ child: SCNNode, at index: Int)
```

```objc
- (void) insertChildNode:(SCNNode *) child atIndex:(NSUInteger) index;
```

## Parameters

- `child`: The node to be inserted.

  > ❗ **Important**:  Raises an exception ([`invalidArgumentException`](../../Foundation/nsexceptionname/invalidargumentexception.md)) if `child` is `nil`.
- `index`: The position at which to insert the new child node.

  > ❗ **Important**:  Raises an exception ([`rangeException`](../../Foundation/nsexceptionname/rangeexception.md)) if `index` is greater than the number of elements in the node’s [`childNodes`](./childnodes.md) array.

## See Also

### Managing the Node Hierarchy
- [var parent: SCNNode?](./parent.md)
  The node’s parent in the scene graph hierarchy.
- [var childNodes: [SCNNode]](./childnodes.md)
  An array of the node’s children in the scene graph hierarchy.
- [func addChildNode(SCNNode)](./addchildnode%28_%29.md)
  Adds a node to the node’s array of children.
- [func removeFromParentNode()](./removefromparentnode%28%29.md)
  Removes the node from its parent’s array of child nodes.
- [func replaceChildNode(SCNNode, with: SCNNode)](./replacechildnode%28_,with%29.md)
  Removes a child from the node’s array of children and inserts another node in its place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/insertchildnode(_:at:))*