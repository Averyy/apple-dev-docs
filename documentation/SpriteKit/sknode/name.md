# name

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The node’s assignable name.

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
var name: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * name;
```

## Mentions

- [Searching the Node Tree](../searching-the-node-tree.md)

#### Discussion

This property is used to identify a node in other parts of your game logic. For example, you might use this name as part of collision testing. You can also search for nodes in a tree by their name.

When choosing a name for a node, decide whether each node gets a unique name or whether some nodes will share a common name. If you give the node a unique name, you can find the node later by calling the [`childNode(withName:)`](./childnode%28withname%29.md) method. If a name is shared by multiple nodes, the name usually means that these are all a similar object type in your game. In this case, you can iterate over those objects by calling the [`enumerateChildNodes(withName:using:)`](./enumeratechildnodes%28withname,using%29.md) method.

## See Also

### Accessing Nodes by Name
- [Searching the Node Tree](../searching-the-node-tree.md)
  Access nodes by name to avoid needing an instance variable.
- [func childNode(withName: String) -> SKNode?](./childnode%28withname%29.md)
  Searches the children of the receiving node for a node with a specific name.
- [func enumerateChildNodes(withName: String, using: (SKNode, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratechildnodes%28withname,using%29.md)
  Searches the children of the receiving node to perform processing for nodes that share a name.
- [subscript(String) -> [SKNode]](./subscript%28_%29.md)
  Returns an array of nodes that match the name parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/name)*