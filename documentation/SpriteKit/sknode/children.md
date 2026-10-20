# children

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The node’s children.

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
var children: [SKNode] { get }
```

```objc
@property (nonatomic, readonly) NSArray<SKNode *> * children;
```

## Mentions

- [Accessing and Modifying the Node Tree](../accessing-and-modifying-the-node-tree.md)
- [Controlling User Interaction on Nodes](../controlling-user-interaction-on-nodes.md)

#### Discussion

The objects in this array are all `SKNode` objects.

## See Also

### Accessing Related Nodes
- [About SpriteKit Coordinate Systems](../about-spritekit-coordinate-systems.md)
  Learn how a node conforms to its coordinate systems.
- [var scene: SKScene?](./scene.md)
  The scene node that contains this node.
- [var parent: SKNode?](./parent.md)
  The node’s parent node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/children)*