# childNode(withName:recursively:)

**Framework**: SceneKit  
**Kind**: method

Returns the first node in the node’s child node subtree with the specified name.

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
func childNode(withName name: String, recursively: Bool) -> SCNNode?
```

#### Discussion

If the `recursive` parameter is [`true`](https://developer.apple.com/documentation/swift/true), SceneKit uses a preorder traversal to search the child node subtree—that is, the block searches a node before it searches each of the node’s children, and it searches all children of a node before searching any of that node’s sibling nodes. Otherwise, SceneKit searches only those nodes in the node’s [`childNodes`](scnnode/childnodes.md) array.

## Parameters

- `name`: The name of the node to search for.
- `recursively`:   to search the entire child node subtree, or   to search only the node’s immediate children.

## See Also

- [func childNodes(passingTest: (SCNNode, UnsafeMutablePointer<ObjCBool>) -> Bool) -> [SCNNode]](scnnode/childnodes(passingtest:).md)
  Returns all nodes in the node’s child node subtree that satisfy the test applied by a block.
- [func enumerateChildNodes((SCNNode, UnsafeMutablePointer<ObjCBool>) -> Void)](scnnode/enumeratechildnodes(_:).md)
  Executes the specified block for each of the node’s child and descendant nodes.
- [func enumerateHierarchy((SCNNode, UnsafeMutablePointer<ObjCBool>) -> Void)](scnnode/enumeratehierarchy(_:).md)
  Executes the specified block for each of the node’s child and descendant nodes, as well as for the node itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/childnode(withname:recursively:))*