# scene

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The scene node that contains this node.

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
var scene: SKScene? { get }
```

```objc
@property (nonatomic, readonly, nullable) SKScene * scene;
```

## Mentions

- [Accessing and Modifying the Node Tree](../accessing-and-modifying-the-node-tree.md)

#### Discussion

If the node is not embedded in a scene, the value is `nil`.

## See Also

### Accessing Related Nodes
- [About SpriteKit Coordinate Systems](../about-spritekit-coordinate-systems.md)
  Learn how a node conforms to its coordinate systems.
- [var parent: SKNode?](./parent.md)
  The node’s parent node.
- [var children: [SKNode]](./children.md)
  The node’s children.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/scene)*