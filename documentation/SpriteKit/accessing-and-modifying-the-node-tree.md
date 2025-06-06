# Accessing and Modifying the Node Tree

**Framework**: SpriteKit

See the objects and functions you use to control the node tree’s composition.

#### Overview

You create the node tree by creating parent-child relationships between nodes. Each node maintains an ordered list of children, referenced by reading the node’s `children` property. The order of the children in the tree affects many aspects of scene processing, including hit testing and rendering, so it’s important to organize the node tree appropriately.

| Method | Description |
| --- | --- |
| [`addChild(_:)`](sknode/addchild(_:).md) | Adds a node to the end of the receiver’s list of child nodes. |
| [`insertChild(_:at:)`](sknode/insertchild(_:at:).md) | Inserts a child into a specific position in the receiver’s list of child nodes. |
| [`removeFromParent()`](sknode/removefromparent().md) | Removes the receiving node from its parent. |

When you need to directly traverse the node tree, you use the properties in the following table to uncover the tree’s structure.

| Property | Description |
| --- | --- |
| [`children`](sknode/children.md) | The array of [`SKNode`](sknode.md) objects that are the receiving node’s children. |
| [`parent`](sknode/parent.md) | If the node is a child of another node, this property holds the parent. Otherwise, it holds `nil`. |
| [`scene`](sknode/scene.md) | If the node is included anywhere in a scene, this property returns the scene node that is the root of the tree. Otherwise it holds `nil`. |

## See Also

- [func addChild(SKNode)](sknode/addchild(_:).md)
  Adds a node to the end of the receiver’s list of child nodes.
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

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/accessing-and-modifying-the-node-tree)*