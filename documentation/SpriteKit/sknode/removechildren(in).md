# removeChildren(in:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

Removes a list of children from the receiving node.

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
func removeChildren(in nodes: [SKNode])
```

```objc
- (void) removeChildrenInArray:(NSArray<SKNode *> *) nodes;
```

## Parameters

- `nodes`: An array of `SKNode` objects that are all children of the receiving node.

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
- [func move(toParent: SKNode)](./move%28toparent%29.md)
  Moves the node to a new parent node in the scene.
- [func removeFromParent()](./removefromparent%28%29.md)
  Removes the receiving node from its parent.
- [func removeAllChildren()](./removeallchildren%28%29.md)
  Removes all of the node’s children.
- [func inParentHierarchy(SKNode) -> Bool](./inparenthierarchy%28_%29.md)
  Returns a Boolean value that indicates whether the node is a descendant of the target node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/removechildren(in:))*