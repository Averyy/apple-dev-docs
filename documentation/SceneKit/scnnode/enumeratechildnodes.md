# enumerateChildNodes(_:)

**Framework**: SceneKit  
**Kind**: method

Executes the specified block for each of the node’s child and descendant nodes.

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
func enumerateChildNodes(_ block: (SCNNode, UnsafeMutablePointer<ObjCBool>) -> Void)
```

#### Discussion

SceneKit uses a recursive preorder traversal to process the child node subtree—that is, the block runs for a node before it runs for each of the node’s children, and it processes all children of a node before processing any of that node’s sibling nodes.

## Parameters

- `block`: The block to apply to the node’s child and descendant nodes.

## See Also

- [func childNodes(passingTest: (SCNNode, UnsafeMutablePointer<ObjCBool>) -> Bool) -> [SCNNode]](scnnode/childnodes(passingtest:).md)
  Returns all nodes in the node’s child node subtree that satisfy the test applied by a block.
- [func childNode(withName: String, recursively: Bool) -> SCNNode?](scnnode/childnode(withname:recursively:).md)
  Returns the first node in the node’s child node subtree with the specified name.
- [func enumerateHierarchy((SCNNode, UnsafeMutablePointer<ObjCBool>) -> Void)](scnnode/enumeratehierarchy(_:).md)
  Executes the specified block for each of the node’s child and descendant nodes, as well as for the node itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/enumeratechildnodes(_:))*