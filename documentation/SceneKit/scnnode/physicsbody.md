# physicsBody

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The physics body associated with the node.

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
var physicsBody: SCNPhysicsBody? { get set }
```

```objc
@property (nonatomic, retain, nullable) SCNPhysicsBody * physicsBody;
```

#### Discussion

The default value is `nil`, specifying that the node does not participate in the physics simulation at all. If you provide a physics body, SceneKit updates the node’s position and orientation each time it processes a step of its physics simulation. For more information on SceneKit’s physics system, see [`SCNPhysicsWorld`](../scnphysicsworld.md).

## See Also

### Adding Physics to a Node
- [var physicsField: SCNPhysicsField?](./physicsfield.md)
  The physics field associated with the node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/physicsbody)*