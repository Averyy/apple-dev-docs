# physicsWorld

**Framework**: SpriteKit  
**Kind**: property

The physics simulation associated with the scene.

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
var physicsWorld: SKPhysicsWorld { get }
```

#### Discussion

Every scene automatically creates a physics world object to simulate physics on nodes in the scene. You use this property to access the scene’s global physics properties, such as gravity. To add physics to a particular node, see [`physicsBody`](sknode/physicsbody.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skscene/physicsworld)*