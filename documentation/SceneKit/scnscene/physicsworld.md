# physicsWorld

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The physics simulation associated with the scene.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var physicsWorld: SCNPhysicsWorld { get }
```

```objc
@property (nonatomic, readonly) SCNPhysicsWorld * physicsWorld;
```

## Discussion

Every scene automatically creates a physics world object to simulate physics on nodes in the scene. You use this property to access the scene’s global physics properties, such as gravity, and to manage physics interactions between nodes. To make a node in the scene participate in the physics simulation, use either or both of its [`physicsBody`](../scnnode/physicsbody.md) and [`physicsField`](../scnnode/physicsfield.md) properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscene/physicsworld)*