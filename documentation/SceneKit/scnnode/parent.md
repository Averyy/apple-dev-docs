# parent

**Framework**: SceneKit  
**Kind**: property

The node’s parent in the scene graph hierarchy.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var parent: SCNNode? { get }
```

#### Discussion

For a scene’s [`rootNode`](scnscene/rootnode.md) object, the value of this property is `nil`.

## See Also

- [var childNodes: [SCNNode]](scnnode/childnodes.md)
  An array of the node’s children in the scene graph hierarchy.
- [func addChildNode(SCNNode)](scnnode/addchildnode(_:).md)
  Adds a node to the node’s array of children.
- [func insertChildNode(SCNNode, at: Int)](scnnode/insertchildnode(_:at:).md)
  Adds a node to the node’s array of children at a specified index.
- [func removeFromParentNode()](scnnode/removefromparentnode.md)
  Removes the node from its parent’s array of child nodes.
- [func replaceChildNode(SCNNode, with: SCNNode)](scnnode/replacechildnode(_:with:).md)
  Removes a child from the node’s array of children and inserts another node in its place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/parent)*