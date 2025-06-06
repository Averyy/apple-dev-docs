# physicsBody

**Framework**: SpriteKit  
**Kind**: property

The physics body associated with the node.

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
var physicsBody: SKPhysicsBody? { get set }
```

## Mentions

- [Getting Started with Physics Bodies](getting-started-with-physics-bodies.md)
- [Configuring a Physics Body](configuring-a-physics-body.md)

#### Discussion

The default value is `nil`, which indicates that the node does not participate in the physics simulation at all. If a physics body is provided, when the scene’s physics are simulated, the physics body updates the node’s position and rotates the node.

## See Also

- [Getting Started with Physics Bodies](getting-started-with-physics-bodies.md)
  Create and assign a physics body to enable physics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/physicsbody)*