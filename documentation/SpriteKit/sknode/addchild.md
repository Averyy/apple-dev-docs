# addChild(_:)

**Framework**: SpriteKit  
**Kind**: method

Adds a node to the end of the receiver’s list of child nodes.

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
func addChild(_ node: SKNode)
```

## Mentions

- [Accessing and Modifying the Node Tree](accessing-and-modifying-the-node-tree.md)

## Parameters

- `node`: The node to add. The node must not already have a parent.

## See Also

- [Accessing and Modifying the Node Tree](accessing-and-modifying-the-node-tree.md)
  See the objects and functions you use to control the node tree’s composition.
- [func insertChild(SKNode, at: Int)](sknode/insertchild(_:at:).md)
  Inserts a node into a specific position in the receiver’s list of child nodes.
- [func isEqual(to: SKNode) -> Bool](sknode/isequal(to:).md)
  Compares the parameter node to the receiving node.
- [func move(toParent: SKNode)](sknode/move(toparent:).md)
  Moves the node to a new parent node in the scene.
- [func removeFromParent()](sknode/removefromparent.md)
  Removes the receiving node from its parent.
- [func removeAllChildren()](sknode/removeallchildren.md)
  Removes all of the node’s children.
- [func removeChildren(in: [SKNode])](sknode/removechildren(in:).md)
  Removes a list of children from the receiving node.
- [func inParentHierarchy(SKNode) -> Bool](sknode/inparenthierarchy(_:).md)
  Returns a Boolean value that indicates whether the node is a descendant of the target node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/addchild(_:))*