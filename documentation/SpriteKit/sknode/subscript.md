# subscript(_:)

**Framework**: SpriteKit  
**Kind**: subscript

Returns an array of nodes that match the name parameter.

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
subscript(name: String) -> [SKNode] { get }
```

## Mentions

- [Searching the Node Tree](searching-the-node-tree.md)

#### Return Value

An array of `SKNode` objects that match the name. If no matching nodes are found, an empty array is returned.

## Parameters

- `name`: The name to search for. This may be either the literal name of the node or a customized search string. See  .

## See Also

- [Searching the Node Tree](searching-the-node-tree.md)
  Access nodes by name to avoid needing an instance variable.
- [var name: String?](sknode/name.md)
  The node’s assignable name.
- [func childNode(withName: String) -> SKNode?](sknode/childnode(withname:).md)
  Searches the children of the receiving node for a node with a specific name.
- [func enumerateChildNodes(withName: String, using: (SKNode, UnsafeMutablePointer<ObjCBool>) -> Void)](sknode/enumeratechildnodes(withname:using:).md)
  Searches the children of the receiving node to perform processing for nodes that share a name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/subscript(_:))*