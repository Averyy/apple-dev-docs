# parent

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The node’s parent node.

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
var parent: SKNode? { get }
```

```objc
@property (nonatomic, readonly, nullable) SKNode * parent;
```

## Mentions

- [Accessing and Modifying the Node Tree](../accessing-and-modifying-the-node-tree.md)

#### Discussion

If the node is not in a node tree, the value is `nil`.

## See Also

### Accessing Related Nodes
- [About SpriteKit Coordinate Systems](../about-spritekit-coordinate-systems.md)
  Learn how a node conforms to its coordinate systems.
- [var scene: SKScene?](./scene.md)
  The scene node that contains this node.
- [var children: [SKNode]](./children.md)
  The node’s children.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/parent)*