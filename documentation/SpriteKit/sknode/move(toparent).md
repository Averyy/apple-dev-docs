# move(toParent:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

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
func move(toParent parent: SKNode)
```

```objc
- (void) moveToParent:(SKNode *) parent;
```

#### Discussion

The node maintains its current position in scene coordinates.

## Parameters

- `parent`: An [`SKNode`](../sknode.md) object to move the receiver to. This node must be in the same scene as the node’s current parent.

## See Also

### Modifying the Node Tree
- [Accessing and Modifying the Node Tree](../accessing-and-modifying-the-node-tree.md)
  See the objects and functions you use to control the node tree’s composition.
- [func addChild(SKNode)](./addchild%28_%29.md)
  Adds a node to the end of the receiver’s list of child nodes.
- [func insertChild(SKNode, at: Int)](./insertchild%28_,at%29.md)
  Inserts a node into a specific position in the receiver’s list of child nodes.
- [func isEqual(to: SKNode) -> Bool](./isequal%28to%29.md)
  Compares the parameter node to the receiving node.
- [func removeFromParent()](./removefromparent%28%29.md)
  Removes the receiving node from its parent.
- [func removeAllChildren()](./removeallchildren%28%29.md)
  Removes all of the node’s children.
- [func removeChildren(in: [SKNode])](./removechildren%28in%29.md)
  Removes a list of children from the receiving node.
- [func inParentHierarchy(SKNode) -> Bool](./inparenthierarchy%28_%29.md)
  Returns a Boolean value that indicates whether the node is a descendant of the target node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/move(toparent:))*