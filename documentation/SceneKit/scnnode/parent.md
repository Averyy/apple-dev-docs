# parent

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The node’s parent in the scene graph hierarchy.

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
var parent: SCNNode? { get }
```

```objc
@property (nonatomic, readonly, nullable) SCNNode * parentNode;
```

## Discussion

For a scene’s [`rootNode`](../scnscene/rootnode.md) object, the value of this property is `nil`.

## See Also

### Managing the Node Hierarchy
- [var childNodes: [SCNNode]](./childnodes.md)
  An array of the node’s children in the scene graph hierarchy.
- [func addChildNode(SCNNode)](./addchildnode%28_%29.md)
  Adds a node to the node’s array of children.
- [func insertChildNode(SCNNode, at: Int)](./insertchildnode%28_,at%29.md)
  Adds a node to the node’s array of children at a specified index.
- [func removeFromParentNode()](./removefromparentnode%28%29.md)
  Removes the node from its parent’s array of child nodes.
- [func replaceChildNode(SCNNode, with: SCNNode)](./replacechildnode%28_,with%29.md)
  Removes a child from the node’s array of children and inserts another node in its place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/parent)*