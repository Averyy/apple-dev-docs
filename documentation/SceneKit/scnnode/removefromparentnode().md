# removeFromParentNode()

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Removes the node from its parent’s array of child nodes.

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
func removeFromParentNode()
```

```objc
- (void) removeFromParentNode;
```

#### Discussion

Removing nodes from the node hierarchy serves two purposes. Nodes own their contents (child nodes or attached lights, geometries, and other objects), so deallocating unneeded nodes can reduce memory usage. Additionally, SceneKit does more work at rendering time with a large, complex node hierarchy, so removing nodes whose contents you don’t need to display can improve rendering performance.

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
- [func replaceChildNode(SCNNode, with: SCNNode)](./replacechildnode%28_,with%29.md)
  Removes a child from the node’s array of children and inserts another node in its place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/removefromparentnode())*