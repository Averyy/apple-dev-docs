# addChildNode(_:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Adds a node to the node’s array of children.

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
func addChildNode(_ child: SCNNode)
```

```objc
- (void) addChildNode:(SCNNode *) child;
```

## Discussion

Calling this method appends the node to the end of the [`childNodes`](./childnodes.md) array.

## Parameters

- `child`: The node to be added.

## See Also

### Managing the Node Hierarchy
- [var parent: SCNNode?](./parent.md)
  The node’s parent in the scene graph hierarchy.
- [var childNodes: [SCNNode]](./childnodes.md)
  An array of the node’s children in the scene graph hierarchy.
- [func insertChildNode(SCNNode, at: Int)](./insertchildnode%28_,at%29.md)
  Adds a node to the node’s array of children at a specified index.
- [func removeFromParentNode()](./removefromparentnode%28%29.md)
  Removes the node from its parent’s array of child nodes.
- [func replaceChildNode(SCNNode, with: SCNNode)](./replacechildnode%28_,with%29.md)
  Removes a child from the node’s array of children and inserts another node in its place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/addchildnode(_:))*