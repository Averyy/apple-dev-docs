# insertChild(_:at:)

**Framework**: SpriteKit  
**Kind**: method

Inserts a node into a specific position in the receiver’s list of child nodes.

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
func insertChild(_ node: SKNode, at index: Int)
```

## Mentions

- [Accessing and Modifying the Node Tree](accessing-and-modifying-the-node-tree.md)

## Parameters

- `node`: The node to add. The node must not already have a parent.
- `index`: The position in the array to insert the node.

## See Also

- [Accessing and Modifying the Node Tree](accessing-and-modifying-the-node-tree.md)
  See the objects and functions you use to control the node tree’s composition.
- [func addChild(SKNode)](sknode/addchild(_:).md)
  Adds a node to the end of the receiver’s list of child nodes.
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

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/insertchild(_:at:))*