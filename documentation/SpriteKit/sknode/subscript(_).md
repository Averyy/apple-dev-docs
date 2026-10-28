# subscript(_:)

**Framework**: SpriteKit  
**Kind**: subscript  
**Role**: Instance Subscript

Returns an array of nodes that match the name parameter.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
subscript(name: String) -> [SKNode] { get }
```

```objc
- (NSArray<SKNode *> *) objectForKeyedSubscript:(NSString *) name;
```

## Mentions

- [Searching the Node Tree](../searching-the-node-tree.md)

## Return Value

An array of `SKNode` objects that match the name. If no matching nodes are found, an empty array is returned.

## Parameters

- `name`: The name to search for. This may be either the literal name of the node or a customized search string. See `Searching the Node Tree`.

## See Also

### Accessing Nodes by Name
- [Searching the Node Tree](../searching-the-node-tree.md)
  Access nodes by name to avoid needing an instance variable.
- [var name: String?](./name.md)
  The node’s assignable name.
- [func childNode(withName: String) -> SKNode?](./childnode%28withname%29.md)
  Searches the children of the receiving node for a node with a specific name.
- [func enumerateChildNodes(withName: String, using: (SKNode, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratechildnodes%28withname,using%29.md)
  Searches the children of the receiving node to perform processing for nodes that share a name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/subscript(_:))*