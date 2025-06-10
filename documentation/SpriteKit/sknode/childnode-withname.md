# childNode(withName:)

**Framework**: SpriteKit  
**Kind**: method

Searches the children of the receiving node for a node with a specific name.

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
@MainActor
func childNode(withName name: String) -> SKNode?
```

## Mentions

- [Searching the Node Tree](searching-the-node-tree.md)

#### Return Value

If a node object with that name is found, the method returns the node object. Otherwise, it returns `nil`.

#### Discussion

If more than one child share the same name, the first node discovered is returned.

## Parameters

- `name`: The name to search for. This may be either the literal name of the node or a customized search string. See  .

## See Also

- [Searching the Node Tree](searching-the-node-tree.md)
  Access nodes by name to avoid needing an instance variable.
- [var name: String?](sknode/name.md)
  The node’s assignable name.
- [func enumerateChildNodes(withName: String, using: (SKNode, UnsafeMutablePointer<ObjCBool>) -> Void)](sknode/enumeratechildnodes(withname:using:).md)
  Searches the children of the receiving node to perform processing for nodes that share a name.
- [subscript(String) -> [SKNode]](sknode/subscript(_:).md)
  Returns an array of nodes that match the name parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/childnode(withname:))*