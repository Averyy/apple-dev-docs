# move(toParent:)

**Framework**: SpriteKit  
**Kind**: method

Moves the node to a new parent node in the scene.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@MainActor
func move(toParent parent: SKNode)
```

#### Discussion

The node maintains its current position in scene coordinates.

## Parameters

- `parent`: An   object to move the receiver to. This node must be in the same scene as the node’s current parent.

## See Also

- [Accessing and Modifying the Node Tree](accessing-and-modifying-the-node-tree.md)
  See the objects and functions you use to control the node tree’s composition.
- [func addChild(SKNode)](sknode/addchild(_:).md)
  Adds a node to the end of the receiver’s list of child nodes.
- [func insertChild(SKNode, at: Int)](sknode/insertchild(_:at:).md)
  Inserts a node into a specific position in the receiver’s list of child nodes.
- [func isEqual(to: SKNode) -> Bool](sknode/isequal(to:).md)
  Compares the parameter node to the receiving node.
- [func removeFromParent()](sknode/removefromparent.md)
  Removes the receiving node from its parent.
- [func removeAllChildren()](sknode/removeallchildren.md)
  Removes all of the node’s children.
- [func removeChildren(in: [SKNode])](sknode/removechildren(in:).md)
  Removes a list of children from the receiving node.
- [func inParentHierarchy(SKNode) -> Bool](sknode/inparenthierarchy(_:).md)
  Returns a Boolean value that indicates whether the node is a descendant of the target node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/move(toparent:))*