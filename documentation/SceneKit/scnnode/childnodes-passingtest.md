# childNodes(passingTest:)

**Framework**: SceneKit  
**Kind**: method

Returns all nodes in the node’s child node subtree that satisfy the test applied by a block.

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
func childNodes(passingTest predicate: (SCNNode, UnsafeMutablePointer<ObjCBool>) -> Bool) -> [SCNNode]
```

#### Return Value

An array containing nodes that passed the test.

#### Discussion

Use this method to search for nodes using a test you specify. For example, you can search for empty nodes using a block that returns YES for nodes whose [`light`](scnnode/light.md), [`camera`](scnnode/camera.md), and [`geometry`](scnnode/geometry.md) properties are all `nil`.

SceneKit uses a recursive preorder traversal to search the child node subtree—that is, the block searches a node before it searches each of the node’s children, and it searches all children of a node before searching any of that node’s sibling nodes.

## Parameters

- `predicate`: The block to apply to the node’s child and descendant nodes.

## See Also

- [func childNode(withName: String, recursively: Bool) -> SCNNode?](scnnode/childnode(withname:recursively:).md)
  Returns the first node in the node’s child node subtree with the specified name.
- [func enumerateChildNodes((SCNNode, UnsafeMutablePointer<ObjCBool>) -> Void)](scnnode/enumeratechildnodes(_:).md)
  Executes the specified block for each of the node’s child and descendant nodes.
- [func enumerateHierarchy((SCNNode, UnsafeMutablePointer<ObjCBool>) -> Void)](scnnode/enumeratehierarchy(_:).md)
  Executes the specified block for each of the node’s child and descendant nodes, as well as for the node itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/childnodes(passingtest:))*