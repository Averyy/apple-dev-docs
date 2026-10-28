# childNode(withName:recursively:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Returns the first node in the node’s child node subtree with the specified name.

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
func childNode(withName name: String, recursively: Bool) -> SCNNode?
```

```objc
- (SCNNode *) childNodeWithName:(NSString *) name recursively:(BOOL) recursively;
```

## Discussion

If the `recursive` parameter is [`true`](../../Swift/true.md), SceneKit uses a preorder traversal to search the child node subtree—that is, the block searches a node before it searches each of the node’s children, and it searches all children of a node before searching any of that node’s sibling nodes. Otherwise, SceneKit searches only those nodes in the node’s [`childNodes`](./childnodes.md) array.

## Parameters

- `name`: The name of the node to search for.
- `recursively`: [`true`](../../Swift/true.md) to search the entire child node subtree, or [`false`](../../Swift/false.md) to search only the node’s immediate children.

## See Also

### Searching the Node Hierarchy
- [func childNodes(passingTest: (SCNNode, UnsafeMutablePointer<ObjCBool>) -> Bool) -> [SCNNode]](./childnodes%28passingtest%29.md)
  Returns all nodes in the node’s child node subtree that satisfy the test applied by a block.
- [func enumerateChildNodes((SCNNode, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratechildnodes%28_%29.md)
  Executes the specified block for each of the node’s child and descendant nodes.
- [func enumerateHierarchy((SCNNode, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratehierarchy%28_%29.md)
  Executes the specified block for each of the node’s child and descendant nodes, as well as for the node itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/childnode(withname:recursively:))*