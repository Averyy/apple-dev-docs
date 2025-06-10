# removeFromParentNode()

**Framework**: SceneKit  
**Kind**: method

Removes the node from its parent’s array of child nodes.

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
func removeFromParentNode()
```

#### Discussion

Removing nodes from the node hierarchy serves two purposes. Nodes own their contents (child nodes or attached lights, geometries, and other objects), so deallocating unneeded nodes can reduce memory usage. Additionally, SceneKit does more work at rendering time with a large, complex node hierarchy, so removing nodes whose contents you don’t need to display can improve rendering performance.

## See Also

- [var parent: SCNNode?](scnnode/parent.md)
  The node’s parent in the scene graph hierarchy.
- [var childNodes: [SCNNode]](scnnode/childnodes.md)
  An array of the node’s children in the scene graph hierarchy.
- [func addChildNode(SCNNode)](scnnode/addchildnode(_:).md)
  Adds a node to the node’s array of children.
- [func insertChildNode(SCNNode, at: Int)](scnnode/insertchildnode(_:at:).md)
  Adds a node to the node’s array of children at a specified index.
- [func replaceChildNode(SCNNode, with: SCNNode)](scnnode/replacechildnode(_:with:).md)
  Removes a child from the node’s array of children and inserts another node in its place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/removefromparentnode())*