# physicsWorld

**Framework**: SceneKit  
**Kind**: property

The physics simulation associated with the scene.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var physicsWorld: SCNPhysicsWorld { get }
```

#### Discussion

Every scene automatically creates a physics world object to simulate physics on nodes in the scene. You use this property to access the scene’s global physics properties, such as gravity, and to manage physics interactions between nodes. To make a node in the scene participate in the physics simulation, use either or both of its [`physicsBody`](scnnode/physicsbody.md) and [`physicsField`](scnnode/physicsfield.md) properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscene/physicsworld)*