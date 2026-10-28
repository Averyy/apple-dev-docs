# enumerateHierarchy(_:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Executes the specified block for each of the node’s child and descendant nodes, as well as for the node itself.

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
func enumerateHierarchy(_ block: (SCNNode, UnsafeMutablePointer<ObjCBool>) -> Void)
```

```objc
- (void) enumerateHierarchyUsingBlock:(void (^)(SCNNode *node, BOOL *stop)) block;
```

## Discussion

SceneKit uses a recursive preorder traversal to process the child node subtree—that is, the block runs for a node before it runs for each of the node’s children, and it processes all children of a node before processing any of that node’s sibling nodes.

This method is equivalent to the [`enumerateChildNodes(_:)`](./enumeratechildnodes%28_%29.md) method, but unlike that method it also runs the block to process the node itself, not just its child nodes.

## Parameters

- `block`: The block to apply to the node’s child and descendant nodes.

  - The block takes two parameters:
  - - **child**: The child node currently being evaluated.

  - **stop**: A reference to a Boolean value. Set `*stop` to [`true`](../../Swift/true.md) in the block to abort further processing of the child node subtree.

## See Also

### Searching the Node Hierarchy
- [func childNodes(passingTest: (SCNNode, UnsafeMutablePointer<ObjCBool>) -> Bool) -> [SCNNode]](./childnodes%28passingtest%29.md)
  Returns all nodes in the node’s child node subtree that satisfy the test applied by a block.
- [func childNode(withName: String, recursively: Bool) -> SCNNode?](./childnode%28withname,recursively%29.md)
  Returns the first node in the node’s child node subtree with the specified name.
- [func enumerateChildNodes((SCNNode, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratechildnodes%28_%29.md)
  Executes the specified block for each of the node’s child and descendant nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/enumeratehierarchy(_:))*