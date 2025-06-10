# childNodes

**Framework**: SceneKit  
**Kind**: property

An array of the node’s children in the scene graph hierarchy.

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
var childNodes: [SCNNode] { get }
```

## See Also

- [var parent: SCNNode?](scnnode/parent.md)
  The node’s parent in the scene graph hierarchy.
- [func addChildNode(SCNNode)](scnnode/addchildnode(_:).md)
  Adds a node to the node’s array of children.
- [func insertChildNode(SCNNode, at: Int)](scnnode/insertchildnode(_:at:).md)
  Adds a node to the node’s array of children at a specified index.
- [func removeFromParentNode()](scnnode/removefromparentnode.md)
  Removes the node from its parent’s array of child nodes.
- [func replaceChildNode(SCNNode, with: SCNNode)](scnnode/replacechildnode(_:with:).md)
  Removes a child from the node’s array of children and inserts another node in its place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/childnodes)*