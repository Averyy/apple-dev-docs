# isEqual(to:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

Compares the parameter node to the receiving node.

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
func isEqual(to node: SKNode) -> Bool
```

```objc
- (BOOL) isEqualToNode:(SKNode *) node;
```

## Return Value

[`true`](../../Swift/true.md) if the node is a descendant of the `parent` node; otherwise [`false`](../../Swift/false.md).

## Parameters

- `node`: The node to compare to the receiving node.

## See Also

### Modifying the Node Tree
- [Accessing and Modifying the Node Tree](../accessing-and-modifying-the-node-tree.md)
  See the objects and functions you use to control the node tree’s composition.
- [func addChild(SKNode)](./addchild%28_%29.md)
  Adds a node to the end of the receiver’s list of child nodes.
- [func insertChild(SKNode, at: Int)](./insertchild%28_,at%29.md)
  Inserts a node into a specific position in the receiver’s list of child nodes.
- [func move(toParent: SKNode)](./move%28toparent%29.md)
  Moves the node to a new parent node in the scene.
- [func removeFromParent()](./removefromparent%28%29.md)
  Removes the receiving node from its parent.
- [func removeAllChildren()](./removeallchildren%28%29.md)
  Removes all of the node’s children.
- [func removeChildren(in: [SKNode])](./removechildren%28in%29.md)
  Removes a list of children from the receiving node.
- [func inParentHierarchy(SKNode) -> Bool](./inparenthierarchy%28_%29.md)
  Returns a Boolean value that indicates whether the node is a descendant of the target node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/isequal(to:))*