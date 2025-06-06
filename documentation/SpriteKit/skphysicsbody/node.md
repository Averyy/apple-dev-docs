# node

**Framework**: SpriteKit  
**Kind**: property

The node that this body is connected to.

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
weak var node: SKNode? { get }
```

#### Discussion

You associate the body with a node by assigning it to the [`physicsBody`](sknode/physicsbody.md) property of the [`SKNode`](sknode.md) object. If the body is not associated with a node, the value is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsbody/node)*